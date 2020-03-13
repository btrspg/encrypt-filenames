#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) Aegicare License
# @Time    : 2020/3/13 8:30 PM
# @Author  : YUELONG.CHEN
# @Mail    : yuelong.chen.btr@gmail.com
# @File    : encryptfn
# @Software: PyCharm

import argparse
from encryptfn.utils import pipeline

def main():
    parser = argparse.ArgumentParser('Encrypt filenames')
    parser.add_argument('--files', '-f', nargs='+', dest='files', required=True,
                        help='files for encrypt')
    parser.add_argument('--sep', '-s', dest='sep', default='_',
                        help='the separation of the information in the filename')
    parser.add_argument('--information-names', '-in', dest='information_names',
                        nargs='+', default=None,
                        help='names for the information in separate')
    parser.add_argument('--outdir', '-o', dest='outdir', default='./',
                        help='outdir')
    pipeline(parser.parse_args())


if __name__ == '__main__':
    main()
