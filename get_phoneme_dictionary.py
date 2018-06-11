from urllib import request

DICTIONARY_URL = 'http://svn.code.sf.net/p/cmusphinx/code/trunk/cmudict/cmudict-0.7b'


word_to_phoneme = {}

with request.urlopen(DICTIONARY_URL) as f:
    for bytes_line in f:
        line = bytes_line.decode('latin-1').strip()
        if line and not line.startswith(';;;'):
            line = line.split()
            word_to_phoneme[line[0]] = [''.join([c for c in ph if not c.isdigit()]) for ph in line[1:]]






pass