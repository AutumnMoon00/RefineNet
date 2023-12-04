import laspy

## Clipping 
laz_file_path = "D:\\Geomatics\\thesis\\RefineNet\\data\\AHN\\C_37EN2.LAZ"
clip_folder_path = "D:\\Geomatics\\thesis\\RefineNet\\data\\AHN\\clipped"  # clipped laz files will come here
with laspy.open(laz_file_path) as f:
    x_min, x_max, y_min, y_max, = f.header.x_min, f.header.x_max, f.header.y_min, f.header.y_max


top, left = y_max, x_min
bottom, right = y_max - (y_max-y_min)/8, x_min + (x_max-x_min)/8

clipping = True


## Neighbourhood search
search_radius = 0.5  # 0.5 meters
bin_count_nn = 40  # making bins, giving all the points for neighbourhood search is crashing the notebook
nn_threshold = 5  ## threshold for ambiguity, not enough number of neighbours to compare