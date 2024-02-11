import pika 



params = pika.URLParameters('amqps://ljyikwmt:QhVdM0cVxpbc1hdA7NR3Hv1Yc6_vQygV@rat.rmq2.cloudamqp.com/ljyikwmt')


connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello')