import concurrent.futures
import time
from PIL import Image, ImageFilter

start = time.perf_counter()

size = (1200, 1200)

img_names = [
    'photo-1532009324734-20a7a5813719.jpg',
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1524429656589-6633a470097c.jpg',
    'photo-1530224264768-7ff8c1789d79.jpg',
    'photo-1564135624576-c5c88640f235.jpg',
    'photo-1541698444083-023c97d3f4b6.jpg',
    'photo-1522364723953-452d3431c267.jpg',
    'photo-1493976040374-85c8e12f0c0e.jpg',
    'photo-1504198453319-5ce911bafcde.jpg',
]

def load_image(img_name):
    image = Image.open(img_name)
    print(f'{img_name} was loaded')
    return image


def process_image(img_name, image):
    try:
        image = image.filter(ImageFilter.GaussianBlur(15))
        image.thumbnail(size)
        image.save(f'processed/{img_name}')
        print('Image was processed')
    except:
        print('Processing failed')


with concurrent.futures.ThreadPoolExecutor() as executor:
    images = executor.map(load_image, img_names)

with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(process_image, img_names, images)


finish = time.perf_counter()

print(f'It took {round(finish-start, 3)} to finish')