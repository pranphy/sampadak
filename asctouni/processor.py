#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 ft=python

# author : Prakash [प्रकाश]
# date   : 2018-09-22 23:38

from . import xmlread as rxml

class Processor():
    def __init__(self,pxmlfile):
        self.xml_file = pxmlfile
    
    def process_it(self):
        RXML = rxml.ReadXML(self.xml_file)
        word_info = RXML.read_xml()

if __name__ == '__main__':
    MP = Processor()
    MP.process_it()

