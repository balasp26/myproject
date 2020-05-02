import re


text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ

1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Abdul Kalam
Mr Kamarajar
Mr Shakthiman
Mrs. Doubtfire
Mr. B
'''

sentence = 'Start a sentence and then bring it to an end'

# r Represents the Raw String which wiull print the whole string as it is.
print("\ttab") #with out making the string raw
print(r"\ttab") # Making the string Raw

pattern = (r'abcd')

matches = pattern.find(text_to_search)

for match in matches:
	print(match)