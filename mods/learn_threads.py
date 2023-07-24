import concurrent.futures
import time
import requests

start = time.perf_counter()

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
]


    
def download_image(url):
    img_bytes = requests.get(url).content
    img_name = url.split('/')[3]
    img_name = f'{img_name}.jpg'

    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was dowloaded')

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(download_image, img_urls)


finish = time.perf_counter()

print(f'Completed in {round(finish-start,3)} seconds')
