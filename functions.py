# Import the netCDF data
#path = "files/S5P_NRTI_L2__NO2____20220930T101908_20220930T102408_25722_03_020400_20220930T105625.nc"

import os

def get_file_name(dir_path):
    file_array = []
    files = (os.listdir(dir_path))
    return files

# parse function for file-name
def parse_path(path):
    year = path[83:87]
    month = path[87:89]
    day = path[89:91]
    return year, month, day

# write to file func


def write_to_file(year, month, day, value):
    f = open(r'~/s5p-prj/files/isdemir.txt', 'a+')
    line = ["{} {} {} {}".format(year, month, day, value)]
    f.writelines(line)
    f.write("\n")
    f.close()
