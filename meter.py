from pika import BasicProperties
from random import uniform
from time import strftime, gmtime
from tqdm import tqdm
from commonpvs import connection, channel, QUEUE_NAME


if __name__ == '__main__':
    START_TIME = 0
    STOP_TIME = 24 * 60 * 60
    INTERVAL = 5

    for timestamp in tqdm(range(START_TIME, STOP_TIME, INTERVAL), desc= 'Sending meter values'):
        formatted_time = strftime("%H:%M:%S", gmtime(timestamp))
        consumption = '{:.2f}'.format(uniform(0.0, 9000.0))

        channel.basic_publish(exchange = '',
                              routing_key = QUEUE_NAME,
                              body = f'{timestamp},{formatted_time},{consumption}',
                              properties = BasicProperties(delivery_mode = 2))

    connection.close()
