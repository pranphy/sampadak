#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 ft=python

# author : Prakash [प्रकाश]
# date   : 2019-09-08 12:04



class Group():
    class consonants:
        # There are some characters which if appearing
        # in the end of word are pronunced without the 
        # halant as done generally in other characters
        end_full = ['छ','य', 'र','व','ह']
        maps ={
            'क':'k',
            'ख':'kh',
            'ग':'g',
            'घ':'gh',
            'ङ':'ng',
            'च':'ch',
            'छ':'chh',
            'ज':'j',
            'झ':'jh',
            'ञ':'yn',
            'ट':'t',
            'ठ':'th',
            'ड':'d',
            'ढ':'dh',
            'ण':'n',
            'त':'t',
            'थ':'th',
            'द':'d',
            'ध':'dh',
            'न':'n',
            'प':'p',
            'फ':'ph',
            'ब':'b',
            'भ':'bh',
            'म':'m',
            'य':'y',
            'र':'r',
            'ल':'l',
            'व':'w',
            'श':'sh',
            'ष':'sh',
            'स':'s',
            'ह':'h',
        }

    class vowel_suffix:
        all = ['ा','ि','ी','ु','ू','े','ै','ो','ौ']
        maps = {
            'ा':'a',
            'ि':'i',
            'ी':'i',
            'ु':'u',
            'ू':'u',
            'ृ':'ri',
            'े':'e',
            'ै':'ai',
            'ो':'o',
            'ौ':'u',
            'ः':'',
        }
    class digits:
        maps = {
            '०':'0',
            '१':'1',
            '२':'2',
            '३':'3',
            '४':'4',
            '५':'5',
            '६':'6',
            '७':'7',
            '८':'8',
            '९':'9',
        }
    class vowel_full:
        all = ['अ','आ','इ','ई','उ','ऊ','ऋ','ए','ऐ','ओ','औ']
        maps = {
            'अ':'a',
            'आ':'aa',
            'इ':'i',
            'ई':'i',
            'उ':'u',
            'ऊ':'u',
            'ऋ':'ri',
            'ए':'e',
            'ऐ':'ai',
            'ओ':'o',
            'औ':'au',
        }
    class pancham:
        maps = {
            'ं':'m',
            'ँ':'n',
        }
    class punctuation:
        maps = {
            '।':'.',
            ' ': ' ',
        }
    class joiners:
        # Obviously in some editors the joiners are invisible. Might seem
        # like ghost traansformation. I should figure out some way of having
        # unicode key instead.
        maps = {
            '‌':'',
            '‍':'',
        }
    class pass_chars:
        map_ind = {
            '\n':'\n',
        }
        maps_list = [
            map_ind,
            {k:k for k in ':.,;[]{}()+_!@#$%^&?'},
            {k:k for k in 'abcdefghijklmnopqrstuvwxyz'},
            {k:k for k in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
        ]

        maps = {k: v for d in maps_list for k, v in d.items()}

        all = [k for k in maps]

def get_map():
    return dict(
        **Group.vowel_full.maps,
        **Group.vowel_suffix.maps,
        **Group.consonants.maps,
        **Group.pancham.maps,
        **Group.digits.maps,
        **Group.punctuation.maps,
        **Group.joiners.maps,
        **Group.pass_chars.maps

    )


HALANT = '्'
PURNABIRAM = '।'

#VOWELS = Group.vowel_full.all + Group.vowel_suffix.all
VOWELS = Group.vowel_full.all
VOWELS_SUFFIX = Group.vowel_suffix.all

SPECIAL = 'ँंृः। '

# Many a times we have seen the combination of character
# (ा) (े) used  wrontly as substitute for (ो). This is to
# identify them
WOWRONG = 'ाे'
WORIGHT = 'ो'

# This is another one fo the issues.
AAWRONG = 'अा'
AARIGHT = 'आ'

END_CONSONANT_FULL = Group.consonants.end_full

# Pass list
# The list of non nepali characters infiltrating
PASS_CHARS = Group.pass_chars.all
