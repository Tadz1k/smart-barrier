import cv2
import numpy as np

def extract_plate_from_image(results, frame):
    xmin = results.pandas().xyxy[0]['xmin']
    xmax = results.pandas().xyxy[0]['xmax']
    ymin = results.pandas().xyxy[0]['ymin']
    ymax = results.pandas().xyxy[0]['ymax']
    image = None
    if len(xmin) > 0 and len(xmax) > 0 and len(ymin) > 0 and len(ymax) > 0:
        image = frame[ymin[0].astype(np.int):ymax[0].astype(np.int), xmin[0].astype(np.int):xmax[0].astype(np.int)]
        height, width, channels = image.shape
        height = height * 2
        width = width * 2
        image = cv2.resize(image, (width, height))
        #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #image = adjust_gamma(image, 2)
        image = np.asarray(image)
        return image
    return image

def adjust_gamma(image, gamma=1.0):
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
	return cv2.LUT(image, table)

def to_gray(image):
    image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image2