import pika
import json
import time


def connect_to_rabbitmq():
    while True:
        try:
            # Your AMQP URL parameters, create a free account in https://customer.cloudamqp.com/login and a create a new instance
            params = params = pika.URLParameters('amqps://ljyikwmt:QhVdM0cVxpbc1hdA7NR3Hv1Yc6_vQygV@rat.rmq2.cloudamqp.com/ljyikwmt')
            connection = pika.BlockingConnection(params)
            channel = connection.channel()
            return connection, channel
        except pika.exceptions.AMQPConnectionError:
            print("Connexion à RabbitMQ échouée. Tentative de reconnexion...")
            time.sleep(5)  # Attendre 5 secondes avant de réessayer

def publish_safe(method, body):
    connection, channel = connect_to_rabbitmq()
    try:
        properties = pika.BasicProperties(
            content_type='application/json',
            headers={'event_type': method}
        )
        channel.basic_publish(
            exchange='',
            routing_key='main',
            body=json.dumps(body),
            properties=properties
        )
    except (pika.exceptions.ConnectionClosedByBroker, pika.exceptions.StreamLostError):
        print("La connexion ou le canal a été fermé. Tentative de reconnexion et de republication...")
        connection, channel = connect_to_rabbitmq()
        channel.basic_publish(
            exchange='',
            routing_key='main',
            body=json.dumps(body),
            properties=properties
        )
    finally:
        connection.close()
