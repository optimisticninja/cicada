#!/usr/bin/env python3

import string

ENGLISH_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

LOOKUP = {
    'F': 2,
    'U': 3,
    'V': 3,
    'TH': 5,
    'O': 7,
    'R': 11,
    'C': 13,
    'K': 13,
    'G': 17,
    'W': 19,
    'H': 23,
    'N': 29,
    'I': 31,
    'J': 37,
    'EO': 41,
    'P': 43,
    'X': 47,
    'S': 53,
    'Z': 53,
    'T': 59,
    'B': 61,
    'E': 67,
    'M': 71,
    'L': 73,
    'NG': 79,
    'ING': 79,
    'OE': 83,
    'D': 89,
    'A': 97,
    'AE': 101,
    'Y': 103,
    'IA': 107,
    'IO': 107,
    'EA': 109
}

FIRST_LETTER_LOOKUP = {}

lookup_keys = LOOKUP.keys()
for letter in ENGLISH_ALPHABET:
    FIRST_LETTER_LOOKUP[letter] = [x for x in LOOKUP.keys() if x.startswith(letter)]

def preprocess(txt, keep_tabs_breaks = True):
    preprocessed = txt.upper()
    if not keep_tabs_breaks:
        processed = txt.replace("\n", " ").replace("\r", " ").replace("\t", " ")
    # kwestion/cwestion q->k
    preprocessed = preprocessed.replace("QU","CW").replace("Q","K")
    return preprocessed


class Gematria:
    @staticmethod
    def english_to_value(txt):
        txt = preprocess(txt)
        i = 0
        result = 0
        txt_iter = iter(txt)
        for c in txt_iter:
            if c in FIRST_LETTER_LOOKUP.keys():
                candidates = FIRST_LETTER_LOOKUP[c]

                # Peek forward in text to match larger possibilities
                peek2 = None
                peek3 = None

                if i + 1 < len(txt) - 1:
                    peek2 = c + txt[i + 1]
                if i + 2 < len(txt) - 1:
                    peek3 = peek2 + txt[i + 2]

                if peek3 and peek3 in candidates:
                    result += LOOKUP[peek3]
                    next(txt_iter, None)
                    next(txt_iter, None)
                    i += 2
                elif peek2 and peek2 in candidates:
                    result += LOOKUP[peek2]
                    next(txt_iter, None)
                    i += 1
                elif c in candidates:
                    result += LOOKUP[c]
                else:
                    if c.isspace() or c in string.punctuation:
                        i += 1
                        continue
            i += 1
        return result

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        print(Gematria.english_to_value(sys.argv[1]))
