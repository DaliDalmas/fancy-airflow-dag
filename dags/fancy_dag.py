from airflow.decorators import dag, task, task_group
from datetime import datetime
from airflow.providers.amazon.aws.transfers.sql_to_s3 import SqlToS3Operator
from sql_scripts.queries import get_customers_with_active_products, get_customers_info

from airflow.models import Variable
from airflow.models.connection import Connection
from airflow.models.baseoperator import chain


iam_role = Variable.get('iam_role')
bucket_name = Variable.get('bucket_name')
customers_conn = 'customers'
products_conn = 'products' 

dag_description = """
This is a daily dag created as an illustration on how to 
use decorators to create airflow dags. On top of that
the dag illustrates how to integrate airflow with aws s3
"""


@dag(
    dag_id="fancy_dag",
    description=dag_description,
    start_date=datetime(2025, 3, 5),
    schedule="@daily",
    tags=["daily", "fancy", "s3"],
    catchup=False,
    owner_links={"DaliCodes": "https://www.dalmasotieno.com"},
    max_active_runs=1,
)
def fancy_dag():

    @task_group(group_id="active_customers")
    def active_customers():

        @task_group(group_id="from_db_to_s3_queries")
        def from_db_to_s3_queries():
            customers_info = SqlToS3Operator(
                task_id="get_customers_info",
                sql_conn_id=customers_conn,
                query=get_customers_info["query"],
                s3_bucket=bucket_name,
                s3_key=get_customers_info["key"],
                replace=True,
                file_format="parquet"
            )

            active_products = SqlToS3Operator(
                task_id="get_customers_with_active_products",
                sql_conn_id=products_conn,
                query=get_customers_with_active_products["query"],
                s3_bucket=bucket_name,
                s3_key=get_customers_with_active_products["key"],
                replace=True,
                file_format="parquet",
            )

        active_customers_queries = from_db_to_s3_queries()

        @task(task_id="transform_active_customers")
        def transform():
            print("Transform")

        transform_process = transform()

        chain(
            active_customers_queries,
            transform_process
        )

    active_customers_table = active_customers()


my_dag = fancy_dag()
