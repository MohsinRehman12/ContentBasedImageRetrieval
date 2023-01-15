import math
import os


def Search_Algorithm(image_name, c, test, file_name, projection, distance):

    cwd = os.getcwd() + str(chr(92)) + file_name  #get the path of the text file

    listOfProjections = []

    data = "";

    print("for image ", image_name)

    if os.path.isfile(cwd): #checks if file exists and if it does read the file into a string
        # open text file in read mode
        text_file = open(cwd, "r")

        # read whole file to a string
        data = text_file.read()
        # close file
        text_file.close()

    str_img_name = str(image_name) #cast the image_name to string for comparisons to other string

    linesList = data.splitlines(); #convert the Query string into a list

    for i in range(10): #gets the total number of times a number appears in the quey

        if i == int(c): #the c value corresponds to the searched number so we have to lower it by 1 to get the accurate average

            test.append(9)

        else: #i does not correspond to the searched numbers library so we append 10 for an accurate average

            test.append(10)

    for j in range(len(linesList)): #for loop and if statements remove all blank spaces and converts the string projections into integer list and stores it into an array

        if str_img_name in linesList[j]: #if the projections in the query corresponnds to the image being searched remove the projections from lineslist

            for k in range(7):
                linesList[j+k] = " ";

        line = linesList[j]

        if "22.5 projection" in line: #converts the line holding the 22.5 projection into an integer list
            temp = line[16:]

            temp = temp.replace('[', "")
            temp = temp.replace(']', "")

            temp = temp.split(',')

            temp = [int(i) for i in temp]
            listOfProjections.append(temp);

        if "45 projection" in line:  #converts the line holding the 45 projection into an integer list
            temp = line[16:]

            temp = temp.replace('[', "")
            temp = temp.replace(']', "")

            temp = temp.split(',')

            temp = [int(i) for i in temp]
            listOfProjections.append(temp);

        if "90 projection" in line:  #converts the line holding the 90 projection into an integer list
            temp = line[16:]

            temp = temp.replace('[', "")
            temp = temp.replace(']', "")

            temp = temp.split(',')

            temp = [int(i) for i in temp]
            listOfProjections.append(temp);

        if "180 projection" in line:  #converts the line holding the 180 projection into an integer list
            temp = line[16:]

            temp = temp.replace('[', "")
            temp = temp.replace(']', "")

            temp = temp.split(',')

            temp = [int(i) for i in temp]
            listOfProjections.append(temp);

        if "135 projection" in line:  #converts the line holding the 135 projection into an integer list
            temp = line[16:]

            temp = temp.replace('[', "")
            temp = temp.replace(']', "")

            temp = temp.split(',')

            temp = [int(i) for i in temp]
            listOfProjections.append(temp);

        if "112.5 projection" in line:  #converts the line holding the 112.5 projection into an integer list
            temp = line[17:]

            temp = temp.replace('[', "")
            temp = temp.replace(']', "")

            temp = temp.split(',')

            temp = [int(i) for i in temp]
            listOfProjections.append(temp);

    sum = 0;

    for i in range(len(listOfProjections)): #for loop and nested for loop compare the values of the image to the other 99 images in the query

        for j in range(len(listOfProjections[i])):

            k = i % 6; #allows the value to be looped and compared to all 6 projections for each image

            if (projection[k][j] != listOfProjections[i][j]): #if the value are not equal increase the value by 1
                sum += 1

            if ((k == 0) and (i != 0) and (j == 0)): #when we reach the end of a comparison for 2 images for all 6 projections set the sum to 0 to calculate the hamming distance for the next image
                distance.append(sum) #store hamming distance in the array
                sum = 0
    sum = 0
    leng = 0
    avg = []
    for i in range(10): #for loop and nested for loop get the average of the hamming distance corresponding to each handwritten number(class)

        for j in range(test[i]):

            sum += distance[j + leng - 1]
        leng += test[i]
        avg.append(sum / test[i])
        sum = 0;
    print("The image corresponds to ", avg.index(min(avg))) #print out the number the image corresponds to
    print(distance)
    check = int(c)

    if (avg.index(min(avg)) == check): #checks if image returned is correct
        return 1; #returns 1 to be incremented for the hit ratio
    else:
        return 0; #retuns 0 if the image is not correctly matched
