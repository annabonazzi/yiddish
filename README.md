# yiddish
Script to transliterate Yiddish text into Latin (English) alphabet.
The script takes in text typed by the user and returns a transliterated version (Hebrew alphabet -> Latin alphabet).

A user-friendly web-based version of this script based on Trinket (https://trinket.io) is available at this website: http://tinyurl.com/yiddish-reader

yiddish_main.py does the input, transliteration, and output tasks.
yiddish_fix_issues.py does the most text-intensive part of the job, which is:
- Editing the transliterated text
- Fixing common issues deriving from transliteration mistakes
- Completely changing Hebrew words commonly used in Yiddish which make no sense when transliterated directly (e.g. 'Sholem Aleykhem' would actually look like 'shlum elikhm' if transliterated directly).
NB: This is a transliterator, not a translator. 

Main problem to be addressed: the current code doesn't know how to deal with diacritic marks, i.e. the tiny dots/lines above or under Hebrew letters. It skips them entirely.
This means that the program is unable to tell the difference between these letters:
- A, O and silent A (אַ, אָ, א) are all considered A
- F and P (פּ, פֿ) are both considered F
- AY and EY (יי, ײַ) are both considered EY.

The temporary solution is a long list of conditions intoduced to deal with the most common mistakes / ambiguities (e.g. 'babe' [grandma] should actully be 'bobe', so it is automaticaly changed to 'bobe').
Although this process does catch most common situations, it's still full of gaps.

Next steps:
- Try and fix this issue at the root by getting the script to recognize diacritics.
- Introducing a larger dictionary of Hebrew words used in Yiddish which have their own peculiar transliteration
