from celery import Celery

app_celery = Celery(
    broker='pyamqp://guest@localhost//'
)


@app_celery.task
def hello_world():
    return 'Hello World'