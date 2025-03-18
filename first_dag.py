"""
* Importing the DAG class to create DAG's instance
* dates utilities provided by airflow
* There are various operators available in airflow but this time we'll
only use BashOperator. Executors are nothing but handles using which you
can execute your task.
"""
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash_operator import BashOperator

"""
my_dag is an instance of DAG with respective dag_id and is scheduled
for daily. you can also give cron like syntax for scheduling.
"""
my_dag = DAG(
        dag_id = "helloworld",
        schedule_interval = "@daily",
        start_date = days_ago(1)
        )

"""
Now we've created a task that will be a part of my_dag
"""
task_1 = BashOperator(
       task_id = "t1",
       bash_command = "echo hello",
       dag = my_dag
        )