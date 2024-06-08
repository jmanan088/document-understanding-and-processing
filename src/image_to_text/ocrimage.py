from PIL import Image

import pytesseract


path = '/code/src/image_to_text/';
print(pytesseract.image_to_string(Image.open(path + 'test1.jpeg')))