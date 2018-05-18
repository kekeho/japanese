import japanese
from janome.tokenizer import Tokenizer
pass_chars = ['。', '、', ' ', '\n', '\t', '\b', '\r', '\f']

t = Tokenizer(mmap=True)

def upper(string: str) -> str:
    """Convert to Ōmoji every char.
    Args:
        string(str): Check string
    Returns:
        Converted string(str)
    """
    if(isinstance(string, str)):  # string is str
        for char in string:
            if(char in japanese.komoji_to_omoji_dict):
                # replace komoji to omoji
                string = string.replace(
                    char, japanese.komoji_to_omoji_dict[char])
        return string
    else:
        raise ValueError('arg must be str')


def lower(string: str) -> str:
    """Convert to Komoji every char.
    Args:
        string(str): Check string
    Returns:
        Converted string(str)
    """
    if(isinstance(string, str)):  # string is str
        for char in string:
            if(char in japanese.omoji_to_komoji_dict):
                # replace omoji to komoji
                string = string.replace(
                    char, japanese.omoji_to_komoji_dict[char])
        return string
    else:
        raise ValueError('arg must be str')


def katakana(string: str) -> str:
    """Convert sentence(include Kanji) to Katakana string.
    Args:
        string(str): Input string which includes Kanji
    Returns:
        Converted Katakana string
    """
    if(isinstance(string, str)):
        global t
        word_list = t.tokenize(string, stream=True)

        kana_string = ''
        for word in word_list:
            if(word.reading is '*'):
                kana_string += word.surface
            else:
                kana_string += word.reading

        return kana_string
    else:
        raise ValueError('arg must be str')


def hiragana(string: str) -> str:
    """Convert sentence(include Kanji) to Hiragana string.
    Args:
        string(str): Input string which includes Kanji
    Returns:
        Converted Hiragana string
    """
    if(isinstance(string, str)):
        katakana_string = katakana(string)
        hiragana_string = ''
        for word in katakana_string:
            if(japanese.isthis.katakana(word) is False):
                hiragana_string += word
            else:
                hiragana_string += japanese.katakana_to_hira_dict[word]

        return hiragana_string
    else:
        raise ValueError('arg must be str')


def phonetic(string: str) -> str:
    """Convert Sentence to phonetic(Katakana)
    Example: 東京→トーキョー
    Arg:
        string(str): Input string
    Return:
        Katakana(str)
    """
    if(isinstance(string, str)):
        global t
        word_list = t.tokenize(string, stream=True)

        kana_string = ''
        for word in word_list:
            if(word.phonetic is '*'):
                kana_string += word.surface
            else:
                kana_string += word.phonetic

        return kana_string
    else:
        raise ValueError('arg must be str')
