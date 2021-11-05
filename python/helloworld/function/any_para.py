def make_pizza(*toppings):
    """print toppings"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms','green pepper')

def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")
make_pizza('pepperoni')
make_pizza('mushrooms','green pepper')

def build_profile(first,last,**user_info):
    """create a dictionary of user information"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)