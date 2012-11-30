#!/usr/bin/python
import fileinput


def main():
    for filename in fileinput.input():
        print filename

if __name__=="__main__":
    main()

