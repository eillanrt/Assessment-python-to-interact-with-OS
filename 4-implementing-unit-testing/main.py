#!/usr/bin/env python
from emails import find_email
import sys
import re


def is_email_address(string):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, string) is not None


def main():
    email_address = find_email(sys.argv)

    print(f'Email address: {email_address}' if is_email_address(
        email_address) else email_address)


if __name__ == '__main__':
    main()
