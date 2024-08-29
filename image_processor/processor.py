from PIL import Image

def open_image(path):
    return Image.open(path)

def show_image(image):
    image.show()

def rotate_image(image,degree):
    return image.rotate(degree)

def crop_image(image,box):
    return image.crop(box)