#### Smart barrier


The project uses YOLOv7 algorithms and an OCR system to locate and read the vehicle's license plate.


## Plate detection

![Imgur Image](https://i.imgur.com/F3zGBj7.png)


* 1 - Extract truck / car from image (yolov7 MS COCO dataset)
* 2 - Extract licence plate from car image (trained web by own)
* 3 - Read text from licence plate using OCR algorithm (ex. Tesseracat)


## Project in this repository is only proof of concept at the moment. 
In the future, I will update the project with appropriate transformations of training photos, and photos of the license plate.


## List of scripts

* /colab/prepare_data.ipynb - generate augumented images and annotations
* /colab/yolov7_plate_train.ipynb - prepare and train yolov7
* /tools/images.py - operations on images
