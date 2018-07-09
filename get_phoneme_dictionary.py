from urllib import request
import os

DICTIONARY_FILE = 'cmudict-0.7b'
DICTIONARY_URL = 'http://svn.code.sf.net/p/cmusphinx/code/trunk/cmudict/cmudict-0.7b'

PUNCTUATION_EXCEPTIONS = ('3D', "'TIL", "'TIS", "'TWAS", "'ROUND", "'S", "'KAY", "'M", "'N", "'FRISCO", "'GAIN",
                          "'BOUT", "'CAUSE", "'COURSE", "'CUSE", "'EM", "'ALLO")

WORD_TO_PHONEME_DICTIONARY = None
PHONEME_TO_WORD_DICTIONARY = None


def get_phoneme_dictionary():
    if not os.path.isfile('./' + DICTIONARY_FILE):
        print("Downloading dictionary...")
        req_response = request.urlopen(DICTIONARY_URL)
        phoneme_dict_str = req_response.read().decode('latin-1')
        write_dict = ''
        while write_dict.lower() not in ('y', 'n'):
            write_dict = input("Write phoneme dictionary to file for future you? [y/n] ").strip()
        if write_dict.lower() == 'y':
            with open('./' + DICTIONARY_FILE, 'w') as f:
                f.write(phoneme_dict_str)
    else:
        with open('./' + DICTIONARY_FILE) as f:
            phoneme_dict_str = f.read()
    word_to_phoneme = {}
    for line in phoneme_dict_str.split('\n'):
        if line and not line.startswith(';;;'):
            line = line.split()
            word = line[0]
            # remove numbers indicating stress
            phonemes = tuple(''.join([c for c in ph if not c.isdigit()]) for ph in line[1:])
            if not word[0].isalpha() and word != '3D':
                # TODO: specific allowed bits, associated with advanced word splitting?
                pass
            elif word[-1] == ')' and word[-3] == '(':
                # TODO: alternate pronounciations
                pass
            else:
                word_to_phoneme[word] = phonemes
    return word_to_phoneme
