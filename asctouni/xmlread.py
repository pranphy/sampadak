#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 ft=python

# author : Prakash [प्रकाश]
# date   : 2018/09/08

import os
import xml.etree.ElementTree as et

#import .converter as cvt
from . import converter as cvt



class ReadXML():
    def __init__(self,pxmlfile):
        self.xml_file = pxmlfile

        namespace_prefix = f'urn:oasis:names:tc:opendocument:xmlns'
        ns_ids = ['office','drawing','text','table','style']

        self.ns = {id:f'{namespace_prefix}:{id}:1.0' for id in ns_ids}
    
    def set_xml_file(self,xml_file):
        self.xml_file = xml_file

    def get_font_stat(self):
        tree = et.parse(self.xml_file)
        root = tree.getroot()
        faces = []

        for face_decls in root.findall('office:font-face-decls',self.ns):
            for font_face in face_decls.findall('style:font-face',self.ns):
                atrb = font_face.attrib
                face_name = atrb['{'+self.ns['style']+'}name']                
                faces.append(face_name)

    
        font_styles = {}

        for auto_style in root.findall('office:automatic-styles',self.ns):
            for style in auto_style.findall('style:style',self.ns):
                if style.attrib['{'+self.ns['style']+'}family'] == 'text':
                    st_name = style.attrib['{'+self.ns['style']+'}name']
                    for text_prop in style.findall('style:text-properties',self.ns):
                        st_font_name= text_prop.attrib['{'+self.ns['style']+'}font-name']
                        font_styles[st_name] = st_font_name


        print(font_styles)
        return font_styles
    
    def read_xml_blockwise(self):
        tree = et.parse(self.xml_file)
        root = tree.getroot()
        for body in root.findall('office:body',self.ns):
            for drawing in body.findall('office:drawing',self.ns):
                for page in drawing.findall('drawing:page',self.ns):
                    for frame in page.findall('drawing:frame',self.ns):
                        for text_box in frame.findall('drawing:text-box',self.ns):
                            for p in text_box.findall('text:p',self.ns):
                                for span in p.findall('text:span',self.ns):
                                    atrb = span.attrib
                                    nst = '{'+self.ns['text']+'}style-name'
                                    style = atrb[nst]
                                    txt = "".join(span.itertext())
                                    yield (style,txt)

    def save_to_txt(self,output_file):
        with open(output_file,'w') as ofl:
            for _,txt in self.read_xml_blockwise():
                ofl.write(txt)
            




    def read_xml(self):
        lw = []
        for style,txt in self.read_xml_blockwise():
            tp = (style,txt)
            lw.append(tp)

        return lw

    def show_font_stat(self):
        self.get_font_stat()

    def show_info(self):
        lw = self.read_xml()
        for ft,word in lw:
            cvcl = cvt.Converter()
            c_word = word
            if ft != 'T8':
                c_word = cvcl.convert_word(word)

            print(f'{ft} ::{word}::{c_word}::')

    def show_font_text(self):
        lw = self.read_xml()
        for ft,word in lw:
            print(f'{ft} :: {word} ')

    def write_file(self,output_file):
        print(f'म यो फाइल लेख्दै छु अब::{output_file}')
        lw = self.read_xml()
        print(f'Lw ahs {len(lw)} elements')
        with open(output_file,'w') as ofl:
            for ft,word in lw:
                cvcl = cvt.Converter()
                c_word = word
                if ft not in ['T7', 'T9']:
                    c_word = cvcl.convert_word(word)

                # T5 147 is chandrabindu
                # T5 151 is -

                print(f'{c_word}',end='',flush=True)
                #print(f'{c_word} has {c_word.count(" ")} spaces ')
                #c_word = c_word.replace(' ','<spc>')
                ofl.write(f'{c_word}')


if __name__ == '__main__':
    MP = ReadXML('test')
    MP.show_info()
