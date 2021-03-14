from pika import BlockingConnection, ConnectionParameters

start_time = 0
resolution = 60 * 60
stop_time = 24 * resolution
interval = 5

queue_name = 'meter'

connection = BlockingConnection(ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue = queue_name, auto_delete = True)
