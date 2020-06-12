#!/usr/bin/env python3
# -*-coding:utf-8-*-


import os, os.path, sys


def get_files_name(path, suffix, old, new):
    for parent, dir_name, file_name in os.walk(path, topdown=True, followlinks=False, onerror=None):
        for name in file_name:
            if name.endswith(suffix):
                rename(name, old, new)


def get_path():
    return os.path.abspath('.')


def rename(name, old, new):
    new_name = name.replace(old, new)
    # print(name, '===', name)
    os.rename(name, new_name)


if __name__ == '__main__':
    len = len(sys.argv)
    if len != 5:
        print('Usage: python3 change_names.py path suffix old new')
        print('Usage: python3 change_names.py 所在路径 文件后缀名 文件名中需要去掉的部分 去掉后需要填充的内容')
        exit(0)
    print(sys.argv)
    
    get_files_name(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
