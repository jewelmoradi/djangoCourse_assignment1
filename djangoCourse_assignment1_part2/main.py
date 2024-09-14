# assignment 1
# part 2: Person class

class Person:

    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def age_changer(self, new_age):
        self.age = new_age


lines = []

for i in range(2):
    line = input()
    lines.append(line)

information = lines[0].split()

if len(information) == 1:
    person = Person(information[0])
elif len(information) == 2:
    person = Person(information[0], int(information[1]))
else:
    print('invalid number of arguments!')
    quit()

person.age_changer(int(lines[1]))
print(f'name: {person.name}, age: {person.age}')
