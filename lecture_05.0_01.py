print("Lecture  5 part 1 2023 03/25")
# OOП

class Dog:
    biology_class = 'Animal'
    def __init__(self, name, weight, color):
        self.name = name       # public
        self._color = color    # private
        self.__weight = weight # protected

    def run(self):
        return 'I can run'

    def get_name(self):
        return f'Hello, I am {self.name}'

    def set_name(self, name):
        self.name = name

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

# dog = Dog('Bobik', 3, 'black')
# print(dog.run())
# print(dog.name)
# print(dog.get_name())
# # I can run!
# # Bobik
# # Hello, I am Bobik
#
# def change_dog():
#     dog.name = 'Sharik'
#
# change_dog()
# print(dog.name)
# # Sharik
# print(dog.biology_class)
# # Animal
#
# dog.biology_class = 'Bird'
# print(dog.biology_class)
# # Bird

class PitBull(Dog):
    def __init__(self, name, weight, color, passport):
        super().__init__(name, weight, color)
        self.passport = passport

    def run(self):
        return  super().run() + ' fast'

dog3 = PitBull('Bobik', 3, 'black', True)
print(dog3.passport)
# True

print(dog3.run())
# I can run fast

print(dog3.__dict__)
# {'name': 'Bobik', '_Dog__weight': 3, '_color': 'black', 'passport': True}

dog3.set_name('Charlik')
print(dog3.get_name())
# Hello, I am Charlik

dog3._color = 'white' # No error
# dog3.set_color('white')
print(dog3.get_color())
# white

dog3.__weight = 10
print(dog3.__weight) # 10
print(dog3._Dog__weight) # 3
dog3.aaa = 15
print(dog3.aaa) # 15
