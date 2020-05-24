from PIL import Image
from pylab import array
import numpy as np


def clamp(arr, min_, max_):
    return np.asarray(arr / 255 * (max_ - min_) + min_).astype(np.uint8)


def gray_level_transformation(path):
    img = Image.open(path)
    clamped = clamp(array(img), 0, 100)
    new_path = path.rsplit(".", 1)[0] + "_gray_level_transformed.png"
    Image.fromarray(clamped).save(new_path)