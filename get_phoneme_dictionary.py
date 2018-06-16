from urllib import request
import os


DICTIONARY_FILE = 'cmudict-0.7b'
DICTIONARY_URL = 'http://svn.code.sf.net/p/cmusphinx/code/trunk/cmudict/cmudict-0.7b'


def get_phoneme_dictionary():
    if not os.path.isfile('./' + DICTIONARY_FILE):
        print("Downloading dictionary...")
        req_response = request.urlopen(DICTIONARY_URL)
        phoneme_dict_str = req_response.read().decode('latin-1')
        write_dict = ''
        while write_dict.lower() not in ('y', 'n'):
            write_dict = input("Write phoneme dictionary to file for future you? [y/n]").strip()
        if write_dict == 'y':
            with open('./' + DICTIONARY_FILE, 'w') as f:
                f.write(phoneme_dict_str)
    else:
        with open('./' + DICTIONARY_FILE) as f:
            phoneme_dict_str = f.read()
    word_to_phoneme = {}
    for line in phoneme_dict_str.split('\n'):
        if line and not line.startswith(';;;'):
            line = line.split()
            word_to_phoneme[line[0]] = [''.join([c for c in ph if not c.isdigit()]) for ph in line[1:]]
    return word_to_phoneme
