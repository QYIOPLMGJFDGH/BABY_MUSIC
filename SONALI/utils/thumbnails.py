from config import YOUTUBE_IMG_URL
from youtubesearchpython import VideosSearch


from PIL import Image, ImageDraw, ImageFilter
import requests
from io import BytesIO

async def get_thumb(videoid):
    try:
        query = f"https://www.youtube.com/watch?v={videoid}"
        results = VideosSearch(query, limit=1)
        for result in (await results.next())["result"]:
            thumbnail_url = result["thumbnails"][0]["url"].split("?")[0]
            
            # Fetch the image
            response = requests.get(thumbnail_url)
            img = Image.open(BytesIO(response.content))

            # Create circular crop
            np_img = img.convert("RGB")
            np_img = np_img.resize((200, 200))  # Resize as needed
            mask = Image.new('L', np_img.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0) + np_img.size, fill=255)

            thumb_with_circle = Image.new("RGB", np_img.size)
            thumb_with_circle.paste(np_img, mask=mask)

            # Apply background blur
            blurred_img = img.filter(ImageFilter.GaussianBlur(10))

            # Save or return the modified image
            thumb_with_circle.show()  # This displays the image
            
            return thumbnail_url  # Or save the modified image as needed
    except Exception as e:
        return YOUTUBE_IMG_URL



async def get_qthumb(vidid):
    try:
        query = f"https://www.youtube.com/watch?v={vidid}"
        results = VideosSearch(query, limit=1)
        for result in (await results.next())["result"]:
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
        return thumbnail
    except Exception as e:
        return YOUTUBE_IMG_URLE_IMG_URL
