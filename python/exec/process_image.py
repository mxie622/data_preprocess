"""

 process_image.py (author: Anson Wong / git: ankonzoid)

 Process your image using any of the following techniques:

  1) Force resizing (ypixels, xpixels) -> (ypixels_force, xpixels_force)

  2) Grey scaling (3 rgb channels -> 1 greyscale channel)

  3) K-means color quantization (using cluster colors or user-defined colors)

  4) Edge detection (gaussian blue, then sobel edge detection)

"""
import os

import skimage.io
from skimage.transform import resize

def img2resize(imgFile, outFile, ypixels_resize, xpixels_resize):
    img = skimage.io.imread(imgFile, as_gray=False)
    img_resized = resize(img, (ypixels_resize, xpixels_resize), anti_aliasing=True)
    skimage.io.imsave(outFile, img_resized)

def process_image(settings, imgFile, outDir):

    # Create output directory
    if not os.path.exists(outDir):
        os.mkdir(outDir)

    # Get file name without extension
    nametag = os.path.splitext(os.path.basename(imgFile))[0]

    # Process image
    print("Processing {} to {}...".format(imgFile, outDir))

    if "img2resize" in settings.keys():
        print("Resizing image...")
        img2resize(imgFile, os.path.join(outDir, nametag + "_resized.jpg"),
                   ypixels_resize=settings["img2resize"]["ypixels"],
                   xpixels_resize=settings["img2resize"]["xpixels"])


settings = {
    "img2resize": {"ypixels": 256,
                   "xpixels": 256},
}

images = os.listdir(os.getcwd() + '/input') # images list of current path
print(images)
for i in images:
 
# Run our tools
    process_image(settings=settings,
                  imgFile= os.path.join(os.getcwd() + '/input/' + i),
                  outDir=os.path.join(os.getcwd(), "output"))
# process_image(settings=settings,
#               imgFile=os.path.join(os.getcwd(), ,"burger_test.jpeg"),
#               outDir=os.path.join(os.getcwd(), "output"))
# process_image(settings=settings,
#               imgFile=os.path.join(os.getcwd(), "input", "squirrel.jpeg"),
#               outDir=os.path.join(os.getcwd(), "output"))
