from netCDF4 import Dataset
import numpy as np
from functions import *

# radius of the earth in meters
R = 6371000
#ISDEMIR, 36.77118198728893, 36.21960356869678
user_lon = float(36.77118198728893)
user_lat = float(36.21960356869678)

# path to netCDF data
path = r'/Users/erdoganb/Desktop/erdo-dev/python/gis/s5p_read/no2 files/S5P_NRTI_L2__NO2____20221003T110408_20221003T110908_25765_03_020400_20221003T115001.nc'
dir_path = r'/Users/erdoganb/Desktop/erdo-dev/python/gis/s5p_read/no2 files'

#path divided
path_suffix = "/Users/erdoganb/Desktop/erdo-dev/python/gis/s5p_read/no2 files/"
# read dataset function
def read_dataset(file_path):  # file = path to file
    # read as Dataset
    file = Dataset(file_path, 'r')
    #reading dataset
    print("read_dataset ok!")
    # Saving the data to lat, long, and no2_data variables
    lat = file.groups['PRODUCT'].variables['latitude'][0, :, :]
    lon = file.groups['PRODUCT'].variables['longitude'][0, :, :]
    no2_data = file.groups['PRODUCT'].variables['nitrogendioxide_tropospheric_column'][0, :, :]
    #call nearest!
    nearest=find_nearest(user_lat, lat, lon)
    return no2_data.ravel()[nearest]

# necessary for find_nearest (Haversine formula)
# calculation to find nearest point in data to entered location (haversine formula)
def find_nearest(user_input_lat, lat, lon):
    user_lat = user_input_lat
    lat1 = np.radians(user_lat)
    lat2 = np.radians(lat)
    delta_lat = np.radians(lat-user_lat)
    delta_lon = np.radians(lon-user_lon)
    a = (np.sin(delta_lat/2))*(np.sin(delta_lat/2))+(np.cos(lat1)) * \
        (np.cos(lat2))*(np.sin(delta_lon/2))*(np.sin(delta_lon/2))
    c = 2*np.arctan2(np.sqrt(a), np.sqrt(1-a))
    d = R*c
    print("NEAREST!!")
    return ((d.argmin()))


#lat-lon values of nearest tile

#ravel needed!
#no2_val = str(no2_data.ravel()[nearest])


# write to file
for file_name in get_file_name(dir_path):
    # added dated for related pixel
    full_path = (path_suffix+file_name)
    
    year = parse_path(full_path)[0]
    month = parse_path(full_path)[1]
    day = parse_path(full_path)[2]
    
    no2_val = read_dataset(full_path)
    write_to_file(year, month, day, no2_val)
