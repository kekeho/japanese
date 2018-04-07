import japanese
pass_chars = ['。', '、', ' ', '\n', '\t', '\b', '\r', '\f']


def hiragana(string: str) -> bool:
    """Is this hiragana?
    Check all char in string is Hiragana.

    Args:
        string(str): check string.
    Returns:
        bool: 
            True: String is completely written by Hiragana.
            False: Hiragana is included in string.
    """
    for char in string:
        if(char in pass_chars or char in japanese.hira_to_katakana_dict):
            pass
        else:
            return False
    # every char is Hiragana
    return True


def katakana(string: str) -> bool:
    """Is this katakana?
    Check all char in string is Katakana.

    Args:
        string(str): check string.
    Returns:
        bool:
            True: String is completely written by Katakana.
            False: Katakana is included in string.
    """
    for char in string:
        if(char in pass_chars or char in japanese.katakana_to_hira_dict):
            pass
        else:
            return False
    # every char is Katakana
    return True


def omoji(string: str) -> bool:
    """Is this Ōmoji?
    Check all char in string is Ōmoji.

    Args:
        string(str): check string.
    Returns:
        bool:
            True: String is completely written by Ōmoji.
            False: Komoji (and more) is included in string.
    """
    for char in string:
        if(char in pass_chars or char not in japanese.komoji_dict):
            pass
        else:
            return False
    # every char is Ōmoji
    return True


def komoji(string: str) -> bool:
    """Is this Komoji?
    Check all char in string is Komoji.

    Args:
        string(str): check string.
    Returns:
        bool:
            True: String is completely written by Komoji.
            False: Komoji
    """
    for char in string:
        if(char in pass_chars or char in japanese.komoji_dict):
            pass
        else:
            return False
    # every char is komoji
    return True
