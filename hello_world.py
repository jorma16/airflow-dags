from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
from airflow.utils.dates import days_ago

default_args = {"ownser": "airflow", "start_date": days_ago(1)}

with DAG(
    dag_id="hello_world_kubernetes",
    default_args=default_args,
    schedule_interval="@once",  # "* * * * *"
    catchup=False,
) as dag:
    hello_world = KubernetesPodOperator(
        namespace="airflow",
        image="python:3.11-slim",
        cmds=["python", "-c"],
        arguments=["print('Hello World')"],
        labels={"foo": "bar"},
        name="hello_world",
        task_id="hello_world_task",
        get_logs=True,
    )

    hello_world
