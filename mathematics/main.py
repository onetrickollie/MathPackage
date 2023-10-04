# mathematics/main.py
from .numbers import *
from .geometry import *

if __name__ == "__main__":
    print("Testing mathematics package:")
    
    # Testing whoami modules
    print("mathematics whoami:", mathematics.whoami.getname())
    print("numbers whoami:", numbers.whoami.getname())
    print("geometry whoami:", geometry.whoami.getname())

    # Testing series module
    num_list = [1, 2, 3, 4, 5]
    print("Sum:", numbers.series.sum(num_list))
    print("Average:", numbers.series.average(num_list))

    # Testing simple module
    print("Addition:", numbers.simple.addition(5, 3))
    print("Subtraction:", numbers.simple.subtraction(5, 3))
    print("Multiplication:", numbers.simple.multiplication(5, 3))
    print("Division:", numbers.simple.division(5, 3))

    # Testing geometry modules
    print("Circle Circumference:", geometry.circle.circumference(5))
    print("Circle Area:", geometry.circle.area(5))
    print("Cube Surface Area:", geometry.cube.surface_area(4))
    print("Cube Volume:", geometry.cube.volume(4))
