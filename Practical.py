import math
r = 50
print(f"A circle with radius {r} has an area of {math.pi * r * r}")
if __name__ == '__main__':
    width = 104.32
    height = 15.654
    space = width * height
    print(f"The area of a rectangle with a width of {width} and a height of {height} is {space}")
if __name__ == '__main__':
    import math

    r = 50
    print(f"A circle with radius {r} has an area of {math.pi * r * r:.3f}")
if __name__ == '__main__':
    name = "ali"
    age = 10

    print(f"name: {name:10}-   age: {age:3}")
if __name__ == '__main__':
    name = "ali"
    age = 10
    print(f"name: {name:$>20}   -   age: {age:$>20.2f}")
if __name__ == '__main__':
    import math

    r = 52
    print("A circle with radius {r} has an area of {area:}".format(r=r, area=math.pi * r * r))
if __name__ == '__main__':
    name = "ali"
    age = 15

    print("{name:@^15} - {age:#^10}".format(name=name, age=age))
if __name__ == '__main__':
    with open("info.txt", "r") as file:
        for line in file:
            print(line.strip())