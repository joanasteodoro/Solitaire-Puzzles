from project import *


'''b1 = [["_","O","O","O","_"],
["O","_","O","_","O"],
["_","O","_","O","_"],
["O","_","O","_","_"],
["_","O","_","_","_"]]
'''

'''b1 = [["O","O","O","X"],
["O","O","O","O"],
["O","_","O","O"],
["O","O","O","O"]]'''

'''b1 = [["O","O","O","X","X"],
["O","O","O","O","O"],
["O","_","O","_","O"],
["O","O","O","O","O"]] '''

b1 = [["O","O","O","X","X","X"],
["O","_","O","O","O","O"],
["O","O","O","O","O","O"],
["O","O","O","O","O","O"]]

sol1 = solitaire(b1)
p1 = InstrumentedProblem(sol1)

print(depth_first_tree_search(p1))
print(p1)
