import csv

with open('security_incidents.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    list = list(reader)

list[0].append('Status')


for status in range(1,len(list)):
    list[status].append('pending')

with open('security_incidents_modified.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(list)