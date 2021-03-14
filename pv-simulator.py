from random import uniform
from scipy.interpolate import InterpolatedUnivariateSpline

from commonpvs import connection, channel, QUEUE_NAME


graph_points = [(0, 0),
                (1, 0),
                (2, 0),
                (3, 0),
                (4, 0),
                (6, 0.1),
                (8, 0.4),
                (12, 2.7),
                (14, 3.2),
                (16, 3),
                (20, 0.1),
                (21, 0),
                (22, 0),
                (23, 0),
                (24, 0)
                ]

x = [i[0] * 60 * 60 for i in graph_points]
y = [i[1] * 1000 for i in graph_points]
interpolation_function = InterpolatedUnivariateSpline(x, y)


def simulator(timestamp):
    reading = interpolation_function(int(timestamp))
    noise = uniform(-1, 1) * (reading * 0.05)
    return round(max(0, reading + noise), 2)

def process_data(chan, method, properties, body):
    timestamp, formatted_time, meter_value = str(body)[2:-1].split(",")
    pvs_value = simulator(timestamp)
    print(timestamp, formatted_time, meter_value, pvs_value)


if __name__ == '__main__':
    channel.basic_consume(queue = QUEUE_NAME,
                          on_message_callback = process_data)
    try:
        channel.start_consuming()
    except KeyboardInterrupt as ex:
        channel.stop_consuming()
        connection.close()
