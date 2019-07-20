import PIL
from PIL import Image
def open_image(path):
    im = Image.open(path)
    return im


def save_image(image, path):
    image.save(path, 'png')


def get_pixel(image, x, y):
    width, height = image.size
    if x > width or y > height:
        return None
    pixel = image.getpixel((x, y))
    return pixel


def change_pixel(image, x, y, r, g, b, a):
    pix = image.load()
    pix[x, y] = (r, g, b, a)
    return image

def charToBin(char):
    return bin(ord(char))[2:]
