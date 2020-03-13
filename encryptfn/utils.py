#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) Aegicare License
# @Time    : 2020/3/13 8:29 PM
# @Author  : YUELONG.CHEN
# @Mail    : yuelong.chen.btr@gmail.com
# @File    : utils
# @Software: PyCharm

import pandas as pd
import hashlib
import os


def encrypt(name):
    '''

    :param name:
    :return:
    '''
    return hashlib.sha256(name.encode('utf8')).hexdigest()


def get_info(fn, sep):
    '''

    :param fn:
    :param sep:
    :return:
    '''
    name, suffix = fn.split('.', 1)
    return name.split(sep), suffix, encrypt(name)


def copy_cmd(fn, new_fn):
    '''

    :param fn:
    :param new_fn:
    :return:
    '''
    return 'cp {fn} {new_fn}'.format(**locals())


def pipeline(args):
    df = {}
    os.makedirs(args.outdir, mode=0o755, exist_ok=True)
    cmds = list()

    for fn in args.files:
        infos, suffix, encrypt_name = get_info(fn, args.sep)
        if args.information_names is not None and len(args.information_names) != len(infos):
            raise ValueError('information names must equal to the information separate')
        if args.information_names is not None:
            for i in range(len(infos)):
                df.setdefault(args.information_names[i], [])
                df[args.information_names[i]].append(infos[i])
        else:
            for i in range(len(infos)):
                df.setdefault('V' + str(i), [])
                df['V' + str(i)].append(infos[i])
        df.setdefault('encrypt_file', [])
        df['encrypt_file'].append('{encrypt_name}.{suffix}'.format(encrypt_name=encrypt_name,
                                                                   suffix=suffix))
        cmds.append(copy_cmd(fn, '{outdir}/{encrypt_name}.{suffix}'.format(outdir=args.outdir,
                                                                           encrypt_name=encrypt_name,
                                                                           suffix=suffix)))
    pd.DataFrame(df).to_csv('{outdir}/information.csv'.format(outdir=args.outdir))
    with open('{outdir}/cp.bash'.format(outdir=args.outdir), 'w') as f:
        f.write('#! /bin/bash\n')
        f.write('\n'.join(cmds))
