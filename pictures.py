import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"

def image_open(img_name):
    try:
        if img_name[-4:] == '.jpg' or img_name[-4:] == '.png':
            return Image.open(img_name)
        else:
            print('Image not found')
            return 
    except FileNotFoundError(err):
        return err


def image_to_str(img):
    return pytesseract.image_to_string(img, lang='rus+eng')

def write_file(fname, text):
    if fname[-4:] != '.txt':
        print('Write a correct filename')
        return 
    with open(fname, 'w') as f:
        f.write(str(text.strip()))
        return f
    return

def main():
    img_name = 'img1.jpg'
    fname = 'file.txt'
        
    img = image_open(img_name)
    text = image_to_str(img)

    write_file(fname, text)
    return text.strip()
# print(main())    

if __name__ == '__main__':
    main()    
    
    
    
    
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