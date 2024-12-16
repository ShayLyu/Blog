from PIL import Image, ImageDraw

# 打开原始图片
image = Image.open("avatar.jpg").convert("RGBA")

# 确定图片的尺寸
width, height = image.size
size = min(width, height)

# 创建一个圆形蒙版
mask = Image.new("L", (size, size), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, size, size), fill=255)

# 裁剪原始图片为正方形，并应用圆形蒙版
image = image.crop(((width - size) // 2, (height - size) // 2, (width + size) // 2, (height + size) // 2))
image.putalpha(mask)  # 应用透明圆形蒙版

# 保存为透明背景的 PNG
image.save("avatar-round.png", format="PNG")
