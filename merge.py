import glob

with open('исходные данные/MOCK_DATA.csv', 'r') as first_file:
    header = first_file.readline()

with open('mock_data_raw.csv', 'w') as outfile:
    outfile.write(header)

    for filename in glob.glob('исходные данные/*.csv'):
        with open(filename, 'r') as infile:
            next(infile)
            outfile.write(infile.read())