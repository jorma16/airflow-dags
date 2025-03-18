from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {"owner": "airflow", "start_date": days_ago(1)}

with DAG(
    dag_id="hello_world_kubernetes",
    default_args=default_args,
    schedule_interval="* * * * *",
    catchup=False,
) as dag:
    kubernetes_task = KubernetesPodOperator(
        namespace="airflow",
        image="python:3.11-slim",
        cmds=["python", "-c"],
        arguments=["print('Hello World')"],
        labels={"foo": "bar"},
        name="hello_world",
        task_id="kubernetes_task",
        get_logs=True,
    )

    bash_task = BashOperator(
        task_id="bash_task",
        bash_command="echo hello",
    )

    kubernetes_task >> bash_task
