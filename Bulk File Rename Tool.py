import os

name_of_path = []
directory = input('Input the path of the file: ')
format_file = input('What format will u rename the files?(WITHOUT DOTS): ')
for file in os.listdir(directory):
    if file.endswith(format_file) or file.endswith(format_file.upper()):
       name_of_path += [os.path.join(directory, file)]

template = input('What template will u use?: ')
c = 0
for i in name_of_path:
    os.rename(i, '{}\\{}{}.{}'.format(directory, template, c, format_file))
    c += 1