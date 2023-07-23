import multiprocessing
import time

start = time.perf_counter()


def worker():
    print('Sleeping for 1 seconds')
    time.sleep(1)
    print('Done sleeping')

p1 = multiprocessing.Process(target=worker)
p2 = multiprocessing.Process(target=worker)

p1.start()
p2.start()

p1.join()
p2.join()


finish = time.perf_counter()

print(f'It took {round(finish-start, 3)} to finish')



