
#Eric Furukawa
#HW Assignment 3

#Discussed implementation concepts with Osman Bakari
#Discussed implementation on problems 4 and __next__ on 6 with Jimmy Zheng

debugging = False
def debug(*s):
    if debugging:
        print(*s)

#Problem 1 busStops

#imported libraries
from functools import reduce
from itertools import combinations

def busStops(b):
    newDict = {}
    for route,stops in b.items():
        for bstop in stops:
            newDict.setdefault(bstop,[]).append(route)
    for routes in newDict.values():
        routes.sort()
    return newDict

def testbusStops():
    buses = {
        "Lentil": ["Chinook", "Orchard", "Valley", "Emerald", "Providence",
                   "Stadium", "Main", "Arbor", "Sunnyside", "Fountain", "Crestview",
                   "Wheatland", "Walmart", "Bishop", "Derby", "Dilke"],
        "Wheat": ["Chinook", "Orchard", "Valley", "Maple", "Aspen", "TerreView",
                  "Clay", "Dismores", "Martin", "Bishop", "Walmart", "PorchLight",
                  "Campus"],
        "Silver": ["TransferStation", "PorchLight", "Stadium",
                   "Bishop", "Walmart", "Shopco", "RockeyWay"],
        "Blue": ["TransferStation", "State", "Larry", "TerreView", "Grand",
                 "TacoBell", "Chinook", "Library"],
        "Gray": ["TransferStation", "Wawawai", "Main", "Sunnyside", "Crestview",
                 "CityHall", "Stadium", "Colorado"]
    }
    if busStops(buses) != ({'Chinook': ['Blue', 'Lentil', 'Wheat'], 'Orchard': ['Lentil',
'Wheat'], 'Valley': ['Lentil', 'Wheat'], 'Emerald': ['Lentil'],
'Providence': ['Lentil'], 'Stadium': ['Gray', 'Lentil', 'Silver'],
'Main': ['Gray', 'Lentil'], 'Arbor': ['Lentil'], 'Sunnyside': ['Gray',
'Lentil'], 'Fountain': ['Lentil'], 'Crestview': ['Gray', 'Lentil'],
'Wheatland': ['Lentil'], 'Walmart': ['Lentil', 'Silver', 'Wheat'],
'Bishop': ['Lentil', 'Silver', 'Wheat'], 'Derby': ['Lentil'], 'Dilke':
['Lentil'], 'Maple': ['Wheat'], 'Aspen': ['Wheat'], 'TerreView':
['Blue', 'Wheat'], 'Clay': ['Wheat'], 'Dismores': ['Wheat'], 'Martin':
['Wheat'], 'PorchLight': ['Silver', 'Wheat'], 'Campus': ['Wheat'],
'TransferStation': ['Blue', 'Gray', 'Silver'], 'Shopco': ['Silver'],
'RockeyWay': ['Silver'], 'State': ['Blue'], 'Larry': ['Blue'], 'Grand':
['Blue'], 'TacoBell': ['Blue'], 'Library': ['Blue'], 'Wawawai':
['Gray'], 'CityHall': ['Gray'], 'Colorado': ['Gray']}) :
        return False

    myBuses = {
        "A": ["Seattle", "Las Vegas"],
        "B": ["Waikiki","Tokyo"],
        "C": ["Tokyo"],
        "D": [],
        "E": ["Orlando", "Seaside", "San Francisco", "Seattle"]
    }

    if busStops(myBuses) != {'Seattle': ['A', 'E'], 'Las Vegas': ['A'], 'Waikiki': ['B'], 'Tokyo': ['B', 'C'], 'Orlando': ['E'], 'Seaside': ['E'], 'San Francisco': ['E']}:
        return false

    return True

#testbusStops()


#Problem 2 (Dictionaries)

#a. addDict
def addDict(d):
    newDict = {}
    for day,courses in d.items():
        for course,hours in courses.items():
            newDict[course] = newDict.get(course,0) + hours
    return newDict

def testaddDict():
    record = {'Mon': {'355': 2, '451': 1, '360': 2}, 'Tue': {'451': 2, '360': 3},
     'Thu': {'355': 3, '451': 2, '360': 3}, 'Fri': {'355': 2},
     'Sun': {'355': 1, '451': 3, '360': 1}}
    if addDict(record) != {'355': 8, '451': 8, '360': 9}:
        return False

    myRecord = {'Mon': {'9001': 3}, 'BUNS': {'355': 2, '355': 3}, 'Fri': {'355': 2}, 'Sun': {'355': 1, '9001': 1}}
    if addDict(myRecord) != {'9001': 4, '355': 6}:
        return False

    return True

#testaddDict()

#b. addDictN
def addDictN(L):
    def addDictNHelper(d1,d2):
        for course,hours in d1.items():
            if course in d2:
                d2[course] = hours + d2[course] #could forego the conditional using d2.get(course,0)
            else:
                d2[course] = hours
        return d2
    return reduce(addDictNHelper,list(map(addDict,L)))


def testaddDictN():
    listerino = [{'Mon':{'355':2,'360':2},'Tue':{'451':2,'360':3},'Thu':{'360':3},
'Fri':{'355':2}, 'Sun':{'355':1}},
{'Tue':{'360':2},'Wed':{'355':2},'Fri':{'360':3, '355':1}},
{'Mon':{'360':5},'Wed':{'451':4},'Thu':{'355':3},'Fri':{'360':6},
'Sun':{'355':5}}]
    if addDictN(listerino) != {'360': 24, '451': 6, '355': 16}:
        return False

    myListerino = [{'A': {'111': 2, '222': 2}, 'B': {'333': 2, '444': 3}, 'C': {'555': 3},
                  'D': {'666': 2}, 'E': {'777': 1}},
                 {},
                 {'A': {'': 5}, 'B': {'': 4}, 'D': {'': 3}, 'F': {'': 6},
                  'Z': {'': 5}}]
    if addDictN(myListerino) != {'': 23, '111': 2, '222': 2, '333': 2, '444': 3, '555': 3, '666': 2, '777': 1}:
        return False

    return True

#testaddDictN()


#Problem 3 Dictionaries and Lists

#a. searchDicts

def searchDicts(L,k):
    for dict in reversed(L):
        for key,value in dict.items():
            if k == key:
                return value
    return None

def testsearchDicts():
    L1 = [{"x": 1, "y": True, "z": "found"}, {"x": 2}, {"y": False}]
    if searchDicts(L1,"x") != 2 or searchDicts(L1,"y") != False or searchDicts(L1,"z") != "found" or searchDicts(L1,"t") != None:
        return False

    L3 = [{"x": False, "y": True, "x": "Beta"}, {"x": "Right"}, {"xx": "Double"}]
    if searchDicts(L3, "x") != "Right":
        return False

    return True

#testsearchDicts()

#b. searchDicts2

def searchDicts2(L,k):
    def searchDicts2Helper(t,last):
        if k in t[1]:
            return t[1][k]
        if t[0] == last:
            return None
        return searchDicts2Helper(L[t[0]],t[0])
    return searchDicts2Helper(L[-1],-1) #312

def testsearchDicts2():
    L2 = [(0, {"x": 0, "y": True, "z": "zero"}),
          (0, {"x": 1}),
          (1, {"y": False}),
          (1, {"x": 3, "z": "three"}),
          (2, {})]
    if searchDicts2(L2,"x") != 1 or searchDicts2(L2,"y") != False or searchDicts2(L2,"z") != "zero" or searchDicts2(L2,"t") != None:
        return False

    L4 = [(0, {"x": 0, "y": True, "z": "zero"}), #all 0 case
          (0, {"x": 1}),
          (0, {"y": False}),
          (0, {"x": 3, "z": "three"}),
          (0, {})]
    if searchDicts2(L4, "x") != 0:
        return False

    return True

#testsearchDicts2()#this works given the condition the left tuples are sorted ascending down, to avoid loops

#Problem 4 subsets
#
def subsets(L):
    return sum([list(map(list, combinations(L, element))) for element in range(len(L) + 1)], [])

def testsubsets():
    if subsets([1,2,3]) != [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]] or subsets([(1,"one"),(2,"two")]) != [[],[(1,"one")],[(2,"two")],[(1,"one"),(2,"two")]] or subsets([]) != [[]]:
        return False
    if subsets(["A",2,True]) != [[], ['A'], [2], [True], ['A', 2], ['A', True], [2, True], ['A', 2, True]]: #difft type test
        return False
    return True

testsubsets()

#Problem 5 numPaths

def numPaths(m,n):#recursive
    if(m == 1 or n == 1):
        return 1
    return numPaths(m-1,n) + numPaths (m,n-1)

def testnumPaths():
    if numPaths(2,2) != 2 or numPaths (3,3) != 6 or numPaths(4,5) != 35:
        return False

    if numPaths(1,1) != 1 or numPaths (9999,1) != 1 or numPaths(1,9999) != 1:
        return False

    return True

#testnumPaths()

#Problem 6 Iterators

#a. iterprimes

def isPrime(num): #Helper to determine if prime
    for i in range(2, num):
        if (num) % i == 0:
            return False
    return True

def primeRec(num): #Helper to find next prime
    if isPrime(num+1):
        return num+1
    else:
        return primeRec(num+1)

def primeRecREV(num): #Helper to find previous prime, doesnt need to account for going into negatives
    if isPrime(num-1):
        return num-1
    else:
        return primeRecREV(num-1)

class iterPrimes():
    def __init__(self):
        self.current = 1
    def __next__(self):
        self.current = primeRec(self.current)
        return self.current
    def __prev__(self):
        self.current = primeRecREV(self.current)
        return self.current

    def __iter__(self):
        return self

#b. numbersToSum
def numbersToSum(iNumbers,sum):
    result = []
    resultInt = 0
    item = iNumbers.__next__()
    while item + resultInt < sum:
        result.append(item)
        resultInt = resultInt + item
        item = iNumbers.__next__()
    iNumbers.__prev__()
    return result

def testnumbersToSum():
    primes = iterPrimes()
    if numbersToSum(primes,58) != [2,3,5,7,11,13] or numbersToSum(primes,100) != [17,19,23,29]:
        return False

    primes = iterPrimes()
    if numbersToSum(primes, 2) != [] or numbersToSum(primes, 0) != [] or numbersToSum(primes, 3) != [2]:
        return False

    return True

#testnumbersToSum()

#"subsets":testsubsets

testFunctions = {"busStops":testbusStops, "addDict": testaddDict,
"addDictN": testaddDictN, "searchDicts": testsearchDicts, "searchDicts2":
testsearchDicts2, "subsets":testsubsets, "numPaths": testnumPaths,
"numbersToSum":testnumbersToSum }
if __name__ == '__main__':
    for testName,testFunc in testFunctions.items():
        print(testName,': ',testFunc())
        print('---------------------')