#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 ft=python

# author : Prakash [प्रकाश]
# date   : 2019-08-09 15:45

import pickle as pkl

class MakeWordList():
    def __init__(self):
        pass

    def get_saved_data(sel,filename):
        return pkl.load(filename)

    def save_data(self,filename):
        pkl.save(filename)
    
    def write_list(self,filename):
        pass

    
    def nepali_words(self,):
        return "हमी"

    def update_wordlist(self,filename):
        pass





if __name__ == '__main__':
    MP = MakeWordList()
    MP.write_list(filename)
