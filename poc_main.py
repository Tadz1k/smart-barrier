import torch
import pathlib 
import cv2
import pandas as pd

#own imports
import tools.images
import tools.ocr

plate = ['P', 'R', '3', '5', '1']
gamma_adjustments = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.8,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,2.1,2.2,2.3,2.4,2.5]

model = torch.hub.load('yolov7', 'custom', 'models\\plate_detection.pt', source='local')
image = cv2.imread('images\\car.jpg')
data = model(image)

plate = tools.images.extract_plate_from_image(data, image)
#cv2.imshow('plate', plate)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#plate_text = tools.ocr.get_plate(plate)
#print(plate_text)
for gamma_ratio in gamma_adjustments:
    for psm in range(1, 13):
        try:
            img2 = tools.images.adjust_gamma(image, gamma_ratio)
            plate_text = tools.ocr.get_plate(img2, psm)
            print(f'gamma = {gamma_ratio}   psm = {psm}     plate_text = {plate_text}')
        except:
            print(f'PSM : {psm} - skip')