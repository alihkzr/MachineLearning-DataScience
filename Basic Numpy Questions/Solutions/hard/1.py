import numpy as np
def map_pixels(mask, image_width):

    valid_pixel_counts = mask.sum(axis=0) 
    print("-----------VALID PIXEL COUNTS------------")
    print(valid_pixel_counts)
    print("--------------------------------")

    cumsum_valid = np.where(mask !=0, np.cumsum(mask, axis=0), mask)

    print("---------CUMSUM VALID---------")
    print(cumsum_valid)
    print("--------------------------------")

    scale_factors = image_width  / valid_pixel_counts

    print("-----------SCALE FACTORS-----------")
    print(scale_factors)
    print("--------------------------------")

    mapping_matrix = cumsum_valid * np.round(scale_factors, 2)

    print("-----------MAPPING MATRIX-----------")
    print(mapping_matrix)
    print("--------------------------------")

example_one = np.ones((8,5))
example_one[0:2,:]=0
example_one[-2:,:]=0

print("---------EXAMPLE ONE---------")
print(example_one)
print("--------------------------------")
map_pixels(example_one, 300)

example_two = np.zeros((8, 5))
example_two[4, :] = 1
example_two[3, 1:] = 1
example_two[2, 2:] = 1
example_two[1, 3:] = 1
example_two[0, -1] = 1

print("---------EXAMPLE TWO---------")
print(example_two)
print("--------------------------------")
map_pixels(example_two, 300)

example_three = np.zeros((9, 5))
example_three[:, 4] = 1.00
example_three[1:8, 3] = 1.00
example_three[2:7, 2] = 1.00
example_three[3:6, 1] = 1.00
example_three[4, 0] = 1.00

print("---------EXAMPLE THREE---------")
print(example_three)
print("--------------------------------")
map_pixels(example_three, 300.00)

example_four = np.zeros((9, 5))
example_four[0, -1] = 1
example_four[1, 3:] = 1
example_four[2, 2:] = 1
example_four[3, 1:4] = 1
example_four[4, :3] = 1
example_four[5, :2] = 1
example_four[6, 0] = 1

print("---------EXAMPLE FOUR---------")
print(example_four)
print("--------------------------------")
map_pixels(example_four, 90)