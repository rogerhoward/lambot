#!/usr/bin/env python


class BaseClass(object):
    def __init__(self):
        self.someMethod()

    def someMethod(self):
        print('using base class')


class ChildClass(BaseClass):
    def someMethod(self):
        print('using child class')


bc = BaseClass()
cc = ChildClass()
