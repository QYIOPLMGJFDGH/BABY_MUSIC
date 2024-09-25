from config import YOUTUBE_IMG_URL
from youtubesearchpython.__future__ import VideosSearch
from PIL import Image, ImageFilter
import requests
from io import BytesIO

async def get_thumb(videoid):
    try:
        query = f"https://www.youtube.com/watch?v={videoid}"
        results = VideosSearch(query, limit=1)
        for result in (await results.next())["result"]:
            thumbnail_url = result["thumbnails"][0]["url"].split("?")[0]

        # Fetch the thumbnail image
        response = requests.get(thumbnail_url)
        img = Image.open(BytesIO(response.content))

        # Apply a blur effect to the image
        blurred_img = img.filter(ImageFilter.GaussianBlur(10))  # You can adjust the radius

        # Save or return the blurred image
        blurred_img.show()  # This will display the image
        return blurred_img  # You can save or return it as needed

    except Exception as e:
        return YOUTUBE_IMG_URL

async def get_qthumb(vidid):
    try:
        query = f"https://www.youtube.com/watch?v={vidid}"
        results = VideosSearch(query, limit=1)
        for result in (await results.next())["result"]:
            thumbnail_url = result["thumbnails"][0]["url"].split("?")[0]

        # Fetch the thumbnail image
        response = requests.get(thumbnail_url)
        img = Image.open(BytesIO(response.content))

        # Apply a blur effect to the image
        blurred_img = img.filter(ImageFilter.GaussianBlur(10))  # Adjust the radius as needed

        # Save or return the blurred image
        blurred_img.show()  # Display the image
        return blurred_img  # You can save or return it as needed

    except Exception as e:
        return YOUTUBE_IMG_URL
