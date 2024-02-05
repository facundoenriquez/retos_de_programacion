from PIL import Image
import requests
from io import BytesIO
img_url = "https://c4.wallpaperflare.com/wallpaper/219/190/360/ensiferum-fantasy-folk-heavy-wallpaper-preview.jpg"

response = requests.get(img_url)
img = Image.open(BytesIO(response.content))
width, height = img.size
ratio = width / height
print(f"Ratio: {ratio:.2f}")
