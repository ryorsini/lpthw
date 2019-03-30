## Animal is a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Class dog that is an Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has a name
        self.name = name

# Class cat is an Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has a name
        self.name = name

# Person is an object
class Person(object):

    def __init__(self, name):
        ## Person has a name
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

##  class Employee that is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## Employee has a salary
        self.salary = salary

## Fish is an object
class Fish(object):
    pass

## Salmon is a fish
class Salmon(Fish):
    pass

## Halibut is a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## Mary is-a person
mary = Person("Mary")

## From Mary, get the pet attribute and set it equal to Satan
mary.pet = satan

## Set Frank to an instance of class Employee
frank = Employee("Frank", 120000)

## From frank, get the pet attribute and set it to Rover
frank.pet = rover

## Set flipper to an instance of class Fish
flipper = Fish()

## Set crouse to an instance of class Salmon
crouse = Salmon()

## Set harry to an instance of class Halibut
harry = Halibut()
