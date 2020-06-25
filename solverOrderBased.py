from os import popen

SUGAR_CMD = "sugar"

def _solve(systemConstraints, entityConstraints):
    outFile = open("temp.csp", "w")
    for constraint in systemConstraints + entityConstraints:
        outFile.write(constraint + "\n")
    outFile.close()
    command = SUGAR_CMD + " temp.csp"  
    output = popen(command).read()
    output = output.split("\n")
    if "s UNSATISFIABLE" in output[0]:
        return []
    elif "s SATISFIABLE" not in output[0]:
        raise SystemExit("Solver error!")
    solution = []
    for line in output[1:-2]:
        line = line.split()
        solution.append("( = " + line[1] + " " + line[2] + ")")
    return solution
    

def _satisfiable(systemConstraints, entityConstraints):
    return _solve(systemConstraints, entityConstraints) != []







        
