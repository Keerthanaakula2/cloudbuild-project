from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def print_hello():
    return "Hello world!"

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 8, 14),
    'retries': 1,
}

dag = DAG(
    'hello_world_dag',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
)

task = PythonOperator(
    task_id='print_hello_task',
    python_callable=print_hello,
    dag=dag,
)

task