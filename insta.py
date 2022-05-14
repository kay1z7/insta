from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os

for kk in os.listdir('.'):
    if img.endswith('.jpg'):
        img = Image.open(kk)
        fn, flext = os.path.splitext(kk)

        lol = img.convert('L')
        lol1 = lol.filter(ImageFilter.DETAIL)
        lol2 = lol1.resize((1080, 1080))
        width, height = lol2.size

        draw = ImageDraw.Draw(lol2)
        text = "WATERMARK"
        title = "WHITE"
        font = ImageFont.truetype("arial.ttf", 80)
        textwidth, textheight = draw.textsize(text, font)

        margin = 10
        x = width - textwidth - margin
        y = height - textheight - margin

        draw.text((x, y), text, title, font=font)

        lol2.save('kk/{}{}'.format(fn, flext))
