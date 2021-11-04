players = ['charles','martin','michael','florence','eli']
print(players[1:4])
print(players[:4])
print(players[1:])
print(players[-3:])

for player in players[:3]:
    print(player.title())

# copy list
my_foods = ['pizza','falafel','carrot']
friend_foods = my_foods[:]
print(friend_foods)
my_foods.append('ice')
friend_foods.append('tea')
print(my_foods)
print(friend_foods)

# diffs
my_foods = ['pizza','falafel','carrot']
friend_foods = my_foods
print(friend_foods)
my_foods.append('ice')
friend_foods.append('tea')
print(my_foods)
print(friend_foods)

