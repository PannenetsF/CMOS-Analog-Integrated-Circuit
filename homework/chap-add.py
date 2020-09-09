#! python
# -*- coding: UTF-8 -*-

import sys, getopt, os

def main(argv):
    fname = ''
    try:
        opts, args = getopt.getopt(argv,"hn:",["chapname="])
    except getopt.GetoptError:
        print('chap-add.py -n <chapter-name>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('chap-add.py -n <chapter-name>')
            sys.exit()
        elif opt in ("-n", "--chapname"):
            fname = arg
    f = open('elegant-chap.tex', 'r')
    flines = f.readlines()
    f.close()

    l = len(flines)
    for i in range(l):
        flines[i] = flines[i].replace('chap-name-flag', fname)

    f = open('./homework.%s.tex'%fname, 'w')
    f.writelines(flines)
    f.close() 
    print('homework.%s.tex created'%fname)

if __name__ == "__main__":
    main(sys.argv[1:])

