#!/usr/bin/env python3

class PrcMap():
    def __init__():
        pass

    def getPreRex():
        rexary = [
            [r'ट न ् ]',r'ट्ने'],
            [r'ट न ्',r'ट्न'],
            [r'सा ्रे',r'स्रो'],
            [r'क््र',r'क्र'],
            [r' डँी',r'ँडी'],
            [r'। ञ् ',r'।  ~'],
            [r'थ न ु',r'थुन'],
            [r' ́',r'झ'],
            [r'\nअस््ज्ञकबचयव्क्बदमपयकज्ऋजजब।उटछ\n.*[\n][णज्ञईघद्धछटठडढ]+\n',r' '],
            [r'\n+अस््ज्ञकबचयव्क्बदमपयकज्ऋजजब।उटछ\n[णज्ञईघद्धछटठडढ]+\n',r' '],
            #[r'\n',' '],
            [r'¦',r'ु'],
            [r'ु दँा',r'ुँदा'],
            #[r'',r''],
            [r'”',r'ँ'], #font bug
            
            #आकार इकार उकार च्न्द्रविन्दु आदिको अघिल्तिर स्पेस आउन सक्दैन, आयो भने हटाइदिने
            [r'[\ ]+([ँीाीुूेैोौ])',r'\1'],
            [r' डँी',r'ँडी'], #individual bug
            [r'त्रि०',r'क्रि०'], #individual bug
            
            #चन्द्रविन्दु र शिरिविन्दुलाई यूनिकोडमा टाइप गर्दा आकार इकार उकार को पछाडी राख्नु पर्छ
            [r'([ँं])([ािीुूेैोौ])',r'\2\1'], 
                
        ]
        return rexary


class Mapping():
    def __init__():
        pass

    def getMapping():
        mapdict = {"÷": "/", "v": "ख", "r": "च", "\"": "ू", "~": "ञ्", "z": "श", "ç": "ॐ", "f": "ा", "b": "द", "n": "ल", "j": "व", "×": "×", "V": "ख्", "R": "च्", "ß": "द्म", "^": "६", "Û": "!", "Z": "श्", "F": "ँ", "B": "द्य", "N": "ल्", "Ë": "ङ्ग", "J": "व्", "6": "ट", "2": "द्द", "¿": "रू", ">": "श्र", ":": "स्", "§": "ट्ट", "&": "७", "£": "घ्", "•": "ड्ड", ".": "।", "«": "्र", "*": "८", "„": "ध्र", "w": "ध", "s": "क", "g": "न", "æ": "“", "c": "अ", "o": "य", "k": "प", "W": "ध्", "Ö": "=", "S": "क्", "Ò": "¨", "_": ")", "[": "ृ", "Ú": "’", "G": "न्", "ˆ": "फ्", "C": "ऋ", "O": "इ", "Î": "ङ्ख", "K": "प्", "7": "ठ", "¶": "ठ्ठ", "3": "घ", "9": "ढ", "?": "रु", ";": "स", "'": "ु", "#": "३", "¢": "द्घ", "/": "र", "+": "ं", "ª": "ङ", "t": "त", "p": "उ", "|": "्र", "x": "ह", "å": "द्व", "d": "म", "`": "ञ", "l": "ि", "h": "ज", "T": "त्", "P": "ए", "Ý": "ट्ठ", "\\": "्", "Ù": ";", "X": "ह्", "Å": "हृ", "D": "म्", "@": "२", "Í": "ङ्क", "L": "ी", "H": "ज्", "4": "द्ध", "«": "+", "0": "ण्", "<": "?", "8": "ड", "¥": "र्‍", "$": "४", "¡": "ज्ञ्", ",": ",", "©": "र", "(": "९", "‘": "ॅ", "u": "ग", "q": "त्र", "}": "ै", "y": "थ", "e": "भ", "a": "ब", "i": "ष्", "‰": "झ्", "U": "ग्", "Q": "त्त", "]": "े", "˜": "ऽ", "Y": "थ्", "Ø": "्य", "E": "भ्", "A": "ब्", "M": "ः", "Ì": "न्न", "I": "क्ष्", "5": "छ", "´": "झ", "1": "ज्ञ", "°": "ङ्ढ", "=": ".", "Æ": "”", "‹": "ङ्घ", "%": "५", "¤": "झ्", "!": "१", "-": "(", "›": "द्र", ")": "०", "…": "‘", "Ü": "%","œ":"त्र्","́":"झ"}
        return mapdict
    
    def getExtraMap():
        mapdict = {
            '®':'र',
            '“':'ँ',
            '':'ँ', # ord 147
            '':'-', # ord 151
            }
        return mapdict
    
    def getPreRex():
        rexary = [
            # Any number of spaces following Rhswo Ikar '' should be 
            # descarded no matter what.
            [r'l[ ]+','l'],
            
            # Any number of whitespaces or newlines should be descarded
            # before the characther kri
            [r'[\n ]+{',r'{'],
            
            
            # Tyring to save these unique characers
            # I guess now longer required now.
            [r' \] ',r'Σ'], 
            [' \[ ',r'ί']
            
        ]
        
        return rexary
    
    def getRexArray():
        # After character by character subtution is made
        # we still need to correct the misaligned characters
        # in the word. These regular expression mapping, do the same.
        # for example in preeti like font l character is 
        #
        rexary =[
            [r"्ा", r""], 
            [r"(त्र|त्त)([^उभप]+?)m", r"\1m\2"], 
            [r"त्रm", r"क्र"], [r"त्तm", r"क्त"], 
            [r"([^उभप]+?)m", r"m\1"], 
            [r"उm", r"ऊ"], 
            [r"भm", r"झ"], 
            [r"पm", r"फ"], 
            [r"इ{", r"ई"], 
            [r"ि((.्)*[^्])", r"\1ि"], 
            [r"(.[ािीुूृेैोौंःँ]*?){", r"{\1"], 
            [r"((.्)*){", r"{\1"], 
            [r"{", r"र्"], 
            [r"([ाीुूृेैोौंःँ]+?)(्(.्)*[^्])", r"\2\1"], 
            [r"्([ाीुूृेैोौंःँ]+?)((.्)*[^्])", r"्\2\1"], 
            [r"([ंँ])([ािीुूृेैोौः]*)", r"\2\1"], 
            [r"ँँ", r"ँ"], [r"ंं", r"ं"], 
            [r"ेे", r"े"], 
            [r"ैै", r"ै"], 
            [r"ुु", r"ु"], 
            [r"ूू", r"ू"], 
            [r"^ः", r":"], 
            [r"टृ", r"ट्ट"], 
            [r"ेा", r"ाे"], 
            [r"ैा", r"ाै"], 
            [r"अाे", r"ओ"], 
            [r"अाै", r"औ"], 
            [r"अा", r"आ"], 
            [r"एे", r"ऐ"], 
            [r"ाे", r"ो"], 
            [r"ाै", r"ौ"],
            [r'[\n ]+ो',r'ो'],
            [r'[\n ]+([ेौौाःँृं])',r'\1'],
            [r'Σ',r' ] '],
            [r'ί',' [ '],[r'०ृ',r'० ['],[r'¦ँ',r'ुँ']
        ]
        return rexary
        

def get_preeti_map():
    # This map has been studied properly and has pretty high confidence
    # level for its correctness. This is pretty good, as it looks through.
    mapdict = {
        "÷": "/", 
        "v": "ख", 
        "r": "च", 
        "\"": "ू",
        "~": "ञ्",
        "z": "श",
        "ç": "ॐ",
        "f": "ा",
        "b": "द",
        "n": "ल",
        "j": "व",
        "×": "×",
        "V": "ख्",
        "R": "च्",
        "ß": "द्म",
        "^": "६",
        "Û": "!",
        "Z": "श्",
        "F": "ँ",
        "B": "द्य",
        "N": "ल्",
        "Ë": "ङ्ग",
        "J": "व्",
        "6": "ट",
        "2": "द्द",
        "¿": "रू",
        ">": "श्र",
        ":": "स्",
        "§": "ट्ट",
        "&": "७",
        "£": "घ्",
        "•": "ड्ड",
        ".": "।",
        "«": "्र",
        "*": "८",
        "„": "ध्र",
        "w": "ध",
        "s": "क",
        "g": "न",
        "æ": "“",
        "c": "अ",
        "o": "य",
        "k": "प",
        "W": "ध्",
        "Ö": "=",
        "S": "क्",
        "Ò": "¨",
        "_": ")",
        "[": "ृ",
        "Ú": "’",
        "G": "न्",
        "ˆ": "फ्",
        "C": "ऋ",
        "O": "इ",
        "Î": "ङ्ख",
        "K": "प्",
        "7": "ठ",
        "¶": "ठ्ठ",
        "3": "घ",
        "9": "ढ",
        "?": "रु",
        ";": "स",
        "'": "ु",
        "#": "३",
        "¢": "द्घ",
        "/": "र",
        "+": "ं",
        "ª": "ङ",
        "t": "त",
        "p": "उ",
        "|": "्र",
        "x": "ह",
        "å": "द्व",
        "d": "म",
        "`": "ञ",
        "l": "ि",
        "h": "ज",
        "T": "त्",
        "P": "ए",
        "Ý": "ट्ठ",
        "\\": "्",
        "Ù": ";",
        "X": "ह्",
        "Å": "हृ",
        "D": "म्",
        "@": "२",
        "Í": "ङ्क",
        "L": "ी",
        "H": "ज्",
        "4": "द्ध",
        "«": "+",
        "0": "ण्",
        "<": "?",
        "8": "ड",
        "¥": "र्‍",
        "$": "४",
        "¡": "ज्ञ्",
        ", ": ", ",
        "©": "र",
        "(": "९",
        "‘": "ॅ",
        "u": "ग",
        "q": "त्र",
        "}": "ै",
        "y": "थ",
        "e": "भ",
        "a": "ब",
        "i": "ष्",
        "‰": "झ्",
        "U": "ग्",
        "Q": "त्त",
        "]": "े",
        "˜": "ऽ",
        "Y": "थ्",
        "Ø": "्य",
        "E": "भ्",
        "A": "ब्",
        "M": "ः",
        "Ì": "न्न",
        "I": "क्ष्",
        "5": "छ",
        "´": "झ",
        "1": "ज्ञ",
        "°": "ङ्ढ",
        "=": ".",
        "Æ": "”",
        "‹": "ङ्घ",
        "%": "५",
        "¤": "झ्",
        "!": "१",
        "-": "(",
        "›": "द्र",
        ")": "०",
        "…": "‘",
        "Ü": "%",
        "œ":"त्र्",
        "́":"झ"
    }
