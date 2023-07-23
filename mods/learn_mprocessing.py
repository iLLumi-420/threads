import concurrent.futures
import time

start = time.perf_counter()


def worker(seconds):
    print(f'Sleeping for {seconds} seconds')
    time.sleep(seconds)
    return f'Done sleeping for {seconds}'


with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    
    results = executor.map(worker, secs)
    
    for result in results:
        print(result)

# processes = []
# for _ in range(10):
#     p = multiprocessing.Process(target=worker, args=[1.5])
#     p.start()
#     processes.append(p)

# for process in processes:
#     process.join()



finish = time.perf_counter()

print(f'It took {round(finish-start, 3)} to finish')



