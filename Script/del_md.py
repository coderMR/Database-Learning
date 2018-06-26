
# -*- coding= utf-8 -*-

import os
import re

def write_summary():
    lines = []
    r = open('SUMMARY.md', 'r')
    while True:
        line = r.readline()
        if len(line) == 0:
            break
        mat = re.search(r'[[].+[.]md[]]', line)
        if mat:
            line = re.sub(r'[[](.+)[.]md[]]', replace, line)
        lines.append(line)
    r.close()
    w = open('SUMMARY.md', 'w')
    for line in lines:
        w.write(line)
    w.close()

def replace(mat):
    return '[' + mat.group(1)  + ']'

def main():
    write_summary()

if __name__ == '__main__':
    main()
