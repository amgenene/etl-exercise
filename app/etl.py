import pandas as pd
from sqlalchemy import create_engine

def run_etl_process():
    try:
        users_df = pd.read_csv('/data/users.csv', encoding='utf-8-sig', sep='\s*,\s*', engine='python')
        experiments_df = pd.read_csv('/data/user_experiments.csv', encoding='utf-8-sig', sep='\s*,\s*', engine='python')
        compounds_df = pd.read_csv('/data/compounds.csv', encoding='utf-8-sig', sep='\s*,\s*', engine='python')
        # Derive features
        total_experiments = experiments_df.groupby('user_id').experiment_compound_ids.count().reset_index(name='total_experiments')
        avg_experiments = total_experiments['total_experiments'].mean()
        most_common_compounds = experiments_df['experiment_compound_ids'].str.split(';').explode().mode()[0]

        # # Upload data to postgres
        result = pd.merge(experiments_df, total_experiments, on="user_id", how="left")
        result['most_common_compound'] = most_common_compounds
        result['avg_experiments'] = avg_experiments
        engine = create_engine('postgresql://newuser:newpassword@db:5432/newdb')
        with engine.connect() as connection:
            users_df.to_sql('users', con=connection, if_exists='replace')
            experiments_df.to_sql('experiments', con=connection, if_exists='replace')
            compounds_df.to_sql('compounds', con=connection, if_exists='replace')
            # Upload derived features
            result.to_sql('user_experiments', engine, if_exists='replace', index=False)
    except Exception as e:
        print(f"An error occurred: {e}")   

