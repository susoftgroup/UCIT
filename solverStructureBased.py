
from satispy import Variable, Cnf
from satispy.solver import Minisat
from random import randint

def _solve(systemConstraints, entityConstraints):
    options = []
    for opt in systemConstraints:
        if not opt:
            continue
        options.append(opt)
        domain = opt + "=" + "Variable('" + opt + "')" 
        exec(domain)
    solver = Minisat()
    entityConstraintsStr = "&".join(entityConstraints)
    output = solver.solve(eval(entityConstraintsStr))
    if output.error:
        raise SystemExit("Solver error!")
    if not output.success:
        return []
    testCase = {}
    for opt in output.varmap: 
        result = output.varmap[opt]
        testCase[opt.name] = "(" + opt.name + ")" if result else "(-" + opt.name + ")"
    for opt in options:
        if opt not in testCase:
            randBool = bool(randint(0,1))
            testCase[opt] = "(" + opt + ")" if randBool else "(-" + opt + ")"
    solution = testCase.values() 
    return solution


def _satisfiable(systemConstraints, entityConstraints):   
    return _solve(systemConstraints, entityConstraints) != []



