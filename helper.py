from functools import reduce

from mappings import map, word_to_plus_code_mapping

separator = "."

def get_word(code: str):
    return map[code]


def get_code(word: str):
    return word_to_plus_code_mapping[word]


def single_char_phrase(olc: str):
    code = olc.replace('+', '')
    char_arr = [code[i: i+1] for i in range(0, len(code))]
    return reduce(lambda acc, s: acc + separator + get_word(s), char_arr, "")[1:]


def double_char_phrase(olc: str):
    char_arr = []
    code = olc.replace('+', '')
    if len(code) % 2 == 0:
        # Split string into array of 2 char elements.
        char_arr = [code[i: i+2] for i in range(0, len(code), 2)]
    else:
        end_char = code[-1]
        # Split string into array of 2 char elements.
        char_arr = [code[i: i+2] for i in range(0, len(code) - 1, 2)]
        # Add last single character.
        char_arr.append(end_char)
    # Convert coded array to word phrase.
    return reduce(lambda acc, s: acc + separator + get_word(s), char_arr, "")[1:]


def olc_to_phrase(olc: str, single: bool = False):
    if single:
        return single_char_phrase(olc)
    else:
        return double_char_phrase(olc)


def phrase_to_olc(phrase: str):
    word_arr = phrase.split(separator)
    code_arr = [get_code(word_arr[w]) for w in range(0, len(word_arr))]
    code = reduce(lambda acc, c: acc + c, code_arr, "")
    if len(code) % 2 == 0:
        return code[:-2] + "+" + code[-2:]
    return code[:-3] + "+" + code[-3:]
