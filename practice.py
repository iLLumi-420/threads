import concurrent.futures
import time


start = time.perf_counter()

def worker(seconds):
    print(f'Sleeping for {seconds} seconds')
    time.sleep(seconds)
    return f'Done sleeping for {seconds}'

seconds = [5,4,3,2,1]

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(worker, sec) for sec in seconds]

    for f in concurrent.futures.as_completed(results):
        print(f.result())


# threads = []
# for _ in range(10):
#     t = threading.Thread(target=worker)
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()


finish = time.perf_counter()

print(f'Completed in {round(finish-start,3)} seconds')
