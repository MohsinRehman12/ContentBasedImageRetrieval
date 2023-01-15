import math
import os
from matplotlib.image import imread

import numpy as np



def ninty_proj(nintydegree, numzero):  #method that gets the sum of the 90 degree projection and stores the value in a new list

    # get 90 degree projection
    for x in range(len(numzero)): #for loop and nested for loop go down each column and get the sum and append it into a new list
        sum = 0
        for k in range(len(numzero)):
            sum += numzero[x][k]

        nintydegree.append(sum)
    convert_to_projection(nintydegree)


def oneeighty_proj(oneeightydegree, numzero): #method that gets the sum of the 180 degree projection and stores the value in a new list
    # get 180 degree projection

    for x in range(len(numzero)): #for loop and nested for loop go across each row and get the sum and append it into a new list
        sum = 0;
        for k in range(len(numzero)):
            sum += numzero[k][x]

        oneeightydegree.append(sum)
    convert_to_projection(oneeightydegree)

def diagonal_sum_otf(numzero, otfsum): #method that gets the sum of the 135 degree diagonal and stores the value in a new list

    length = math.floor(len(numzero) / 2) #gets the number of half the length of the NxN matrix and floors just in case its odd

    for x in range(length, (len(numzero)) * 2 - (length) - 1): #for loops and nested for loops get the sum of the 135 degree projection
        sum = 0;
        for k in range(0, x + 1):
            i = x - k
            if (i < len(numzero) and k < len(numzero)):
                sum += numzero[i][k]
        otfsum.append(sum);


def diagonal_sum_ff(numzero, ffsum): #method that gets the sum of the 45 degree diagonal and stores the value in a new list

    length = math.floor(len(numzero) / 2) #gets the number of half the length of the NxN matrix and floors just in case its odd

    for j in range(length): #for loop and nested for loops get the sum of diagonals in the upper triangle of the array at a 45 degree angle (from left to right) until length
        sum = 0 #set sum when each instance runs
        for x in range(0, (len(numzero) - j)):
            for k in range(0, (len(numzero) - j)):
                if ((x) == k):
                    sum += numzero[x + j][k] #adds the sum of values in the indexes across the diagonal

        ffsum.append(sum) #append the sum of the diagonal into a list

    ffsum.reverse() #reverse the array so the longest diagonal appears in the middle

    for j in range(1, length): #for loop that gets the sum of the upper triangle of the array at a 45 degree angle
        sum = 0
        for x in range(((len(numzero) + 1) - j)): #for loop stats at last index of x to get the lower diagonal
            for k in range((len(numzero) - j)):
                if ((x) == k):
                    sum += numzero[k][x + j] #adds the sum of values in the indexes across the diagonal
        ffsum.append(sum)  #append the sum of the diagonal into a list





def diagonal_sum_ttpf(numzero, ttpfsum):  #method that gets the sum of the 22.5 degree diagonal and stores the value in a new list

    length = math.floor(len(numzero) / 2) #gets the number of half the length of the NxN matrix and floors just in case its odd

    for j in range(0, length):  #for loop and nested for loops get the sum of diagonals in the upper triangle of the array at a 22.5 degree angle (from left to right) until length
        sum = 0
        y =0;
        for x in range(len(numzero)):
            if (x+j) < len(numzero) and y < len(numzero): #checks if the index is valid and inrange
                sum += numzero[x+j][y] #adds the sum of values in the indexes across the diagonal
            y+=2 #increment y to be 0 so it go across the row across a 22.5 degree angle
        ttpfsum.append(sum) #append the sum of the diagonal into a list

    for j in range(1, length): #for loop that gets the sum of the upper triangle of the array at a 22.5 degree angle
        sum = 0
        y =0;
        for x in range(len(numzero)):
            if (y+j) < len(numzero):#checks if the index is valid and inrange
                sum += numzero[x][y+j] #adds the sum of values in the indexes across the diagonal
            y+=2 #increment y by 2 so it go across the row across a 22.5 degree angle

        ttpfsum.append(sum) #append the sum of the diagonal into a list
ttpfsum = []
ffsum =[]

def diagonal_sum_otpf(numzero, otpfsum):  #method that gets the sum of the 112.5 degree diagonal and stores the value in a new list

    length = math.floor(len(numzero) / 2) #gets the number of half the length of the NxN matrix and floors just in case its odd

    for j in range(0, length): #for loop and nested for loops get the sum of diagonals in the upper triangle of the array at a 112.5 degree angle (from left to right) until length
        sum = 0
        y =len(numzero)-1
        for x in range(len(numzero)):
            if (y-j) < len(numzero) and (y > 0): #checks if the index is valid and inrange
                sum += numzero[x+j][y] #adds the sum of values in the indexes across the diagonal
            y-=2 #decrement y by 2 so it go across the row across a 112.5 degree angle
        otpfsum.append(sum) #append the sum of the diagonal into a list

    for j in range(1, length): #for loop that gets the sum of the upper triangle of the array at a 112.5 degree angle
        sum = 0
        y =len(numzero)-1
        for x in range(len(numzero)):
            if (x+j) < len(numzero) and (y > 0): #checks if the index is valid and inrange
                sum += numzero[x][y-j] #adds the sum of values in the indexes across the diagonal
            y-=2 #append the sum of the diagonal into a list
        otpfsum.append(sum) #append the sum of the diagonal into a list

def convert_to_projection(sumarray): #method that takes a list and converts it into a projection

    avg = 0

    for x in range(len(sumarray)): #for loop calculates the average of the array and stores it into a variable

        avg+=sumarray[x]

    avg = avg/(len(sumarray))

    for x in range(len(sumarray)): #for loop changes the values of list at index x to 0 if its below the average and 1 every else to get the projection

        if (sumarray[x] >= avg):
            sumarray[x] = 1

        else:
            sumarray[x]= 0


def otf_projection(numzero, otf): #method that calls 2 methods to obtain the 135 degree projection
    diagonal_sum_otf(numzero, otf);
    convert_to_projection(otf)


def ff_projection(numzero, ff):  #method that calls 2 methods to obtain the 45 degree projection
    diagonal_sum_ff(numzero, ff);
    convert_to_projection(ff)

def otpf_projection(numzero, otpf):  #method that calls 2 methods to obtain the 112.5 degree projection
    diagonal_sum_otpf(numzero, otpf);
    convert_to_projection(otpf)

def ttpf_projection(numzero, ttpf):  #method that calls 2 methods to obtain the 22.5 degree projection
    diagonal_sum_ttpf(numzero, ttpf);
    convert_to_projection(ttpf)


def Barcode_Generator(numzero, projection, name): #one of the main algorithms that generates the barcodes/projections and prints them out

    temp = [] #empty list temp that will temporarily store the barcodes generated for each angle to be appeneded into another list

    ttpf_projection(numzero, temp) #calls function to get the 22.5 projections
    projection.append(temp) #append projection into the projection list

    temp = [] #set temp to be empty again so it can store the value of the next barcode

    ff_projection(numzero, temp) #calls function to get the 45 projections
    projection.append(temp) #append projection into the projection list

    temp = [] #set temp to be empty again so it can store the value of the next barcode

    ninty_proj(temp, numzero) #calls function to get the 90 projections
    projection.append(temp) #append projection into the projection list
    temp = [] #set temp to be empty again so it can store the value of the next barcode

    otpf_projection(numzero, temp)  #calls function to get the 112.5 projections
    projection.append(temp) #append projection into the projection list
    temp = [] #set temp to be empty again so it can store the value of the next barcode

    otf_projection(numzero, temp) #calls function to get the 90 projections
    projection.append(temp) #append projection into the projection list
    temp = [] #set temp to be empty again so it can store the value of the next barcode

    oneeighty_proj(temp, numzero) #calls function to get the 180 projections
    projection.append(temp) #append projection into the projection list
    temp = [] #set temp to be empty again so it can store the value of the next barcode

    s =""


    s += "Projections for " + name + '\n' + "22.5 projection: "+ str(projection[0])+ '\n'+"45 projection: "+ str(projection[1])+ '\n'+ "90 projection: "+ str(projection[2])+ '\n'+ "112.5 projection: "+ str(projection[3])+ '\n'+ "135 projection: "+ str(projection[4])+ '\n'+  "180 projection: "+ str(projection[5])

    return s;  #retruns the string output that will be stored in the query


