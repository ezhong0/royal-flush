# You will need to update this when you get cards to measure
# Dimensions of card
cardW = 57
cardH = 87
# Dimensions of corner containing number and suit
cornerXmin=2
cornerXmax=10.5
cornerYmin=2.5
cornerYmax=23

#convert from mm to pixels
zoom=4
cardW*=zoom
cardH*=zoom
cornerXmin=int(cornerXmin*zoom)
cornerXmax=int(cornerXmax*zoom)
cornerYmin=int(cornerYmin*zoom)
cornerYmax=int(cornerYmax*zoom)

import numpy as np
import cv2
import os
from tqdm import tqdm
import random
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches
import pickle
from glob import glob 
import imgaug as ia
from imgaug import augmenters as iaa
from shapely.geometry import Polygon