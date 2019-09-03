# Sampadak (सम्पादक) 
This is a utility application to help with all sorts of text processing related to Nepali language.



# Installation 
Simply clone this repository and put the location of  executable `sampadak` in your path.


# Usage 

```
sampadak -i <input_filename> -o <output_filename> -a <action>
```

Say you want to convert a text file with ascii codes corresponding to Nepali text in Preeti (like) font (s) called `preeti_asc.txt` and you want to ge the unicode version of this text file named `unicode.txt` you will need to do

```
sampadak -i preeti_asc.txt -o unicode.txt -a asctouni
```

The action parameter (a) is the action to be done in the file.

## Available actions

Currently the only available action is `asctouni` which converts ascii text to unicode text assuming the text file is ascii values corresponding to Nepali text in Preeti(like) font(s).
