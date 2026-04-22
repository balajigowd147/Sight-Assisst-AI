from PIL import Image , ImageOps , ImageEnhance

def image_loading(image_path):
    image  = Image.open(image_path)
    max_size = 320
    image.thumbnail((max_size,max_size),Image.Resampling.LANCZOS)
    return image
    