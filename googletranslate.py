# 1) Translate
from googletrans import Translator

trans = Translator()
t = trans.translate(
    'Best out of wast', src= 'en', dest='ta'
)
print(f'Source: {t.src}')
print(f'Destination: {t.dest}')
print(f'{t.origin} -> {t.text}')
print()

# 2) List supported languages
from googletrans import LANGUAGES

for lang in LANGUAGES:
    print(f'{lang} - {LANGUAGES[lang]}')
print()

# 3) List possible mistakes and translations 
pm = t.extra_data['possible-mistakes']
pt = t.extra_data['possible-translations']

print(f'Possible Mistakes: {en}')
print(f'Possible Translations: {ta}')