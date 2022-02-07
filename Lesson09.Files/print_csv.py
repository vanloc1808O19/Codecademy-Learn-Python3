import csv

with open('companies.csv', 'w') as csvfile:
    fieldnames = ['name', 'type']
    write = csv.DictWriter(csvfile, fieldnames = fieldnames)
    write.writeheader()
    write.writerow({'name': 'Van Loc Nguyen', 'type': 'Student'})
    write.writerow({'name': 'Nguyen Van Loc', 'type': 'Bachelor Student'})