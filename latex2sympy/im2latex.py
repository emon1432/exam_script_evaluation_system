import pytesseract
from PIL import Image



def image_to_text(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

if __name__ == "__main__":
    image_path = "latex_image.png"
    extracted_text = image_to_text(image_path)
    print(extracted_text)