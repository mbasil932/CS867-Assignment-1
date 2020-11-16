import cv2
import os
import sys
import numpy as np
import glob
import matplotlib.pyplot as plt

def rgbExclusion(img_colored,Channel):

	bgr_image = img_colored.copy()
	bgr_image[:,:,Channel] = 0 #empty blue channel
	return  bgr_image
