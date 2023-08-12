# Classes

class Dog():
    """ Simple dog model"""

    def __init__(self, name, age, color):
        """Attributes initialization, name, age and color"""
        self.name = name
        self.age = age
        self.color = color
        print('Dog created')

    def seat(self):
        """Dog seats"""
        print(self.name.title() + ', Dog sat .')

    def jump(self):
        """Dog jumps"""
        print(self.name.title() + ', Dog jumped .')

    def bark(self):
        """Dog barks"""
        print(self.name.title() + ', Dog barked .')

topic = Dog('Topic', 4, 'Brown')
chinese = Dog('Chinese', 2, 'Yellow')
poppy = Dog('Poppy', 1, 'White')
print('The name is: ', topic.name, ';','Topic age is: ', topic.age, ';','Color is: ', topic.color, '.')
print('The name is: ', chinese.name, ';','Chinese age is: ', chinese.age, ';','Color is: ', chinese.color, '.')
print('The name is: ', poppy.name, ';','Poppy age is: ', poppy.age, ';','Color is: ', poppy.color, '.')
topic.jump()
chinese.seat()
poppy.jump()
poppy.bark()







