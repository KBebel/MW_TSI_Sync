# import itertools

# example = ['left', 'right', 'up', 'down']
# dup = ['left', 'right', 'up', 'down']

# for i, text in enumerate(example):
#     print(i, '-->', text)

from time import sleep

# def callback_a(i, result):
#     print("Items processed: {}. Running result: {}.".format(i, result))

# def square(i):
#     return i * i

# def processor(process, times, report_interval, callback):
#     print("Entered processor(): times = {}, report_interval = {}, callback = {}".format(
#     times, report_interval, callback.__name__))
#     # Can also use callback.__name__ instead of callback.func_name in line above.
#     result = 0
#     print("Processing data ...")
#     for i in range(1, times + 1):
#         result += process(i)
#         sleep(1)
#         if i % report_interval == 0:
#             # This is the call to the callback function
#             # that was passed to this function.
#             callback(i, result)

# processor(square, 20, 5, callback_a)

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-19s) %(message)s',)

def wait_for_event(e):
    logging.debug('wait_for_event starting')
    event_is_set = e.wait()
    logging.debug('event set: %s', event_is_set)

def wait_for_event_timeout(e, t):
    while not e.isSet():
        logging.debug('wait_for_event_timeout starting')
        event_is_set = e.wait(t)
        logging.debug('event set: %s', event_is_set)
        if event_is_set:
            logging.debug('processing event')
        else:
            logging.debug('doing other things')

if __name__ == '__main__':
    e = threading.Event()
    t1 = threading.Thread(name='blocking',
                      target=wait_for_event,
                      args=(e,))
    t1.start()

    t2 = threading.Thread(name='non-blocking',
                      target=wait_for_event_timeout,
                      args=(e, 2))
    t2.start()

    logging.debug('Waiting before calling Event.set()')
    time.sleep(3)
    e.set()
    logging.debug('Event is set')