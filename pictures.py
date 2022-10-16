import pytesseract
from PIL import Image

img = Image.open('img.jpg')

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
text = pytesseract.image_to_string(img, lang='en')


print(text)

with open('file.txt', 'a') as f:
    f.write(text)



# import EasyOCR


# def text_recognition(file_puth):
#     reader = EasyOCR.easyocr.Reader(['ru'])
#     result = reader.readtext(file_puth)
#     return result

# def main():
#     file_puth = 'Prideandprejudiceposter.jpg'
#     text_recognition(file_puth)
    
    
    
# if __name__ == '__main__':
#     main()