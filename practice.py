import threading
import time


start = time.perf_counter()

def worker():
    print('Sleeping for 2 second')
    time.sleep(2)
    print('Done sleeping')


threads = []
for _ in range(10):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()


finish = time.perf_counter()

print(f'Completed in {round(finish-start,3)} seconds')

