import cv2
import sys
from erosion import imageErosion
from dilation import imageDilation

# read the image from the filename in greyscale
greyscale_image = cv2.imread(sys.argv[1],0)
# produce the eroded image
eroded_image = imageErosion(greyscale_image)
# produce the dilated (opened) image from this
opened_image = imageDilation(eroded_image)
# save the resulting file to disk
cv2.imwrite(sys.argv[2],opened_image)
