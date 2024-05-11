import cv2

ASCII_CHARS = "@%#*+=-:_ "
ASCII_RANGE = 256 / len(ASCII_CHARS)


def image_to_ascii(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ascii_image = ""
    for row in gray_image:
        for pixel in row:
            ascii_image += ASCII_CHARS[int(pixel / ASCII_RANGE)]
        ascii_image += "\n"
    return ascii_image


image = cv2.imread("ayasofya.png")
# image = cv2.resize(image, (width, height)) # if you resize the image, you can get better results

ascii_img = image_to_ascii(image)

with open("ascii_image.txt", "w") as f:
    f.write(ascii_img)

print("The image converted to ASCII was saved to the file 'ascii_image.txt'.")
