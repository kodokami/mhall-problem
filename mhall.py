#!/usr/bin/env python3
"""
Script for executing statistics experiments for the Monty Hall Problem

Copyright (C) 2026 _kodokami <kodokami@protonmail.com>
"""
from argparse import ArgumentParser, RawTextHelpFormatter

__version__ = '0.1.0'

COMMON_ERROR_CODE = 1
SIGINT_ERROR_CODE = 2


def cmdmaker():
    """ Argparse function """
    parser = ArgumentParser(
        prog='mhall',
        description='Script for executing statistics experiments for the Monty Hall Problem',
        epilog='Copyright (C) 2026 _kodokami',
        add_help=False,
        formatter_class=RawTextHelpFormatter
    )

    other = parser.add_argument_group('other')
    other.add_argument('-V', '--version', action='version', version=f'v{__version__}')
    other.add_argument('-h', '--help', action='help', help='print this help message and exit')

    # return parser
    return parser.parse_args()


if __name__ == '__main__':
    try:
        args = cmdmaker()
        print(args)

    except KeyboardInterrupt:
        exit(SIGINT_ERROR_CODE)
