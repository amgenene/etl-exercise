This project is a simple ETL pipeline built with Python, Docker, and PostgreSQL. It exposes an API endpoint that triggers the ETL process when accessed. The ETL process loads data from CSV files, derives some features from the data, and uploads it into a PostgreSQL table.

Prerequisites:
- Docker
- Python 3.7+
- PostgreSQL

Instructions:
1. Clone this repository.
2. Run the application: `docker-compose up`
3. After the application has started you can run `curl http://localhost:8000/compounds`, `curl http://localhost:8000/users` and `curl http://localhost:8000/experiments` to get the json representation of the data that was entered into the tables
4. You can also enter the container's database: `docker exec -it <name of container> psql -U newuser -d newdb`
5. And check the data in the database: `select * from user_experiments`, `select * from compounds`, and `select * from users`