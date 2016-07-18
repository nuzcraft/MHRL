
# get_center takes a length and width of a rectangle and returns the center tile
# only works on odd by odd things, if even, it will skew down for width and right for length
def get_center(length, width):
    x_center = round(length / 2)
    y_center = round(width / 2)
    return (int(x_center), int(y_center))
