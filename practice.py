import threading
import time


start = time.perf_counter()

def worker():
    print('Sleeping for 2 second')
    time.sleep(2)
    print('Done sleeping')



t1 = threading.Thread(target=worker)
t2 = threading.Thread(target=worker)


t1.start()
t2.start()

t1.join()
t2.join()


finish = time.perf_counter()

print(f'Completed in {round(finish-start,3)} seconds')

