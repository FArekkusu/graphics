from gray_level import gray_level_transformation
from min_max_median import min_max_median_filter
from laplacian_sobel import laplacian, sobel


if __name__ == "__main__":
    path = "images/profile.png"

    gray_level_transformation(path, 0, 100)
    gray_level_transformation(path, 155, 255)

    min_max_median_filter(path)
    min_max_median_filter(path, size=3)

    laplacian(path)
    laplacian(path, ksize=3)
    laplacian(path, ksize=5)

    sobel(path)
    sobel(path, ksize=5)