#coding=utf8

'''
Anna Bonazzi, 07/25/2019

# Script to transliterate text in Yiddish into Latin alphabet to run online on Trinket.
'''

import time, re
from yiddish_fix_issues import fix_issues # Separate file in the same folder
       
# Function to transliterate Yiddish -> Latin
def translit(words):
    alph = {'ק': 'k', 'ר': 'r', 'א': 'a', 'אַ': 'a', 'אָ': 'o', 'ט': 't', 'ו': 'u', 'ן': 'n', 'ם': 'm', 'פ': 'f', 'פֿ': 'f', 'פּ': 'p', 'ש': 'sh', 'שֹ': 's', 'ד': 'd', 'ג': 'g', 'כ': 'kh', 'כּ': 'k', 'ע': 'e', 'י': 'i', 'יִ': 'i', 'ח': 'kh', 'ל': 'l', 'ך': 'kh', 'ף': 'f', 'ז': 'z', 'ס': 's', 'ב': 'b', 'בֿ': 'v', 'ה': 'h', 'נ': 'n', 'מ': 'm', 'צ': 'ts', 'ת': 's', 'תּ': 't', 'ץ': 'ts', 'ײַ': 'ay', 'ײ':'ey', 'ױ':'oy', 'װ':'v'}
    engl_alph = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', '?', '\'', '’',  '"', ';', ':', '-', '!', '[', ']', '(', ')', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '=', ' ', '\t', '\n', 'ü', 'ö', 'ä']
    # Replaces Hebrew characters with Latin
    
    yd = 0
    result = ''
    for c in words:
        if c in alph:
            # Replace  Hebrew character with Latin
            result = result+alph[c]
            yd = 1
        else:
            # Avoids transposing Hebrew diacritics
            if yd == 0:
                result = result+c
            else:
                if c in engl_alph:
                    result = result+c
          
    # Fix known special cases / common problems
    lines = result.split('\n')
    for i in range(0, len(lines)):
        lines[i] = lines[i] + '\n'
    
    newlines = []
    new_count = -1
    for l in lines:
        new_count += 1
        
        # Post-edit only lines that used to be Yiddish
        # Exceptions listed in separate file imported as a module
        l = fix_issues(l)
        
        # Fixes remaining 'ii' as 'ey' (manually check for 'ay')
        l = re.sub('ii', 'ey', l)
        # Makes upper case
        low = re.findall('(\t|\.|\!|\?|:)( |)([a-z])', l)
        for lo in low:
            new_lo = (''.join(lo)).upper()
            
            l = l.replace(''.join(lo), new_lo)
        
        newlines.append(l)
        
    text = ''.join(newlines)
    if yd == 0:
      pass#text = '\n(That was not Yiddish)\n\n'+text
    return(text)

print('\n\n\tWelcome to the Yiddish transliterator!\n\n\t• Paste or type some Yiddish text\n\t• Press \'enter\' to transliterate it into Latin (English) characters\n\t• Press the \'Run\' button on top to restart.\n\n\t➜ Try this: שלום עליכמ\n\n')
while 1 == 1:
    #words = raw_input('\n\n ->  ')
    words = input()
    
    if words =='stop':
        pass#break
    #print(type(''.join(words)))
    text = translit(words)
    print(text)