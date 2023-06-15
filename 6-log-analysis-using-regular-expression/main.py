#!/usr/bin/env python
import re
import operator
import csv


def get_log_data(file=""):
    error_count = {}
    user_statistics = {}

    with open(file, 'r') as f:
        logs = [line.strip() for line in f.readlines()]
        log_pattern = r"(ERROR|INFO): ([\w ']+) (\[[#\d]+\])? ?\(([\w\d]+)\)$"

        for log in logs:
            result = re.search(log_pattern, log)
            type_of_log = result[1]
            log_message = result[2]
            user = result[4]

            if user_statistics.get(user) is None:
                user_statistics[user] = {'Info': 0, 'Error': 0}

            user_statistics[user][type_of_log.capitalize()] += 1

            if type_of_log == 'ERROR':
                if error_count.get(log_message) is None:
                    error_count[log_message] = 0

                error_count[log_message] += 1

    return (dict(sorted(error_count.items(), key=operator.itemgetter(1), reverse=True)), user_statistics)


def main():
    log_errors, user_statistics = get_log_data('syslog.log')

    print(log_errors)
    print('\n')
    print(user_statistics)

    with open('log_errors.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Errors', 'Count'])
        writer.writeheader()

        for error in log_errors:
            writer.writerow({'Errors': error, 'Count': log_errors[error]})

    with open('user_statistics.csv', 'w', newline='') as f2:
        writer = csv.DictWriter(f2, fieldnames=['Username', 'INFO', 'ERROR'])
        writer.writeheader()

        for user in user_statistics:
            data = user_statistics[user]
            writer.writerow(
                {'Username': user, 'INFO': data['Info'], 'ERROR': data['Error']})


if __name__ == '__main__':
    main()
