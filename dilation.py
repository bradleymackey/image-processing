import cv2
import sys
# the function that can easily perform a morphological transformation
from erosion import morphologicalTransformation

def imageDilation(image):
    """performs dilation on an image and returns this"""
    # produce the dilated image by using the 'max' selection function which will use the maximum pixel value that the structuring element is currently over
    dilated_image = morphologicalTransformation(image,max)
    # return the dilated image
    return dilated_image

# read the image from the filename in greyscale
greyscale_image = cv2.imread(sys.argv[1],0)
# obtain the dilated image
dilated_image = imageDilation(greyscale_image)
# save the dilated image back to disk, with the user-specified filename
cv2.imwrite(sys.argv[2],dilated_image)
