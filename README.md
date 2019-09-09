# Sampadak (सम्पादक) 
This is a utility application to help with all sorts of text processing related to Nepali language. It can be used to convert from Nepali typed in `preeti` like fonts to unicode.  There is also possibility of converting unicode Nepali to romanized Nepali.





# Installation 
Clone this repository and install.
```
git clone https://github.com/pranphy/sampadak.git
cd sampadak
python3 setup.py install
```
This should make `sampadak` executable availabel in CLI.



# Usage 
The documentation has
```
~$ sampadak --help
Usage: sampadak [OPTIONS]

Options:
  -i, --input TEXT                input file name
  -o, --output TEXT               output file name
  -d, --ipdir TEXT                output directory default .
  -a, --action [asctouni|unitoasc]
                                  action to perform
  -t, --text TEXT                 text to process
  --help                          Show this message and exit.
```


```
~$ sampadak -i <input_filename> -o <output_filename> -a <action>
```

Say you want to convert a text file with ascii codes corresponding to Nepali text in Preeti (like) font (s) called `preeti_asc.txt` and you want to ge the unicode version of this text file named `unicode.txt` you will need to do

```
~$ sampadak -i preeti_asc.txt -o unicode.txt -a asctouni
```

The action parameter (a) is the action to be done in the file.

Currently the ~~only~~ available actions ~~is~~ are `asctouni` which converts ascii text to unicode text assuming the text file is ascii values corresponding to Nepali text in Preeti(like) font(s) and `unitoasc` which converts unicode nepali text into romanized texts.

## FAQ

1. Why another converter?

    First of all there are no any good python libraries to do this. Also, I have seen that the ones found all over th internet, mostly based on javascript, have a lot of problem in them. 
    
    Also I have not yet found a good transliterator that converts unicode Nepali to romanized Nepali. The reverse however are plenty (again javascript based).
    
2. Can it be used as a library?

Yes it can, but currently the documentation is non-existant, so it would be hard to get started with. Once I put together documentation and some more features you can use this as library and enjoy.

3. License?

MIT

