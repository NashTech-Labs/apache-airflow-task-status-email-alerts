from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.email import send_email

def failure_function(context):
    dag_run = context.get('dag_run')
    msg = "The folder you are trying to open doesn't exist hence the task has Failed."
    subject = f"DAG {dag_run} Failed"
    send_email(to='sakshim969@gmail.com', subject=subject, html_content=msg)

def success_function(context):
    dag_run = context.get('dag_run')
    msg = "Echoed Hello hence the task has executed successfully."
    subject = f"DAG {dag_run} has completed"
    send_email(to='sakshim969@gmail.com', subject=subject, html_content=msg)

default_args = {
    'owner': 'Sakshi',
    'start_date': datetime(2022, 3, 21), 
}

with DAG('check_task_status_pass_fail',
        default_args=default_args,
        description='A simple job to nofity user about the execution status of their specified tasks.',
        schedule_interval='@daily',
        catchup=False
         ) as dag:

    say_hello = BashOperator(
        task_id='say_hello',
        on_failure_callback=failure_function,
        on_success_callback=success_function,
        bash_command='echo Hello' 
    )

    open_temp_folder = BashOperator(
        task_id='open_temp_folder',
        on_failure_callback=failure_function,
        on_success_callback=success_function,
        bash_command='cd temp_folder'
    )
say_hello >> open_temp_folder