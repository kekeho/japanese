# Python Japanese Library
for Humans!  
Only for Python3. Not support python2.x

## Install
`pip install japanese`

## Use
```python
import japanese as ja
gyaru = 'わたしギャルいちねんせい。こもぢとかまだわかんない。、、りすかしよ'
#Convert Omoji to Komoji
ja.to.lower(gyaru) # -> 'ゎたしギャルぃちねんせぃ。こもぢとかまだゎかんな。、、りすかしょ'

#Check all char is Hiragana
ja.isthis.hiragana(gyaru) # -> False

#Check all char is Katakana
ja.isthis.katakana(gyaru) # -> False
```