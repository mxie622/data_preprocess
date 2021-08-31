import os
import argparse
from process_image import process, process_resize

def main(config):
    # settings = {
    # "img2resize": {"ypixels": 256,
    #                "xpixels": 256},
    #             }
    
    settings = {
    "img2resize": {"ypixels": config.image_dim_y,
                   "xpixels": config.image_dim_x},
                }
    images = os.listdir(os.getcwd() + '/input') # images list of current path
    print(images)
    for i in images:
        process_resize(settings=settings,
                    imgFile= os.path.join(os.getcwd() + '/input/' + i),
                    outDir=os.path.join(os.getcwd(), "output")
                    )

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Model configuration.
    parser.add_argument('--image_dim_x', type=int, default=256, help='dimension x of images')
    parser.add_argument('--image_dim_y', type=int, default=256, help='dimension y of images')

    config = parser.parse_args()
    print(config)
    main(config)