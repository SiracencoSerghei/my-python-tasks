"""Write two functions that convert a roman numeral to and from an integer
value. Multiple roman numeral values will be tested for each function.

Modern Roman numerals are written by expressing each digit separately starting
with the left most digit and skipping any digit with a value of zero.
In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC.
2008 is written as 2000=MM, 8=VIII; or MMVIII.
1666 uses each Roman symbol in descending order: MDCLXVI.

Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

Examples
to roman:
2000 -> "MM"
1666 -> "MDCLXVI"
1000 -> "M"
 400 -> "CD"
  90 -> "XC"
  40 -> "XL"
   1 -> "I"

from roman:
"MM"      -> 2000
"MDCLXVI" -> 1666
"M"       -> 1000
"CD"      -> 400
"XC"      -> 90
"XL"      -> 40
"I"       -> 1

Help
Symbol	Value
I	1
IV	4
V	5
X	10
L	50
C	100
D	500
M	1000
"""

#
# class RomanNumerals:
#     roman_numbers = {
#         "I": 1,
#         "V": 5,
#         "X": 10,
#         "L": 50,
#         "C": 100,
#         "D": 500,
#         "M": 1000
#     }
#
#     @staticmethod
#     def to_roman(val: int) -> str:
#         list_of_roman_numbers = []
#         divisor = 10 ** (len(str(val)) - 1)
#         while val != 0:
#             roman_number = None
#             # val = int(input(" input val or 0 for exit: "))
#             d = val // divisor
#             pr = val % divisor
#             for key, value in RomanNumerals.roman_numbers.items():
#                 if divisor == value:
#                     if d < 4:
#                         roman_number = key * d
#                     elif d == 4:
#                         next_key = list(RomanNumerals.roman_numbers.keys())[
#                             list(RomanNumerals.roman_numbers.values()).index(value * 5)]
#                         roman_number = key + next_key
#                     elif 5 <= d < 9:
#                         roman_number = list(RomanNumerals.roman_numbers.keys())[
#                                            list(RomanNumerals.roman_numbers.values()).index(value * 5)] + key * (d - 5)
#                     elif d == 9:
#                         next_key = list(RomanNumerals.roman_numbers.keys())[
#                             list(RomanNumerals.roman_numbers.values()).index(value * 10)]
#                         roman_number = key + next_key
#
#             if roman_number:
#                 list_of_roman_numbers.append(roman_number)
#             val = pr
#             divisor = int(divisor / 10)
#         return "".join(list_of_roman_numbers)
#
#     @staticmethod
#     def from_roman(roman_num: str) -> int:
#         list_of_roman_numbers = list(roman_num)
#         list_of_arabic_numbers = []
#         i = 0
#         while i < len(list_of_roman_numbers):
#             char = list_of_roman_numbers[i]
#
#             successive_roman_number = list_of_roman_numbers[i + 1] if i + 1 < len(list_of_roman_numbers) else None
#
#             has_I = char == "I" and successive_roman_number in ("V", "X")
#             has_X = char == "X" and successive_roman_number in ("L", "C", "M")
#             has_C = char == "C" and successive_roman_number in ("D", "M")
#
#             arabic_number = RomanNumerals.roman_numbers[char]
#             if has_I or has_X or has_C:
#                 if successive_roman_number:
#                     successive_arabic_number = RomanNumerals.roman_numbers[successive_roman_number]
#                     arabic_number = successive_arabic_number - arabic_number
#                     i += 1
#             list_of_arabic_numbers.append(arabic_number)
#             i += 1
#         arabic_num = sum(list_of_arabic_numbers)
#         return arabic_num

# ==========================================================

#
# from collections import OrderedDict
# import re
#
# ROMAN_NUMERALS = OrderedDict([
#     ('M', 1000),
#     ('CM', 900),
#     ('D', 500),
#     ('CD', 400),
#     ('C', 100),
#     ('XC', 90),
#     ('L', 50),
#     ('XL', 40),
#     ('X', 10),
#     ('IX', 9),
#     ('V', 5),
#     ('IV', 4),
#     ('I', 1),
# ])
#
# DECIMAL_TO_ROMAN = [(v, k) for k, v in ROMAN_NUMERALS.items()]
#
# ROMAN_RE = '|'.join(ROMAN_NUMERALS)
#
#
# class RomanNumerals(object):
#     @staticmethod
#     def from_roman(roman):
#         return sum(ROMAN_NUMERALS[d] for d in re.findall(ROMAN_RE, roman))
#
#     @staticmethod
#     def to_roman(decimal):
#         result = []
#         for number, roman in DECIMAL_TO_ROMAN:
#             while decimal >= number:
#                 decimal -= number
#                 result.append(roman)
#         return ''.join(result)


# ========================================================

# class RomanNumerals:
#
#     def to_roman(val):
#         onesRoman = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
#         tensRoman = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
#         hundsRoman = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
#         thousRoman = ["", "M", "MM", "MMM", "MMMM"]
#
#         ones = onesRoman[val % 10]
#         tens = tensRoman[val // 10 % 10]
#         hunds = hundsRoman[val // 100 % 10]
#         thous = thousRoman[val // 1000]
#
#         return thous + hunds + tens + ones
#
#     def from_roman(roman_num):
#         out = 0
#         mx = 0
#         for cur in map(lambda c: {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}[c], roman_num[::-1]):
#             if cur >= mx:
#                 out += cur
#                 mx = cur
#             else:
#                 out -= cur
#
#         return out
#

# =================================================

# from itertools import groupby
#
# """A RomanNumerals helper object"""
#
#
# class RomanNumerals(object):
#     letters = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90),
#                ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]
#
#     @classmethod
#     def to_roman(cls, val):
#         rom = []
#         for l, v in cls.letters:
#             m = val // v
#             rom += m * [l]
#             val -= m * v
#         return ''.join(rom)
#
#     @classmethod
#     def from_roman(cls, rom):
#         cumu = 0
#         for l, v in cls.letters:
#             while rom[:len(l)] == l:
#                 rom = rom[len(l):]
#                 cumu += v
#             if not rom: break
#         return cumu


# ======================================================


class RomanNumerals:
    @staticmethod
    def from_roman(s):
        X=[dict(zip('MDCLXVI',(1e3,500,100,50,10,5,1)))[x]for x in s]
        return int(sum((x,-x)[x<y]for x,y in zip(X,X[1:]))+X[-1])
    @staticmethod
    def to_roman(i,o=' I II III IV V VI VII VIII IX'.split(' ')):
        r=lambda n:o[n]if n<10 else''.join(dict(zip('IVXLC','XLCDM'))[c]for c in r(n//10))+o[n%10]
        return r(i)
    

# ======================================================

result = RomanNumerals.from_roman("MDCLXVI")  # 1666
print(result)
result = RomanNumerals.from_roman("MMVIII")  # 2008
print(result)
result = RomanNumerals.from_roman("MCMXC")  # 1990
print(result)
result = RomanNumerals.to_roman(21)  # XXI
print(result)
result = RomanNumerals.to_roman(1)  # I
print(result)
result = RomanNumerals.to_roman(4)  # IV
print(result)
result = RomanNumerals.to_roman(2008)  # MMVIII
print(result)
result = RomanNumerals.to_roman(1666)  # MDCLXVI
print(result)
