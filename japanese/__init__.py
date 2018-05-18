from . import isthis
from . import to
from . import speak
from . import filter

__copyright__ = 'Copyright (C) 2018 Hiroki Takemura'
__version__ = '0.1.0'
__license__ = 'MIT'
__author__ = 'Hiroki Takemura'
__author_email__ = 'hirodora@me.com'
__url__ = 'https://github.com/kekeho/japanese'
__all__ = ['isthis', 'to', 'speak']

seion_dict = {
    'あ': 'ア', 'い': 'イ', 'う': 'ウ', 'え': 'エ', 'お': 'オ',
    'か': 'カ', 'き': 'キ', 'く': 'ク', 'け': 'ケ', 'こ': 'コ',
    'さ': 'サ', 'し': 'シ', 'す': 'ス', 'せ': 'セ', 'そ': 'ソ',
    'た': 'タ', 'ち': 'チ', 'つ': 'ツ', 'て': 'テ', 'と': 'ト',
    'な': 'ナ', 'に': 'ニ', 'ぬ': 'ヌ', 'ね': 'ネ', 'の': 'ノ',
    'は': 'ハ', 'ひ': 'ヒ', 'ふ': 'フ', 'へ': 'ヘ', 'ほ': 'ホ',
    'ま': 'マ', 'み': 'ミ', 'む': 'ム', 'め': 'メ', 'も': 'モ',
    'や': 'ヤ', 'ゆ': 'ユ', 'よ': 'ヨ',
    'ら': 'ラ', 'り': 'リ', 'る': 'ル', 'れ': 'レ', 'ろ': 'ロ',
    'わ': 'ワ', 'ゐ': 'ヰ', 'ゑ': 'ヱ', 'を': 'ヲ',
    'ん': 'ン'
}
dakuon_dict = {
    'が': 'ガ', 'ぎ': 'ギ', 'ぐ': 'グ', 'げ': 'ゲ', 'ご': 'ゴ',
    'ざ': 'ザ', 'じ': 'ジ', 'ず': 'ズ', 'ぜ': 'ゼ', 'ぞ': 'ゾ',
    'だ': 'ダ', 'ぢ': 'ヂ', 'づ': 'ヅ', 'で': 'デ', 'ど': 'ド',
    'ば': 'バ', 'び': 'ビ', 'ぶ': 'ブ', 'べ': 'ベ', 'ぼ': 'ボ',
    'ぱ': 'パ', 'ぴ': 'ピ', 'ぷ': 'プ', 'ぺ': 'ペ', 'ぽ': 'ポ',
}
komoji_hiragana_dict = {
    'ぁ': 'ァ', 'ぃ': 'ィ', 'ぅ': 'ゥ', 'ぇ': 'ェ', 'ぉ': 'ォ',
    'っ': 'ッ',
    'ゃ': 'ャ', 'ゅ': 'ュ', 'ょ': 'ョ',
    'ゎ': 'ヮ',
}
komoji_katakana_dict = {
    'ヵ': 'ヵ', 'ヶ': 'ヶ', #Support: the ヵ&ヶ is only available on Katakana
}
komoji_to_omoji_dict = {
    'ぁ': 'あ', 'ぃ': 'い', 'ぅ': 'う', 'ぇ': 'え', 'ぉ': 'お',
    'ァ': 'ア', 'ィ': 'イ', 'ゥ': 'ウ', 'ェ': 'エ', 'ォ': 'オ',
    'っ': 'つ',
    'ッ': 'ツ',
    'ゃ': 'や', 'ゅ': 'ゆ', 'ょ': 'よ',
    'ャ': 'ヤ', 'ュ': 'ユ', 'ョ': 'ヨ',
    'ゎ': 'わ',
    'ヮ': 'ワ',
    'ヵ': 'カ', 'ヶ': 'ケ',
}

hira_to_katakana_dict = {**seion_dict, **dakuon_dict, **komoji_hiragana_dict}
katakana_to_hira_dict = {**{v:k for k, v in seion_dict.items()}, 
                        **{v:k for k, v in dakuon_dict.items()},
                        **{v:k for k, v in komoji_hiragana_dict.items()},
                        **komoji_katakana_dict}
komoji_dict = {**komoji_hiragana_dict, **komoji_katakana_dict}
omoji_to_komoji_dict = {v:k for k, v in komoji_to_omoji_dict.items()}