import pika 



params = pika.URLParameters('amqps://ljyikwmt:QhVdM0cVxpbc1hdA7NR3Hv1Yc6_vQygV@rat.rmq2.cloudamqp.com/ljyikwmt')


connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('Recieve in main')
    print((body))


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)


print('started Consuming')

channel.start_consuming()

channel.close()