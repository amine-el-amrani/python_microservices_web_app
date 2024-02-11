import pika 



params = pika.URLParameters('amqps://ljyikwmt:QhVdM0cVxpbc1hdA7NR3Hv1Yc6_vQygV@rat.rmq2.cloudamqp.com/ljyikwmt')


connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Recieve in Admin')
    print((body))


channel.basic_consume(queue='admin', on_message_callback=callback)


print('started Consuming')

channel.start_consuming()

channel.close()