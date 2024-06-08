from PIL import Image
import pytesseract


#extracting text from image
def gettext(filepath):

    text = pytesseract.image_to_string(Image.open(filepath + 'test1.jpeg'))
    return text