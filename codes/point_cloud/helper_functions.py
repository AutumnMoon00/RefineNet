def generate_bins(number, bin_count):
    # number += 1
    if bin_count <= 0:
        raise ValueError("Number of bins should be greater than 0.")

    bin_size = number / bin_count

    bins = []
    start = 0

    for _ in range(bin_count):
        end = start + bin_size
        bins.append([int(round(start)), int(round(end))])
        start = end

    return bins


# this function is for calculating number of neighbours with same classification and giving confidence
def fraction_of_trues(bool_list):
    ## no neighbours within the radius
    if len(bool_list) == 0:
        return -1.0  # Return 0 if the list is empty

    true_count = sum(bool_list)
    fraction_true = true_count / len(bool_list)
    return fraction_true



def recursive_split(x_min, y_min, x_max, y_max, max_x_size, max_y_size):
    x_size = x_max - x_min
    y_size = y_max - y_min

    if x_size > max_x_size:
        left = recursive_split(
            x_min, y_min, x_min + (x_size // 2), y_max, max_x_size, max_y_size
        )
        right = recursive_split(
            x_min + (x_size // 2), y_min, x_max, y_max, max_x_size, max_y_size
        )
        return left + right
    elif y_size > max_y_size:
        up = recursive_split(
            x_min, y_min, x_max, y_min + (y_size // 2), max_x_size, max_y_size
        )
        down = recursive_split(
            x_min, y_min + (y_size // 2), x_max, y_max, max_x_size, max_y_size
        )
        return up + down
    else:
        return [(x_min, y_min, x_max, y_max)]

