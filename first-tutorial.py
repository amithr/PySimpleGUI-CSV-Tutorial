import csv

header = ['Name', 'Phone Number', 'Address', 'Age']
row = ['John', '372-293-423', '23 Joy Rd', 25]

pelmeni_file = open('pelmeni.csv', 'w')
writer = csv.writer(pelmeni_file)
writer.writerow(header)
writer.writerow(row)
pelmeni_file.close()