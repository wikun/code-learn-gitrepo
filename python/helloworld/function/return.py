def get_formatted_name(first_name,last_name,middle_name=''):
    """return tidy name"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return  full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)
musician = get_formatted_name('jimi','hendrix','lee')
print(musician)

def build_person(first_name,last_name):
    """return a dictionary which include the information of a person"""
    person = {'first':first_name,'last':last_name}
    return person
musician = build_person('jimi','hendrix')
print(musician)