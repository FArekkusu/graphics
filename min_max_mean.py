from PIL import Image
from scipy import ndimage


def min_max_mean_filter(path):
    img = Image.open(path)
    for filter_type in ("minimum", "maximum", "median"):
        new_img = getattr(ndimage.filters, f"{filter_type}_filter")(img, 5)
        new_path = path.rsplit(".", 1)[0] + f"_{filter_type}_filtered.png"
        Image.fromarray(new_img).save(new_path)