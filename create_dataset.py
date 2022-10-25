import os
import shutil

new_file = open('gt.txt', 'a')

for dir in os.listdir('letters'):
    current_letter = dir
    for image in os.listdir(f'letters\\{dir}'):
        print(image)
        new_file.write(f'test/{image}\t{dir}\n')
        shutil.copyfile(f'letters\\{dir}\\{image}', f'data\\test\\{image}')