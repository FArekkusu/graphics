from PIL import Image
import cv2

def laplacian(path):
    img = cv2.imread(path)
    new_img = cv2.Laplacian(img, -1)
    new_path = path.rsplit(".", 1)[0] + "_laplacian_filtered.png"
    Image.fromarray(new_img).save(new_path)

def sobel(path):
    img = cv2.imread(path)
    for i, direction in enumerate(("x", "y")):
        new_img = cv2.Sobel(img, -1, 1 - i, i)
        new_path = path.rsplit(".", 1)[0] + f"_sobel_{direction}_filtered.png"
        Image.fromarray(new_img).save(new_path)