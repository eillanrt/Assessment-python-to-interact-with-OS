#!/usr/bin/env python
import sys
from HTMLHandler import append_to_html_file
from HTMLHandler import generate_html_table


def main():
    csv_file = sys.argv[1]
    html_table = generate_html_table(csv_file)

    html_file = sys.argv[2]
    element_id = 'table'
    content = html_table

    append_to_html_file(html_file, element_id, content)


if __name__ == '__main__':
    main()
