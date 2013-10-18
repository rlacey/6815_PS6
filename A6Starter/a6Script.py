#script for running/testing assignment 6
#Starter code by Abe Davis
#
#
# Student Name:
# MIT Email:

import a6
import numpy as np
import glob
import imageIO as io
from scipy import linalg

def getPNGsInDir(path):
    fnames = glob.glob(path+"*.png")
    pngs = list()
    for f in fnames:
        #print f
        imi = io.getImage(f)
        pngs.append(imi)
    return pngs

def getRawPNGsInDir(path):
    fnames = glob.glob(path+"*.png")
    pngs = list()
    pngnames = list()
    print path
    for f in fnames:
        print f
        imi = io.imreadGrey(f)
        pngs.append(imi)
        pngnames.append(f)
    return pngs, pngnames

def testApplyHomographyPoster():
    signH = np.array([[1.12265192e+00, 1.44940136e-01, 1.70000000e+02], [8.65164180e-03, 1.19897030e+00, 9.50000000e+01],[  2.55704864e-04, 8.06420365e-04, 1.00000000e+00]])
    green = io.getImage("green.png")
    poster = io.getImage("poster.png")
    a6.applyHomography(poster, green, signH, True)
    io.imwrite(green, "HWDueAt9pm_applyHomography.png")


def testComputeAndApplyHomographyPoster():
    green = io.getImage("green.png")
    poster = io.getImage("poster.png")

    h, w = poster.shape[0]-1, poster.shape[1]-1
    pointListPoster=[np.array([0, 0, 1]), np.array([0, w, 1]), np.array([h, w, 1]), np.array([h, 0, 1])]
    pointListT=[np.array([170, 95, 1]), np.array([171, 238, 1]), np.array([233, 235, 1]), np.array([239, 94, 1])]

    listOfPairs=zip(pointListPoster, pointListT)
    
    H = a6.computeHomography(listOfPairs)
    #print H
    a6.applyHomography(poster, green, H, True)
    io.imwrite(green, "HWDueAt9pm_computeHomography.png")

########
def testComputeTransformedBBox():
    im1=io.imread('stata/stata-1.png')
    im2=io.imread('stata/stata-2.png')
    pointList1=[np.array([209, 218, 1]), np.array([425, 300, 1]), np.array([209, 337, 1]), np.array([396, 336, 1])]
    pointList2=[np.array([232, 4, 1]), np.array([465, 62, 1]), np.array([247, 125, 1]), np.array([433, 102, 1])]
    listOfPairsS=zip(pointList1, pointList2)
    HS=a6.computeHomography(listOfPairsS)
    shape = np.shape(im2)
    print a6.computeTransformedBBox(shape, HS)
    
    
def testComputeAndApplyHomographyStata():
    im1=io.imread('stata/stata-1.png')
    im2=io.imread('stata/stata-2.png')
    pointList1=[np.array([209, 218, 1]), np.array([425, 300, 1]), np.array([209, 337, 1]), np.array([396, 336, 1])]
    pointList2=[np.array([232, 4, 1]), np.array([465, 62, 1]), np.array([247, 125, 1]), np.array([433, 102, 1])]
    listOfPairsS=zip(pointList1, pointList2)
    HS=a6.computeHomography(listOfPairsS)
    #multiply by 0.2 to better show the transition
    out=im2*0.5    
    a6.applyHomography(im1, out, HS, True)
    io.imwrite(out, "stata_computeAndApplyHomography.png")

def testStitchStata():
    im1=io.imread('stata/stata-1.png')
    im2=io.imread('stata/stata-2.png')
    pointList1=[np.array([209, 218, 1]), np.array([425, 300, 1]), np.array([209, 337, 1]), np.array([396, 336, 1])]
    pointList2=[np.array([232, 4, 1]), np.array([465, 62, 1]), np.array([247, 125, 1]), np.array([433, 102, 1])]
    listOfPairs=zip(pointList1, pointList2)
    out = a6.stitch(im1, im2, listOfPairs)
    io.imwrite(out, "stata_stitch.png")

def testStitchScience():
    im1=io.imread('science/science-1.png')
    im2=io.imread('science/science-2.png')
    pointList1=[np.array([307, 15, 1], dtype=np.float64), np.array([309, 106, 1], dtype=np.float64), np.array([191, 102, 1], dtype=np.float64), np.array([189, 47, 1], dtype=np.float64)]
    pointList2=[np.array([299, 214, 1], dtype=np.float64), np.array([299, 304, 1], dtype=np.float64), np.array([182, 292, 1], dtype=np.float64), np.array([183, 236, 1], dtype=np.float64)]
    listOfPairs=zip(pointList1, pointList2)
    out = a6.stitch(im1, im2, listOfPairs)
    io.imwrite(out, "science_stitch.png")


def testCompositeStata():
    im1=io.imread('stata/stata-1.png')
    im2=io.imread('stata/stata-2.png')
    pointList1=[np.array([209, 218, 1]), np.array([425, 300, 1]), np.array([209, 337, 1]), np.array([396, 336, 1])]
    pointList2=[np.array([232, 4, 1]), np.array([465, 62, 1]), np.array([247, 125, 1]), np.array([433, 102, 1])]
    listOfPairs=zip(pointList1, pointList2)
    out = a6.stitchN([im1, im2], [listOfPairs], 0)
    io.imwrite(out, "stata_stitchN.png")

def testNPano():
    im1 = io.imread('vancouverPan/vancouver1.png')
    im2 = io.imread('vancouverPan/vancouver2.png')
    im3 = io.imread('vancouverPan/vancouver3.png')

    pointList1=[np.array([316, 21, 1], dtype=np.float64), np.array([288, 173, 1], dtype=np.float64), np.array([178, 203, 1], dtype=np.float64), np.array([156, 82, 1], dtype=np.float64)]
    pointList2=[np.array([313, 147, 1], dtype=np.float64), np.array([291, 293, 1], dtype=np.float64), np.array([172, 324, 1], dtype=np.float64), np.array([161, 198, 1], dtype=np.float64)]
    listOfPairs1=zip(pointList1, pointList2)
    pointList3=[np.array([300, 27, 1], dtype=np.float64), np.array([175, 145, 1], dtype=np.float64), np.array([160, 198, 1], dtype=np.float64), np.array([311, 171, 1], dtype=np.float64)]
    pointList4=[np.array([283, 134, 1], dtype=np.float64), np.array([165, 254, 1], dtype=np.float64), np.array([149, 311, 1], dtype=np.float64), np.array([306, 273, 1], dtype=np.float64)]
    listOfPairs2=zip(pointList3, pointList4)

    listOfListOfPairs = [listOfPairs1, listOfPairs2]
    listOfImages = [im1, im2, im3]
    refIndex = 1
    out = a6.stitchN(listOfImages, listOfListOfPairs, refIndex)
    io.imwrite(out, "vancouver_stitchN.png")    



##testApplyHomographyPoster()
##testComputeAndApplyHomographyPoster()
##testComputeTransformedBBox()
##testComputeAndApplyHomographyStata()
##testStitchStata()
##testStitchScience()
##testCompositeStata()

testNPano()
#***You can test on the first N images of a list by feeding im[:N] as the argument instead of im***

