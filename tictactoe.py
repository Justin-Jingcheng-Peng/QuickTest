
# f = open("test1.in", "w+")

# f.close()


# Test all valid moves and either side wins
import random
matrix = [["o", "o", "x"],
          ["x", "o", None],
          [None, None, "o"]]
names = []


def printMatrix():
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j])
        print()


def init():
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = None


def end():
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != None:
                count += 1
    if count == 9:
        return True

    for each in matrix:
        if each.count("x") == 3 or each.count("o") == 3:
            return True
    for c in range(len(matrix)):
        temp = []
        for r in range(len(matrix[0])):
            temp.append(matrix[r][c])
        if temp.count("x") == 3 or temp.count("o") == 3:
            return True

    temp = []
    for i in range(len(matrix)):
        temp.append(matrix[i][i])
    if temp.count("x") == 3 or temp.count("o") == 3:
        return True
    temp = []
    for i in range(len(matrix)):
        temp.append(matrix[i][2-i])
    if temp.count("x") == 3 or temp.count("o") == 3:
        return True

    return False


def testIn(start_, end_):
    for i in range(start_, end_+1):
        fileName = "test" + str(i) + ".in"
        nameToSuite = "test" + str(i)
        names.append(nameToSuite)
        curFile = open(fileName, "w+")
        turn = "x"
        init()
        while True:
            r = random.randint(0, 2)
            c = random.randint(0, 2)
            while matrix[r][c] != None:
                r = random.randint(0, 2)
                c = random.randint(0, 2)
            if matrix[r][c] == None:
                line = turn + " " + str(r) + " " + str(c) + "\n"
                curFile.write(line)
                matrix[r][c] = turn
                if turn == "x":
                    turn = "o"
                else:
                    turn = "x"
                if end() == True:
                    curFile.close()
                    break


def testInAndArgs(start_, end_):
    for i in range(start_, end_+1):
        fileName = "test" + str(i) + ".in"
        fileName2 = "test" + str(i) + ".args"
        curFile = open(fileName, "w+")
        curFile2 = open(fileName2, "w+")
        nameToSuite = "test" + str(i)
        names.append(nameToSuite)
        turn = "x"
        init()
        while True:
            r = random.randint(0, 2)
            c = random.randint(0, 2)
            while matrix[r][c] != None:
                r = random.randint(0, 2)
                c = random.randint(0, 2)
            if matrix[r][c] == None:
                line = turn + " " + str(r) + " " + str(c) + "\n"
                curFile.write(line)
                curFile2.write(line)
                matrix[r][c] = turn
                if turn == "x":
                    turn = "o"
                else:
                    turn = "x"
                if end() == True:
                    curFile.close()
                    curFile2.close()
                    break


def onlyArgs(start_, end_):
    for i in range(start_, end_+1):
        fileName2 = "test" + str(i) + ".args"
        curFile2 = open(fileName2, "w+")
        turn = "x"
        init()
        nameToSuite = "test" + str(i)
        names.append(nameToSuite)
        while True:
            r = random.randint(0, 2)
            c = random.randint(0, 2)
            while matrix[r][c] != None:
                r = random.randint(0, 2)
                c = random.randint(0, 2)
            if matrix[r][c] == None:
                line = turn + " " + str(r) + " " + str(c) + "\n"
                curFile2.write(line)
                matrix[r][c] = turn
                if turn == "x":
                    turn = "o"
                else:
                    turn = "x"
                if end() == True:
                    curFile2.close()
                    break


testIn(1, 30)
testInAndArgs(33, 34)

suiteFile = open("suiteq3.txt", "w+")
for name in names:
    suiteFile.write(name + "\n")
