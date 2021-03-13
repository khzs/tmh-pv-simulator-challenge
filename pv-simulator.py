from commonpvs import connection, channel, QUEUE_NAME


def process_data(chan, method, properties, body):
    print(str(body))


if __name__ == '__main__':
    channel.basic_consume(queue = QUEUE_NAME,
                          on_message_callback = process_data)
    try:
        channel.start_consuming()
    except KeyboardInterrupt as ex:
        channel.stop_consuming()
        connection.close()
