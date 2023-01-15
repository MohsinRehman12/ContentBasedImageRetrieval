from contentBasedImgRetrieval.projectionsAndSums import Barcode_Generator
from contentBasedImgRetrieval.comparisonClass import Search_Algorithm
from matplotlib.image import imread
from PIL import Image
import cmath
import os

#the 3 lines below get the directory path of the class
cwd = os.getcwd()
MNIST_path = os.path.join(cwd, 'MNIST_DS')
classes = os.listdir(MNIST_path)

#the 3 lines below access the Query text file and if it doesnt exist it creates it
file_name = "Query.txt"
f = open(file_name, "a")

#if the text file remove anything stored in there
f.truncate(0)

hitratio =0


for c in classes: #for loop and nested for loop get the barcodes for all the images and store them in the query text file
    images_path = os.path.join(MNIST_path, c)
    image_files = os.listdir(images_path)

    for i in image_files:
        images_path = os.path.join(images_path, i)

        image_array = imread(images_path)

        images_path = images_path.replace((images_path[images_path.index('img'):]),'') #removes the image name from file path so next image cane be used on next iteration of the for loop

        projection = [] #set projection to be an empty array

        output = Barcode_Generator(image_array,projection,i) + '\n' + '\n' + "image corresponds to " + str(c) + '\n' #calls method and stores value as a string that will be used in the query
        f.write(output) #store output into the query


f.close() #close the file

projection =[]


for d in classes: #for loop and nested for loop compare each image to the other 99 images in the Query

    images_path = os.path.join(MNIST_path, d)
    image_files = os.listdir(images_path)

    for j in image_files:
        images_path = os.path.join(images_path, j)
        image_array = imread(images_path)
        images_path = images_path.replace((images_path[images_path.index('img'):]), '') #removes the image name from file path so next image cane be used on next iteration of the for loop
        distance = []
        test = []
        Barcode_Generator(image_array, projection, j) #generate barcode for the image to be used in the Search_Algorithm

        hitratio+=Search_Algorithm(j, d, test, file_name, projection, distance) #increment the hit ratio with the output from Search Algorithm Function
        projection=[]

print("Hit-ratio/Accuracy is ", hitratio,"%") #output hit ratio after all 100 images have been tested






