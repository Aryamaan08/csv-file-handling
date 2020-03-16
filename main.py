import csv

if input('New document or open? ') == 'o':
    with open(input('File name: ') + '.csv') as filename:
        items = csv.reader(filename)
        print('Name\t\t   Age')
        for item in items:
            print('\t\t'.join(item))
else:
    open(input('File name: '), 'w+')
