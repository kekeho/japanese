import japanese
pass_chars = ['。', '、', ' ', '\n', '\t', '\b', '\r', '\f']


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
