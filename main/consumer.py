import pika 
import json
from main import Product, db, app

params = pika.URLParameters('amqps://ljyikwmt:QhVdM0cVxpbc1hdA7NR3Hv1Yc6_vQygV@rat.rmq2.cloudamqp.com/ljyikwmt')


connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('Received in main')
    data = json.loads(body)
    print(data)
    event_type = properties.headers.get('event_type')

    # Creating an application context
    with app.app_context():
        try:
            if event_type == 'product_created':
                product = Product(id=data['id'], title=data['title'], image=data['image'])
                db.session.add(product)
                db.session.commit()
                print('Product created:', data['id'])

            elif event_type == 'product_updated':
                product = db.session.get(Product, data['id'])
                if product:
                    product.title = data['title']
                    product.image = data['image']
                    db.session.commit()
                    print('Product updated:', data['id'])
                else:
                    print('Product to update not found:', data['id'])

            elif event_type == 'product_deleted':
                product_id = data
                product = db.session.get(Product, product_id)
                if product:
                    db.session.delete(product)
                    db.session.commit()
                    print('Product deleted:', product_id)
                else:
                    print('Product to delete not found:', product_id)


        except Exception as e:
            print(f'Error processing message: {e}')



channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)


print('started Consuming')

channel.start_consuming()

channel.close()