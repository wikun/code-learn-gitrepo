favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
print(f"Sarah's favorite language is {favorite_languages['sarah'].title()}")

alien = {'color':'green','speed':'slow'}
point_value = alien.get('point','no point value assigned')
print(point_value)