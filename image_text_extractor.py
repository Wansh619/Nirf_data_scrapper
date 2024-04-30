# C:\Program Files\Tesseract-OCR\tesseract


import pytesseract
from PIL import Image
import cv2
import numpy as np
import re
# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
def find_numbers(string):
    pattern = r'[-+]?\d*\.?\d+'
    numbers = re.findall(pattern, string)
    return numbers
# Open an image file
def text_extractor(path):
    # image_path = 'image.png'
    img = Image.open(path)
    img = img.convert('L')
    img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    # print(img_cv.shape)
    resized_img = cv2.resize(img_cv, (1920,1080))
    
    extracted_text = pytesseract.image_to_string(resized_img)
    text_list= extracted_text.split('\n')
    score=""
    for i in text_list:
        #print(i)
        if "Score" in i or 'score' in i:
            score=i
            break
    numbers=find_numbers(score)
    output={
    "SS":numbers[0],
    "FSR":numbers[1],
    "FQE":numbers[2],
    "FRU":numbers[3],
    "PU":numbers[4],
    "QP":numbers[5],
    "IPR":numbers[6],
    "FPPP":numbers[7],
    "GPH":numbers[8],
    "GUE":numbers[9],
    "MS":numbers[10],
    "GPHD":numbers[11],
    "RD":numbers[12],
    "WD":numbers[13],
    "ESCS":numbers[14],
    "PCS":numbers[15],
    # "PR":numbers[16]
    }
    return output
if __name__ =='__main__':
    out=text_extractor('output\Chitkara--UniversityMore-DetailsClose-\parm_image\parms.png')
    print(out)
        


