import pika 
import json
import os
import django

# Django initialization to access Django models and other functionalities outside of a Django application.
# This is required because we are using Django models outside of the django app, necessitating the setup of Django's environment settings.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admin.settings')
django.setup()

from products.models import Product


params = pika.URLParameters('your_rabbitmq_url')


connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Recieve in Admin')
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.like + 1
    product.save()
    print('Product likes increased!')

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)


print('started Consuming')

channel.start_consuming()

channel.close()