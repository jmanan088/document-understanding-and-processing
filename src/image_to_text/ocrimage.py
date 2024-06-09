from PIL import Image
import pytesseract


#extracting text from image
def gettext(img):

    text = pytesseract.image_to_string(img)
    return text