import os
import re
import aiohttp
import aiofiles
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps, ImageEnhance
from youtubesearchpython import VideosSearch

def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(image.size[0] * widthRatio)
    newHeight = int(image.size[1] * heightRatio)
    return image.resize((newWidth, newHeight), Image.ANTIALIAS)

def crop_center_triangle(image, size, border):
    width, height = image.size
    new_image = image.crop(((width - size) // 2, (height - size) // 2, (width + size) // 2, (height + size) // 2))
    return ImageOps.expand(new_image, border=border, fill=(255, 255, 255))

def create_gradient(size, colors):
    width, height = size
    gradient = Image.new('RGB', (width, height), color=0)
    draw = ImageDraw.Draw(gradient)

    for i, color in enumerate(colors):
        draw.rectangle([i * (width // len(colors)), 0, (i + 1) * (width // len(colors)), height], fill=color)
    
    return gradient

def truncate(text):
    words = text.split()
    if len(words) > 2:
        return ' '.join(words[:2]), ' '.join(words[2:])
    return text, ''

async def get_thumb(videoid):
    if os.path.isfile(f"cache/{videoid}_v4.png"):
        return f"cache/{videoid}_v4.png"

    url = f"https://www.youtube.com/watch?v={videoid}"
    results = VideosSearch(url, limit=1)
    for result in (await results.next())["result"]:
        try:
            title = result["title"]
            title = re.sub("\W+", " ", title)
            title = title.title()
        except:
            title = "Unsupported Title"
        try:
            duration = result["duration"]
        except:
            duration = "Unknown Mins"
        thumbnail = result["thumbnails"][0]["url"].split("?")[0]
        try:
            views = result["viewCount"]["short"]
        except:
            views = "Unknown Views"
        try:
            channel = result["channel"]["name"]
        except:
            channel = "Unknown Channel"

    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open(f"cache/thumb{videoid}.png", mode="wb")
                await f.write(await resp.read())
                await f.close()
                youtube = Image.open(f"cache/thumb{videoid}.png")

    # Resize the image
    image1 = changeImageSize(1280, 720, youtube)
    image2 = image1.convert("RGBA")

    # Blur the entire background
    blurred_background = image2.filter(ImageFilter.BoxBlur(20))

    # Enhance brightness
    enhancer = ImageEnhance.Brightness(blurred_background)
    blurred_background = enhancer.enhance(0.6)

    # Now we create a gradient colorful border
    border_width = 30  # Width of the colorful stripe
    gradient_colors = ["#FF5733", "#33FF57", "#5733FF", "#FF33A8", "#FFDF33"]  # Some vibrant colors
    gradient_border = create_gradient((blurred_background.width + 2 * border_width, 
                                       blurred_background.height + 2 * border_width), gradient_colors)
    
    # Add the colored gradient border
    bordered_image = ImageOps.expand(blurred_background, border=border_width, fill=0)
    bordered_image.paste(gradient_border, (0, 0))

    # Drawing the elements (title, views, channel, etc.)
    draw = ImageDraw.Draw(bordered_image)
    arial = ImageFont.truetype("SONALI/assets/assets/font2.ttf", 30)
    title_font = ImageFont.truetype("SONALI/assets/assets/font3.ttf", 45)

    # Circular thumbnail
    circle_thumbnail = crop_center_triangle(youtube, 400, 20)
    circle_thumbnail = circle_thumbnail.resize((400, 400))

    # Position of the sharp triangle thumbnail
    circle_position = (120, 160)
    bordered_image.paste(circle_thumbnail, circle_position, circle_thumbnail)

    # Add the text and other elements on top of the blurred background
    text_x_position = 565
    title1 = truncate(title)
    draw.text((text_x_position, 180), title1[0], fill=(255, 255, 255), font=title_font)
    draw.text((text_x_position, 230), title1[1], fill=(255, 255, 255), font=title_font)
    draw.text((text_x_position, 320), f"{channel}  |  {views[:23]}", (255, 255, 255), font=arial)

    # Line under the title
    line_length = 580  
    red_length = int(line_length * 0.6)
    white_length = line_length - red_length

    start_point_red = (text_x_position, 380)
    end_point_red = (text_x_position + red_length, 380)
    draw.line([start_point_red, end_point_red], fill="#4CBB17", width=9)

    start_point_white = (text_x_position + red_length, 380)
    end_point_white = (text_x_position + line_length, 380)
    draw.line([start_point_white, end_point_white], fill="white", width=8)

    # Circle at the end of the line
    circle_radius = 10 
    circle_position = (end_point_red[0], end_point_red[1])
    draw.ellipse([circle_position[0] - circle_radius, circle_position[1] - circle_radius,
                  circle_position[0] + circle_radius, circle_position[1] + circle_radius], fill="#4CBB17")
    
    draw.text((text_x_position, 400), "00:00", (255, 255, 255), font=arial)
    draw.text((1080, 400), duration, (255, 255, 255), font=arial)

    # Play icons
    play_icons = Image.open("SONALI/assets/assets/BABYMUSICPNG.png")
    play_icons = play_icons.resize((620, 150))
    bordered_image.paste(play_icons, (text_x_position, 455), play_icons)

    try:
        os.remove(f"cache/thumb{videoid}.png")
    except:
        pass

    # Save the final image
    bordered_image.save(f"cache/{videoid}_v4.png")
    return f"cache/{videoid}_v4.png"
