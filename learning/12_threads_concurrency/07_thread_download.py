import threading
import requests
import time

def download_image(image_url):
    print(f"Downloading image from {image_url}...")
    resp = requests.get(image_url)
    print(f"Image downloaded from {image_url}., size {len(resp.content)} bytes")

urls = [
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/webp",
]

start_time = time.time()
threads = []

for url in urls:
    t = threading.Thread(target=download_image, args=(url,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end_time = time.time()
print(f"Total time taken: {end_time - start_time:.2f} seconds")