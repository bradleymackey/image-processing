import cv2
import sys
# import needed functions from the needed files
from dilation import imageDilation
from erosion import imageErosion

# read the image from the filename in greyscale
greyscale_image = cv2.imread(sys.argv[1],0)
# produce the dilated image
dilated_image = imageDilation(greyscale_image)
# produce the eroded (closed) image from this
closed_image = imageErosion(dilated_image)
# save the resulting file to disk
cv2.imwrite(sys.argv[2],closed_image)
