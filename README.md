# Python Japanese Library
for Humans!  
Only for Python3. Not support python2.x

## Install
`pip install japanese`

## Use
```python
import japanese as ja
gyaru = 'わたしギャルいちねんせい。こもぢとかまだわかんない。、、りすかしよ'
#Convert Omoji to Komoji
ja.to.lower(gyaru) # -> 'ゎたしギャルぃちねんせぃ。こもぢとかまだゎかんなぃ。、、りすかしょ'

hiragana = 'これは、ひらがなのみでこうせいされたすとりんぐ。'
hiragana_katakana_kanji = 'これは, ひらがな以外も含まれたストリング.'
katakana = 'コレハ、スベテカタカナノストリング。'

#Check all char is Hiragana
ja.isthis.hiragana(hiragana) # -> True
ja.isthis.hiragana(hiragana_katakana_kanji) # -> False

#Check all char is Katakana
ja.isthis.katakana(katakana) # -> True
```

## Reference
Reference is [here](http://kekeho.com/japanese/)