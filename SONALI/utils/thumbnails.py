from config import YOUTUBE_IMG_URL
from youtubesearchpython.__future__ import VideosSearch
from PIL import Image, ImageDraw, ImageFilter
import requests
from io import BytesIO

async def get_thumb(videoid):
    try:
        query = f"https://www.youtube.com/watch?v={videoid}"
        results = VideosSearch(query, limit=1)
        for result in (await results.next())["result"]:
            thumbnail_url = result["thumbnails"][0]["url"].split("?")[0]
        
        return process_image(thumbnail_url)
    except Exception as e:
        return YOUTUBE_IMG_URL


async def get_qthumb(vidid):
    try:
        query = f"https://www.youtube.com/watch?v={vidid}"
        results = VideosSearch(query, limit=1)
        for result in (await results.next())["result"]:
            thumbnail_url = result["thumbnails"][0]["url"].split("?")[0]
        
        return process_image(thumbnail_url)
    except Exception as e:
        return YOUTUBE_IMG_URL


def process_image(image_url):
    try:
        # Fetch the image
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        
        # Make the thumbnail a circle
        mask = Image.new("L", img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + img.size, fill=255)

        # Apply the mask to make the image circular
        circular_img = Image.new("RGBA", img.size)
        circular_img.paste(img, (0, 0), mask=mask)

        # Blur the background
        blurred_img = img.filter(ImageFilter.GaussianBlur(10))
        
        # Paste the circular image onto the blurred background
        final_img = blurred_img.copy()
        final_img.paste(circular_img, (0, 0), circular_img)

        # Save or return the final image
        output = BytesIO()
        final_img.save(output, format="PNG")
        return output.getvalue()
        
    except Exception as e:
        print(f"Error processing image: {e}")
        return None
