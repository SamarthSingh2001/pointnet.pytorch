import numpy as np
import ctypes as ct
import cv2
import sys
import matplotlib as mp

parser = argparse.ArgumentParser()
parser.add_argument('--dataset', type=str, required=True, help="dataset path")

