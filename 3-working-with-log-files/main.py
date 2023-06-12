# To do
# Generate a report.csv file to log all the 'Access Error' logs

import re
import csv

access_errors = []
fields = ['date', 'time', 'id', 'message']

with open('errors.log', 'r') as error_logs_file:
    print(*fields, sep=' || ')
    for line in error_logs_file:
        if 'Access Error' not in line:
            continue

        line_pattern = r'(^([\d:\-]+) ([\d:]+) \[ERROR-(\d+)\] - [\s\w]+: (.+)$)'
        result = re.search(line_pattern, line)
        error_data = {
            'date': result[2],
            'time': result[3],
            'id': result[4],
            'message': result[5]
        }

        access_errors.append(error_data)

# print(access_errors)

with open('access_error_report.csv', 'w', newline='') as report:
    writer = csv.DictWriter(report, fieldnames=fields)

    writer.writeheader()
    for error in access_errors:
        writer.writerow(error)
