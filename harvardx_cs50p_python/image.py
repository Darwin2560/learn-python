from PIL import Image, ImageFilter


def main():
    with Image.open("homero simpson.jpg") as img:
        img = img.rotate(180)
        img = img.filter(ImageFilter.FIND_EDGES)
        img.save("homero simpson out.jpg")


main()
