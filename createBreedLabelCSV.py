import csv
import os
import glob

filePath  = '/content/drive/MyDrive/CNN/labels_full.csv'
imagePath = '/content/drive/MyDrive/CNN/Images/*/*'
breedPath = '/content/drive/MyDrive/CNN/Images/*'

with open(filePath, 'w', newline='') as f:
  write = csv.writer(f)
  write.writerow(['id','breed'])

  images_list = glob.glob()
  breeds_list = glob.glob()
  for data in images_list:
    data = data.split('/')
    breed = data[6].split('-')[1]
    image_path = data[7].split('.')[0]
    write.writerow([image_path, breed])
    #print(breed + " " + image_path)
