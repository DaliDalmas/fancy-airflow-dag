-- on fancy airflow  db
CREATE USER fancy_airflow_user WITH PASSWORD 'fancy_airflow_user';
GRANT ALL PRIVILEGES ON DATABASE fancy_airflow TO fancy_airflow_user;
GRANT ALL ON SCHEMA public TO fancy_airflow_user;

-- on  fancy customers  db
GRANT ALL PRIVILEGES ON DATABASE fancy_customers TO fancy_airflow_user;
GRANT ALL ON SCHEMA public TO fancy_airflow_user;

-- on fancy products
GRANT ALL PRIVILEGES ON DATABASE fancy_products TO fancy_airflow_user;
GRANT ALL ON SCHEMA public TO fancy_airflow_user;