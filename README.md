# image-processing
so now I understand dilation and erosion! hooray, it’s pretty easy. See described the operations for a binary image below:

## dilation
if any one of the structuring element’s “1” pixels come into contact with any of the image’s “1” pixels, it should produce a “1” as output at the centre of the structuring element.

## erosion
only if all of the structuring element’s “1” pixels are on top of the images “1” pixels then we should produce an output at the centre of the structuring element.

### grayscale notes
take the maximum (dilation) or minimum (erosion) of the values of the image that the kernel is over, and add to it the value of the kernel at that point.
