#!/usr/bin/env python

#from PyQt4 import QtGui, QtCore
import sys

class Country():
    def __init__(self,name):
        self.name = name
        

    def __str__(self):
        return ("Hello from {}".format(self.name))


def main():
    name = Country()


if __name__== "__main__":
    main()
