import faker
from faker import Faker
from random import *
from time import process_time


faker = Faker(['ru-RU'])
segmentCount = 6


def fill(dictionary, count):
    for i in range(count):
        tempD = {'key': i, 'infor': "Name: {}, Adress: {}".format(faker.name(), faker.simple_profile())}
        dictionary.append(tempD)
    
    return dictionary


def bruteAlgorithm(dictionary, key):
    for item in dictionary:
       if item['key'] == key:
            return item

    return None

def binaryAlgorithm(dictionary, key):
    Left = 0
    Right = len(dictionary) - 1
    mid = (Left + Right) // 2

    if dictionary[Left]['key'] > key:
        return None
    elif dictionary[Left]['key'] == key:
        return dictionary[Left]

    if dictionary[Right]['key'] < key:
        return None
    elif dictionary[Right]['key'] == key:
        return dictionary[Right] 

    # Поиск от среднего значения
    tmp = dictionary[mid]['key']

    while key != tmp and Left < Right:
        if key < tmp:
            Right = mid
        else:
            Left = mid

        mid = (Left + Right) // 2
        tmp = dictionary[mid]['key']

    return dictionary[mid]


def func(x):
    return x % 10

def prepareSegment(dictionary):
    chance = [[] for i in range(10)]

    for i in range(len(dictionary)):
        chance[func(dictionary[i]['key'])].append(dictionary[i])
    
    return chance


def segment(chance, key):
    segment = chance[func(key)]
    return binaryAlgorithm(segment, key)


def doTimeTest(size, repeat):
    dictionary = []
    chance = []
    key = 0

    dictionary = fill(dictionary, size)

    t1 = process_time()
    for i in range(repeat):
        bruteAlgorithm(dictionary, key)
        key += 1
    t2 = process_time()

    print("Time for brute -\t", (t2 - t1) / repeat)

    key = 0

    t1 = process_time()
    for i in range(repeat):
        binaryAlgorithm(dictionary, key)
        key += 1
    t2 = process_time()

    print("Time for binary -\t", (t2 - t1) / repeat)


    key = 0

    t1 = process_time()
    chance = prepareSegment(dictionary)
    for i in range(repeat):
        segment(chance, key)
        key += 1
    t2 = process_time()

    print("Time for segment -\t", (t2 - t1) / repeat)


if __name__ == "__main__":
    dictionary = []
    chance = []
 
    length = 10

    dictionary = fill(dictionary, length)

    while True:
        print("[1] - Brute")
        print("[2] - Binary")
        print("[3] - Segment")
        print("[4] - Time test")
        print("[0] - Exit")

        c = int(input("Choice - "))

        if c == 1:
            key = int(input("Input key: "))
            print(bruteAlgorithm(dictionary, key))
        elif c == 2:
            key = int(input("Input key: "))
            print(binaryAlgorithm(dictionary, key))
        elif c == 3:
            chance = prepareSegment(dictionary)

            key = int(input("Input key: "))
            print(segment(chance, key))
        elif c == 4:
            sizes = [100, 1000, 10000, 100000]
            repeats = [100, 100, 100, 100]

            for i in range(len(sizes)):
                print("\n", sizes[i], 100000)
                doTimeTest(sizes[i], 1000)
        else:
            break
