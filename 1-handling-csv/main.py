import csv

count_set = {}

with open('employees.csv', 'r') as employees_data:
    reader = csv.DictReader(employees_data)
    for row in reader:
        department = row.get('Department')
        if count_set.get(department) is None:
            count_set[department] = 0

        count_set[department] += 1

print(count_set)
print('total number of employees: {}'.format(sum(count_set.values())))

# Create report in text file

with open('report.txt', 'w') as report:
    for department in count_set:
        report.write(
            f'There are {count_set[department]} employees in {department}\n'
        )
