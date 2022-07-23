import os
dirname = os.path.dirname(__file__)
print(dirname)
relative_path_to_file = '../data/preprocessed_files/rbi/crop_turnout.txt'
outfile_path = '../data/preprocessed_files/rbi/crop_data_pairs.csv'
fullpath_to_datafile = os.path.join(dirname, relative_path_to_file)
fullpath_to_outfile = os.path.join(dirname, outfile_path)
print('filename is:')
print(fullpath_to_datafile)
import csv
def read_data_from_file(f):
    print('in read data function')
    file = open(f,'r')
    print('opened file')
    lines = file.readlines()
    lines= [l.replace('\n','').replace(',','').replace('\'','').replace(' ','') for l in lines]
    lines = [l.split('\t') for l in lines]
    file.close()
    return lines
print('about to call read data function')
all_data = read_data_from_file(fullpath_to_datafile)
headers = all_data[0]
data = all_data[1:]

# The dataset includes pulses and total food grains too, but here I am presenting calculations only until total cereals
# If we want to include pulses also, the choices provided in single_parameter_regression,
#       along with using the correct indices would change
def prepare_data_rows(vals):
    data_set = []
    index_range_start = 1
    index_range_stop = 5
    for v in vals:
        row = v[index_range_start:index_range_stop]
        data_set.append(row)
    return data_set

print(headers)
print(data[1])


data_pairs = prepare_data_rows(data)
for p in data_pairs:
    print(p)

with open(fullpath_to_outfile,'w') as file:
    writer = csv.writer(file)
    writer.writerows(data_pairs)

