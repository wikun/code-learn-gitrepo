user_0 = {
    'username' : 'efermi',
    'first' : 'enrico',
    'last' : 'fermi',
}

for key,value in user_0.items():
    print(f'\nkey:{key}')
    print(f'value:{value}')

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
for name,language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

for name in favorite_languages.keys():
    print(name.title())
for language in favorite_languages.values():
    print(language.title())

for language in set(favorite_languages.values()):
    print(language.title())