from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultPhoto,
)
from youtubesearchpython import VideosSearch
from PIL import Image, ImageDraw, ImageFilter, ImageOps
import requests
from io import BytesIO
from SONALI import app
from SONALI.utils.inlinequery import answer
from config import BANNED_USERS

# Image processing function
def process_thumbnail(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return None  # Handle the case where the image cannot be retrieved

        img = Image.open(BytesIO(response.content)).convert("RGBA")

        # Resize the image to a smaller square size, keeping its aspect ratio
        img.thumbnail((500, 500))

        # Create a circular mask
        mask = Image.new("L", img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, img.size[0], img.size[1]), fill=255)

        # Apply the circular mask to the image
        img_with_circle = ImageOps.fit(img, mask.size, centering=(0.5, 0.5))
        img_with_circle.putalpha(mask)

        # Create a blurred background from the original image
        blurred_bg = img.filter(ImageFilter.GaussianBlur(15))

        # Composite the circular image onto the blurred background
        final_img = Image.alpha_composite(blurred_bg, img_with_circle)

        # Save the processed image
        final_img_path = "processed_thumbnail.png"
        final_img.save(final_img_path)

        return final_img_path

    except Exception as e:
        print(f"Error processing the image: {e}")
        return None

@app.on_inline_query(~BANNED_USERS)
async def inline_query_handler(client, query):
    text = query.query.strip().lower()
    answers = []
    
    if text == "":
        try:
            await client.answer_inline_query(query.id, results=answer, cache_time=10)
            return
        except Exception as e:
            print(f"Error answering inline query: {e}")
            return

    try:
        a = VideosSearch(text, limit=20)
        result = (await a.next()).get("result")

        for x in range(min(15, len(result))):  # Ensure we don't go out of bounds
            video_info = result[x]
            title = video_info["title"].title()
            duration = video_info["duration"]
            views = video_info["viewCount"]["short"]
            thumbnail = video_info["thumbnails"][0]["url"].split("?")[0]
            channellink = video_info["channel"]["link"]
            channel = video_info["channel"]["name"]
            link = video_info["link"]
            published = video_info["publishedTime"]
            description = f"{views} | {duration} ᴍɪɴᴜᴛᴇs | {channel} | {published}"

            buttons = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="ʏᴏᴜᴛᴜʙᴇ 🎄",
                            url=link,
                        )
                    ],
                ]
            )
            
            # Process the thumbnail (make it circular with blurred background)
            processed_thumbnail = process_thumbnail(thumbnail)
            if processed_thumbnail is None:
                continue  # Skip if thumbnail processing failed
            
            searched_text = f"""
❍ <b>ᴛɪᴛʟᴇ :</b> <a href={link}>{title}</a>

❍ <b>ᴅᴜʀᴀᴛɪᴏɴ :</b> {duration} ᴍɪɴᴜᴛᴇs
❍ <b>ᴠɪᴇᴡs :</b> <code>{views}</code>
❍ <b>ᴄʜᴀɴɴᴇʟ :</b> <a href={channellink}>{channel}</a>
❍ <b>ᴘᴜʙʟɪsʜᴇᴅ ᴏɴ :</b> {published}

<u><b>➻ ɪɴʟɪɴᴇ sᴇᴀʀᴄʜ ᴍᴏᴅᴇ ʙʏ {app.name}</b></u"""
            
            answers.append(
                InlineQueryResultPhoto(
                    photo_url=processed_thumbnail,
                    title=title,
                    thumb_url=processed_thumbnail,
                    description=description,
                    caption=searched_text,
                    reply_markup=buttons,
                )
            )

        if answers:  # Only answer if we have results
            await client.answer_inline_query(query.id, results=answers)

    except Exception as e:
        print(f"Error during inline query processing: {e}")
