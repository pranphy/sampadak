#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 ft=python

# author : Prakash [प्रकाश]
# date   : 2018/09/07


import re

from .mapping import Mapping as mpg
from .mapping import PrcMap as Prm

class Converter():
    def __init__(self):
        self.preeti_extra_dict = mpg.getExtraMap()
        self.preeti_char_dict  = mpg.getMapping()
        self.preeti_post_rex = mpg.getRexArray()

    
    def sub_rex_array(self,paragraph,rex):
        for rx in rex:
            try:
                paragraph = re.sub(rx[0],rx[1],paragraph)
            except TypeError:
                pass
        return paragraph
    
    def process_before_char_sub(self,paragraph):
        """
        Processes the word before character substitution

        :type    paragraph: str
        :param   paragraph: word or paragraph to process

        """
        pre_rex = mpg.getPreRex()
        paragraph = self.sub_rex_array(paragraph,pre_rex)
        return paragraph
    
    def convert_preeti(self,paragraph):
        """
        Convert a given paragraph from preeti to unicode

        :type    paragraph: str
        :param   paragraph: word or paragraph to convert to unicode, assumes its composed of ascii of preeti

        """
        post_rex = self.preeti_post_rex
        paragraph = self.process_before_char_sub(paragraph) 
        converted_par = '' # Huge bug found  Fri Apr  5 00:07:45 EDT 2019, whas ' ' instead of ''
        # now do the char sub
        if paragraph != None: 
            for char in paragraph:
                try:
                    unicode_char = self.preeti_char_dict[char]
                    converted_par += unicode_char
                except KeyError:
                    try:
                        extra_unicode_char = self.preeti_extra_dict[char]
                        converted_par += extra_unicode_char
                    except KeyError:
                        converted_par += char
            # now postrex
        converted_par = self.sub_rex_array(converted_par,post_rex)
        return converted_par
                   
    def convert_word(self,word,font='preeti'):
        """
        Convert word of ascii to unicode of given font

        :type    word: str
        :param   word: the word to convert

        :type    font: str
        :param   font: the identifier of font to convert from

        """
        converted = word
        if font == 'preeti':
            converted = self.convert_preeti(word)
        return converted

    def test(self):
        word = r''' CL ;+3Lo sflGtk'/ eQmk'/ kl/qmdf  '''
        c_word = self.convert_word(word)
        return word,c_word
        

if __name__ == '__main__':
    MP = Converter()
    # word = 
    word = 'zfsfxf/L #fF; kqlsf kl/s\/df'
    c_word = MP.convert_word(word)
    print(' {}  == > {} '.format(word,c_word))

