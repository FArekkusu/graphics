from gray_level import gray_level_transformation
from min_max_mean import min_max_mean_filter
from laplacian_sobel import laplacian, sobel


if __name__ == "__main__":
    functions = [
        gray_level_transformation,
        min_max_median_filter,
        laplacian,
        sobel
    ]

    for f in functions:
        f("images/profile.png")
