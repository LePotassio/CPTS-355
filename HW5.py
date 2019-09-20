#Eric Furukawa
#11580506
#CPTS 355
#Assignment 5


tupleDict = {}

#------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations
opstack = []  #assuming top of the stack is the end of the list

# Now define the helper functions to push and pop values on the opstack (i.e, add/remove elements to/from the end of the Python list)
# Remember that there is a Postscript operator called "pop" so we choose different names for these functions.
# Recall that `pass` in python is a no-op: replace it with your code.


#Switch beween DYNAMIC 0 and STATIC 1
mode = 0

import re
def tokenize(s):
    return re.findall("/?[a-zA-Z()][a-zA-Z0-9_()]*|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)


def opPop():
    if len(opstack) > 0:
        return opstack.pop()
    else:
        print ("Pop empty list error")
    # opPop should return the popped value.
    # The pop() function should call opPop to pop the top value from the opstack, but it will ignore the popped value.

def opPush(value):
    opstack.append(value)

#-------------------------- 20% -------------------------------------
# The dictionary stack: define the dictionary stack and its operations
dictstack = []  #assuming top of the stack is the end of the list

# now define functions to push and pop dictionaries on the dictstack, to define name, and to lookup a name

def dictPop():
    if len(dictstack) > 0:
        return dictstack.pop()
    else:
        print ("Pop empty list error")
    # dictPop pops the top dictionary from the dictionary stack.

def dictPush(d):
    dictstack.append(d)
    #dictPush pushes the dictionary ‘d’ to the dictstack. Note that, your interpreter will call dictPush only when Postscript “begin” operator is called. “begin” should pop the empty dictionary from the opstack and push it onto the dictstack by calling dictPush.

def define(name, value):
    if len(dictstack) == 0:
        dictPush({})
    dictstack[-1][name] = value

    #add name:value pair to the top dictionary in the dictionary stack. Keep the '/' in the name constant.
    # Your psDef function should pop the name and value from operand stack and call the “define” function.

def lookup(name):
    for element in reversed(dictstack):#now looks through dictstack starting from top (end)
        for (p1,p2) in element.items():
            if "/" + name == p1:
                return p2
            elif name == p1:
                return p2
    #print ("lookup error, value not found")

    # return the value associated with name
    # What is your design decision about what to do when there is no definition for “name”? If “name” is not defined, your program should not break, but should give an appropriate error message.

#--------------------------- 10% -------------------------------------
# Arithmetic and comparison operators: add, sub, mul, div, mod, eq, lt, gt
#Make sure to check the operand stack has the correct number of parameters and types of the parameters are correct.

def add():#pop two values and add, then push back, remember error checking
    if len(opstack) > 1:
        var1 = opPop()
        var2 = opPop()
        if type(var1) is int and type(var2) is int:
            opPush(var1+var2)
        else:
            print ("Operation type error")
            opPush(var2)
            opPush(var1)
    else:
        print ("Operation length error")

def sub():
    if len(opstack) > 1:
        var2 = opPop()
        var1 = opPop()
        if type(var1) is int and type(var2) is int:
            opPush(var1 - var2)
            #print(var1 - var2)
        else:
            print ("Operation type error")
            opPush(var1)
            opPush(var2)
    else:
        print ("Operation length error")

def mul():
    if len(opstack) > 1:
        var1 = opPop()
        var2 = opPop()
        if type(var1) is int and type(var2) is int:
            opPush(var1 * var2)
        else:
            print ("Operation type error")
            opPush(var2)
            opPush(var1)
    else:
        print ("Operation length error")

def div():
    if len(opstack) > 1:
        var2 = opPop()
        var1 = opPop()
        if type(var1) is int and type(var2) is int:
            if(var2 != 0):
                opPush(var1 / var2)
            else:
                print("Divide by zero error")
                opPush(var1)
                opPush(var2)
        else:
            print ("Operation type error")
            opPush(var1)
            opPush(var2)
    else:
        print ("Operation length error")

def mod():
    if len(opstack) > 1:
        var2 = opPop()
        var1 = opPop()
        if type(var1) is int and type(var2) is int:
            opPush(var1 % var2)
        else:
            print ("Operation type error")
            opPush(var1)
            opPush(var2)
    else:
        print ("Operation length error")

def eq():
    if len(opstack) > 1:
        #stack()
        var1 = opPop()
        var2 = opPop()
        #print(var1)
        #print(var2)
        if (type(var1) is int and type(var2) is int) or (type(var1) is str and type(var2) is str): #compares str now
            opPush(var1 == var2)
        else:
            print ("Operation type error")
            opPush(var2)
            opPush(var1)
    else:
        print ("Operation length error")

def lt():
    if len(opstack) > 1:
        var2 = opPop()
        var1 = opPop()
        if type(var1) is int and type(var2) is int:
            opPush(var1 < var2)
            #print(var1)
            #print(var2)
            #print(var1 < var2)
        else:
            print ("Operation type error")
            opPush(var1)
            opPush(var2)
    else:
        print ("Operation length error")

def gt():
    if len(opstack) > 1:
        var2 = opPop()
        var1 = opPop()
        if type(var1) is int and type(var2) is int:
            opPush(var1 > var2)
        else:
            print ("Operation type error")
            opPush(var1)
            opPush(var2)
    else:
        print ("Operation length error")

#--------------------------- 15% -------------------------------------
# String operators: define the string operators length, get, getinterval, put
def length():
    popped = opPop()
    if type(popped) is str:
        opPush(len(popped) - 2) #accounts for ()
    else:
        print ("Length not string error")
        opPush(popped)

def get():
    poppedI = opPop()
    poppedS = opPop()
    if type(poppedI) is int and type(poppedS) is str:
        opPush(ord(poppedS[poppedI + 1]))#ord used to convert to ASCII
    else:
        print ("Get not int/string error")
        opPush(poppedS)
        opPush(poppedI)

def getinterval():
    poppedI1 = opPop()
    poppedI2 = opPop()
    poppedS = opPop()
    #print("**" + str(poppedI1) + "**" + str(poppedI2) + "**" + str(poppedS) + "**")
    if type(poppedI1) is int and type(poppedI2) is int and type(poppedS) is str:
        #print(poppedS[poppedI2:(poppedI1 + poppedI2)])
        opPush("(" + poppedS[poppedI2 + 1:(poppedI1 + poppedI2 + 1)] + ")") #now account for parentheses
    else:
        print("GetInterval not int/int/string error")
        opPush(poppedS)
        opPush(poppedI2)
        opPush(poppedI1)

def put():#replaces an element of the string with given char, use dup to
    poppedC = opPop()
    poppedI = opPop() + 1
    poppedS = opPop()
    #print(hex(id(poppedS)))
    result = ""
    if type(poppedC) is int and type(poppedI) is int and type(poppedS) is str:
        for i in range(len(poppedS)):
            if i == poppedI:
                result += chr(poppedC)
            else:
                result += poppedS[i]
        #opPush(result)#couldn't find out how to do with dup reference as changing the string changed the reference
        #result = Cpts350

        #PT 2: all copies of the same string (i.e., the strings that have
        #the same object-id) in the opstack and the dictstack should be updated

        for element in range(len(opstack)):
            if id(opstack[element]) == id(poppedS):
                #print("reached")
                opstack[element] = result
                #print(result)
                #stack()

        for element in dictstack:
            for (p1, p2) in element.items():
                if id(p2) == id(poppedS):
                    element[p1] = result
                    #print(p2)


    else:
        print("Put error not int/int/string")
        opPush(poppedS)
        opPush(poppedI)
        opPush(poppedC)

#--------------------------- 25% -------------------------------------
# Define the stack manipulation and print operators: dup, copy, pop, clear, exch, roll, stack
def dup():#changes operand stack content
    if len(opstack) > 0:
        opPush(opstack[-1])
    else:
        print ("dup Error")

def copy():#error coverage? and
    poppedN = opPop()
    tbPushed = []
    for element in range(poppedN):
        tbPushed.append(opstack[-1 - element])
    tbPushed.reverse()
    for element in tbPushed:
        opPush(element)

def pop():
    opPop()

def clear():
    del opstack[:]
    del dictstack[:]

def exch():
    if len(opstack) >= 2 :
        poppedFirst = opPop()
        poppedSecond = opPop()
        opPush(poppedFirst)
        opPush((poppedSecond))
    else:
        print ("Exchange error")

def stack():
    revstack = reversed(opstack)
    for element in revstack:
        print (element)

def roll():
    timesRoll = opPop()#-2
    topRange = opPop()#4

    if timesRoll > 0:
        while timesRoll != 0:
            timesRoll = timesRoll - 1
            temp = opstack[-1]
            for element in range(1,topRange):
                opstack[-element] = opstack[-element - 1]
            opstack[-topRange] = temp


    if timesRoll < 0:
        while timesRoll != 0:#2 times
            temp = opstack[-topRange]
            timesRoll = timesRoll + 1
            for element in range(1,topRange):#1-3
                opstack[-topRange + element - 1] = opstack[-topRange + element]
            opstack[-1] = temp
    #print("****")
    #stack()
    #print("****")

#--------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in Python. Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and call your own "define" operator (pass those values as parameters).
# Note that psDef()won't have any parameters.

def psDef():
    value = opPop()
    name = opPop()
    if name[0] == "/":
        define(name,value)
    else:
        opPush(name)
        opPush(value)

def psIf():
    codeList = opPop()
    statement = opPop()
    if type(codeList) is list and statement == True:
        interpretSPS(codeList, mode)
    else:
        opPush(statement)
        opPush(codeList)

def psIfelse():
    codeList2 = opPop()
    codeList1 = opPop()
    statement = opPop()
    #print(statement)
    if type(codeList1) is list and type(codeList2) is list:
        if statement:
            interpretSPS(codeList1, mode)
        else:
            #print(codeList2)
            interpretSPS(codeList2, mode)
    else:
        opPush(statement2)
        opPush(codeList2)
        opPush(codeList1)
def psFor():
    conditional = opPop()
    ender = opPop()
    increment = opPop()
    starter = opPop()
    if increment > 0:
        for i in range(starter,ender+1,increment):
            opPush(i)
            interpretSPS(conditional, mode)
    elif increment < 0:
        for i in range(starter,ender-1,increment):
            opPush(i)
            interpretSPS(conditional, mode)
    else:
        opPush(starter)
        opPush(increment)
        opPush(ender)
        opPush(conditional)

#####################################################################################

def isInt(c):
    try:
        int(c)
        return True
    except:
        return False

# The it argument is an iterator.
# The sequence of return characters should represent a list of properly nested
# tokens, where the tokens between '{' and '}' is included as a sublist. If the
# parentheses in the input iterator is not properly nested, returns False.
def groupMatching2(it):
    res = []
    for c in it:
        if c == '}':
            return res
        elif c=='{':
            # Note how we use a recursive call to group the tokens inside the
            # inner matching parenthesis.
            # Once the recursive call returns the code-array for the inner
            # parenthesis, it will be appended to the list we are constructing
            # as a whole.
            res.append(groupMatching2(it))
        else:
            if c == "true":
                res.append(True)
            elif c == "false":
                res.append(False)
            elif isInt(c):
                res.append(int(c))
            else:
                res.append(c)
    return False
# Function to parse a list of tokens and arrange the tokens between { and } braces
# as code-arrays.
# Properly nested parentheses are arranged into a list of properly nested lists.
def parse(L):
    res = []
    it = iter(L)
    for c in it:
        if c=='}': #non matching closing parenthesis; return false since there is
                    # a syntax error in the Postscript code.
            return False
        elif c=='{':
            res.append(groupMatching2(it))
        else:
            if c == "true":
                res.append(True)
            elif c == "false":
                res.append(False)
            elif isInt(c):
                res.append(int(c))
            else:
                res.append(c)
    return res


opDictionary = {"add":add,"sub":sub,"mul":mul,"div":div,"mod":mod,"gt":gt,"lt":lt,"eq":eq,"length":length,"get":get,"getinterval":getinterval,"put":put,"dup":dup,"copy":copy,"exch":exch,"roll":roll,"stack":stack,"clear":clear,"def":psDef,"if":psIf,"ifelse":psIfelse,"for":psFor,"pop":pop}
# Write the necessary code here; again write
# auxiliary functions if you need them. This will probably be the largest
# function of the whole project, but it will have a very regular and obvious
# structure if you've followed the plan of the assignment.

def interpretSPS(code, scope):  # code is a code-array
    for c in code:
        if type(c) is int:
            opPush(c)
        elif type(c) is bool:
            opPush(c)
        elif type(c) is list:
            opPush(c)
        elif c in opDictionary.keys():
            opDictionary[c]()
        elif type(c) is str:
            if c[0] == "/":
                opPush(c)
            else:
                var = lookup(c)
                if var == None:
                    opPush(c)
                elif type(var) is list:
                    interpretSPS(var, scope)
                else:
                    opPush(var)

# Copy this to your HW4_part2.py file>
def interpreter(s, scope):  # s is a string
    interpretSPS(parse(tokenize(s)), scope)



inputTest1 = """/x 4 def
        /g { x stack } def
        /f { /x 7 def g } def
        f"""


print("Test 1:")
clear()
interpreter(inputTest1, 0)




#Added scope parameter and mode variable
#Removed begin end and psdict
#Removed previous assignment tests