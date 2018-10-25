from project import *
import time

b1 = [["_","O","O","O","_"],
["O","_","O","_","O"],
["_","O","_","O","_"],
["O","_","O","_","_"],
["_","O","_","_","_"]]

'''b1 = [["O","O","O","X"],
["O","O","O","O"],
["O","_","O","O"],
["O","O","O","O"]]'''

'''b1 = [["O","O","O","X","X"],
["O","O","O","O","O"],
["O","_","O","_","O"],
["O","O","O","O","O"]] '''

'''b1 = [["O","O","O","X","X","X"],
["O","_","O","O","O","O"],
["O","O","O","O","O","O"],
["O","O","O","O","O","O"]]'''

startTime = time.time()
sol1 = solitaire(b1)
p1 = InstrumentedProblem(sol1)

greedy_search(p1)
endTime = time.time()
finalTime = endTime - startTime
print(finalTime)
