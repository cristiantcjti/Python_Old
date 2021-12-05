<h1>STARTING SERVICES</h1>
<u1>
    <h2>docker run -d -p 5672:5672 rabbitmq</h2>
    <h2>pip install gevent</h2>
    <h2>celery -A tasks worker -l info -P gevent</h2> 
    <h2>celery flower --port=5566</h2>
    <h2>flower -A tasks</h2>
    <h2>celery -A tasks flower  --address=127.0.0.6 --port=5566</h2>
<u1>