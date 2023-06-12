#!/usr/bin/env python
from emails import find_email
import sys


def main():
    email_address = find_email(sys.argv)
    print(f'Email Address: {email_address}')


if __name__ == '__main__':
    main()
