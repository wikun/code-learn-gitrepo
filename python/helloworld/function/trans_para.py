def describe_pet(pet_name,animal_type='cat'):
    """display information of pets"""
    print(f"\nI have a {animal_type}.")
    print(f"It's name is {pet_name.title()}.")

describe_pet('harry','dog')
describe_pet(animal_type='dog',pet_name='harry')
describe_pet(pet_name='willie')