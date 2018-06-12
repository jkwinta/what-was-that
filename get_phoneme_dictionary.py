from urllib import request
import os
from sys import stderr

DICTIONARY_DIR = './files'

if not os.path.isdir(DICTIONARY_DIR):
    if os.path.isfile(DICTIONARY_DIR):
        print('You have a file where a directory should be in {}'.format(DICTIONARY_DIR), file=stderr)
        exit(1)
    os.mkdir(DICTIONARY_DIR)
    

DICTIONARY_URL = 'http://svn.code.sf.net/p/cmusphinx/code/trunk/cmudict/cmudict-0.7b'

word_to_phoneme = {}

with request.urlopen(DICTIONARY_URL) as f:
    for bytes_line in f:
        line = bytes_line.decode('latin-1').strip()
        if line and not line.startswith(';;;'):
            line = line.split()
            word_to_phoneme[line[0]] = [''.join([c for c in ph if not c.isdigit()]) for ph in line[1:]]

pass
