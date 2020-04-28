#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 ft=python

# author : Prakash [प्रकाश]
# date   : 2019-08-09 17:52


import re

from . import mapping as transmap


class Translit():
    def __init__(self):
        pass

    def get_trans_keys(self):
        pass

    def  preprocess(self,line):
        # Just to correct that pesky wrong e sound. Check transmap
        # for more explanation
        line = re.sub(transmap.WOWRONG,transmap.WORIGHT,line)
        line = re.sub(transmap.AAWRONG,transmap.AARIGHT,line)
        return line



    def  calculate_distance(self,word1,word2):
        pass

    
    def trans_to_ascii(self,uni_keys):
        uni_keys = self.preprocess(uni_keys)
        keys_length = len(uni_keys)
        map_dict = transmap.get_map()
        word = ''
        i = 0
        while i < keys_length:
            full_char = True
            char =  uni_keys[i]
            nexchar = uni_keys[i+1] if i < keys_length -1  else ''
            #if i == 0 and char == transmap.HALANT:
            #    raise


            if (
                    nexchar == transmap.HALANT or 
                    nexchar in transmap.VOWELS_SUFFIX or
                    char in transmap.VOWELS  or 
                    char in transmap.VOWELS_SUFFIX or
                    char in transmap.SPECIAL or
                    char in transmap.PASS_CHARS
                ):
                full_char = False

            # Generally in Nepali the last consonant is pronunced consonant even
            # if it doesn't come with a HALANT sign. But also in nepali language
            # there are certain characeters which are pronunced as full character
            # if they are at the end like the on in the list below
            if i == keys_length-1:
                if char in transmap.END_CONSONANT_FULL:
                    full_char = True
                else:
                    full_char = False
                if uni_keys[i-1] == transmap.HALANT:
                    full_char = True

            # One character word is always full
            if keys_length == 1:
                full_char = True


            if char in transmap.PASS_CHARS:
                full_char = False

            asc_val =  char
            try:
                asc_val = map_dict[char]
            except:
                raise Exception('Unknown character ',char)
                asc_val = char

            asc_char = asc_val+'a' if full_char else asc_val
            word = word + asc_char

            i += 1
            if nexchar == transmap.HALANT:
                i += 1
        return word


    def translit_wordlist(self,ipfile,opfile):
        wordlist = []
        print('writing file ',opfile)
        with open(ipfile,'r') as ifile:
            with open(opfile,'w') as ofile:
                for line in ifile:
                    line = self.preprocess(line)
                    for word in line.split(' '):
                        word = word.strip()
                        word = re.sub(transmap.PURNABIRAM,'',word)
                        word = re.sub(',',' ',word)

                        asc_word = self.trans_to_ascii(word)
                        if word not in wordlist:
                            ofile.write(f'{word} : {asc_word} \n')
                        wordlist.append(word)
        
    def trans_to_unicode(self,ascii_keys):
        trans_map = {}


    def  test_in_loop(self):
        a = ' '
        while not (a == ''):
            #a = nput_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
            a = input('Enter your word: ')
            print(a)
            #a = input()
            print(self.trans_to_ascii(a))


if __name__ == '__main__':
    MP = Translit()
    MP.trans_to_ascii(other_params)

