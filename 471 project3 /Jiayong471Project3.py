from PIL import Image
import os, sys
from os import listdir
import os.path
import scipy as sp
from scipy.misc import imread
from scipy.signal.signaltools import correlate2d as c2d

def valueIt(i):
    
    data = imread(i)
    data = sp.inner(data, [299, 587, 114]) / 1000.0
    return (data - data.mean()) / data.std()

def main():
    
    checker = True
    while checker == True:
        testfile = input('Enter the file path to JPG: ')
        if os.path.exists(testfile):
            checker = False
        else:
            print("Not valid file path.")
    
    img_test = Image.open(testfile)
    img_test.thumbnail([50,50], Image.ANTIALIAS)
    img_test.save(testfile, "JPEG")
    
    
    testValue = valueIt(testfile)

    count = [0,0,0,0,0]
    for eachkind in range(1, 6): 
        for eachfile in listdir("Data/0"+str(eachkind)):
            
            img = Image.open("Data/0"+str(eachkind)+"/"+ eachfile)
            img.thumbnail([50,50], Image.ANTIALIAS)
            img.save("Data/0"+str(eachkind)+"/"+ eachfile, "JPEG")
            
            
            compareValue = valueIt("Data/0"+str(eachkind)+"/"+ eachfile)
            CompareCode = c2d(testValue, compareValue, mode='same')
            count[eachkind-1] += CompareCode.max()
            
    
    numofFile = []
    for eachkind in range(1, 6): 
         numofFile.append(len(listdir("Data/0"+str(eachkind))))            
    fianlpercentage = []
    fianlpercentage.append(count[0]/numofFile[0])
    fianlpercentage.append(count[1]/numofFile[1])
    fianlpercentage.append(count[2]/numofFile[2])
    fianlpercentage.append(count[3]/numofFile[3])
    fianlpercentage.append(count[4]/numofFile[4])
    
    
    thehighest = 0
    theindex = 0
    
    for eachindex in range(0,5):
        if fianlpercentage[eachindex] > thehighest:
            thehighest = fianlpercentage[eachindex]
            theindex = eachindex
    if theindex == 0:
        print("It is Smile")
    elif theindex == 1:
        print("It is Hat")
    elif theindex == 2:
        print("It is Hash")
    elif theindex == 3:
        print("It is Heart")
    elif theindex == 4:
        print("It is Dollar")
    
    

            
main()
            
            
            
            
            
            
            

