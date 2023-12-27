import pytesseract 
from PIL import Image
from PIL import ImageFilter
from scipy.ndimage import gaussian_filter
import numpy

# image = Image.open("/home/my/Desktop/test/seleniumRepo/test2.jpg")
# saveIm = image.filter(ImageFilter.GaussianBlur(radius= 5))
# saveIm.save("newImage.png")
# # image.filter()
# image2 = Image.open("/home/my/Desktop/test/seleniumRepo/final.png")
# text = pytesseract.image_to_string(image, lang='eng',config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789').strip()
# print(text)

# th1 = 140
# th2 = 140  # threshold after blurring
# sig = 1.5  
# black_and_white = image.convert("L")  # converting to black and white
# # black_and_white.save("black_and_white.png")
# first_threshold = black_and_white.point(lambda p: p > th1 and 255)
# # first_threshold.save("first_threshold.png")
# blur = numpy.array(first_threshold)  # create an image array
# blurred = gaussian_filter(blur, sigma=sig)
# blurred = Image.fromarray(blurred)
# # blurred.save("blurred.png")
# final = blurred.point(lambda p: p > th2 and 255)
# final = final.filter(ImageFilter.EDGE_ENHANCE_MORE)
# final = final.filter(ImageFilter.SHARPEN)
# final.save("final.png")
# number = pytesseract.image_to_string(Image.open('test2.jpg'))
# image2 = Image.open("/home/my/Desktop/test/seleniumRepo/final.png")

image = Image.open("/home/my/Desktop/test/seleniumRepo/Draft.png")
text = pytesseract.image_to_string(image)
print(text)