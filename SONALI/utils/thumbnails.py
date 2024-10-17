import os
import re
import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from youtubesearchpython.__future__ import VideosSearch

async def get_thumb(videoid):
    if os.path.isfile(f"cache/{videoid}_v4.png"):
        return f"cache/{videoid}_v4.png"

    url = f"https://www.youtube.com/watch?v={videoid}"
    results = VideosSearch(url, limit=1)
    for result in (await results.next())["result"]:
        title = re.sub("\W+", " ", result.get("title", "Unsupported Title")).title()
        duration = result.get("duration", "Unknown Mins")
        thumbnail = result["thumbnails"][0]["url"].split("?")[0]
        views = result.get("viewCount", {}).get("short", "Unknown Views")
        channel = result.get("channel", {}).get("name", "Unknown Channel")

    # Download thumbnail
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                async with aiofiles.open(f"cache/thumb{videoid}.png", mode="wb") as f:
                    await f.write(await resp.read())
                youtube = Image.open(f"cache/thumb{videoid}.png")

    # Process the image
    background = ImageEnhance.Brightness(
        youtube.convert("RGBA").filter(ImageFilter.BoxBlur(20))
    ).enhance(0.6)
    
    draw = ImageDraw.Draw(background)
    title_font = ImageFont.truetype("SONALI/assets/assets/font3.ttf", 45)
    arial = ImageFont.truetype("SONALI/assets/assets/font2.ttf", 30)

    # Circular cropped thumbnail
    def crop_center_circle(img, size):
        mask = Image.new("L", (size, size), 0)
        draw_mask = ImageDraw.Draw(mask)
        draw_mask.ellipse((0, 0, size, size), fill=255)
        img = img.resize((size, size))
        result = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        result.paste(img, (0, 0), mask)
        return result

    circle_thumbnail = crop_center_circle(youtube, 400)
    background.paste(circle_thumbnail, (120, 160), circle_thumbnail)

    # Text and line
    title_lines = [line.strip() for line in re.findall(r'.{1,30}(?:\s+|$)', title)]
    draw.text((565, 180), title_lines[0], fill="white", font=title_font)
    if len(title_lines) > 1:
        draw.text((565, 230), title_lines[1], fill="white", font=title_font)
    draw.text((565, 320), f"{channel}  |  {views}", fill="white", font=arial)

    # Line and play icons
    draw.line([(565, 380), (905, 380)], fill="#4CBB17", width=9)
    draw.line([(905, 380), (1145, 380)], fill="white", width=8)
    draw.ellipse([(905 - 10, 370), (905 + 10, 390)], fill="#4CBB17")
    draw.text((565, 400), "00:00", fill="white", font=arial)
    draw.text((1080, 400), duration, fill="white", font=arial)

    play_icons = Image.open("SONALI/assets/assets/BABYMUSICPNG.png").resize((620, 150))
    background.paste(play_icons, (565, 455), play_icons)

    # Clean up and save
    os.remove(f"cache/thumb{videoid}.png")
    background.save(f"cache/{videoid}_v4.png")
    return f"cache/{videoid}_v4.png"
