
# -*- coding=utf-8 -*-

import os
import re

def main():
    dir_path = input('请输入文件名称:')
    files = os.listdir(dir_path)
    for file_t in files:
        if file_t.endswith('.md'):
            lines = []
            r = open(dir_path + '/' + file_t, 'r')
            while True:
                line = r.readline()
                if len(line) == 0:
                    break
                if line == '--\n':
                    line = '---'
                lines.append(line)
            r.close()
            w = open(dir_path + '/' + file_t, 'w')
            for line in lines:
                w.write(line)
            w.close()

if __name__ == '__main__':
    main()
