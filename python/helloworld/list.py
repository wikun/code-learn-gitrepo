bicycles = ["trek","cannondale","redline","specialized"]
print(bicycles)

print(bicycles[0])
print(bicycles[-1])
message = f"my first bicycle was a {bicycles[-2].title()}"
print(message)

motorcycles = ["honda","yamaha","suzuki"]
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

motorcycles = []
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0,'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

