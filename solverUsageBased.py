from random import randint


def _solve(systemConstraints, entityConstraints):
    domains = {}
    testCase = {}
    for sc in systemConstraints:
        d = sc.rstrip().split()
        if not d:
            continue
        domains[d[0]] = (int(d[1]), int(d[2]))
        testCase[d[0]] = "*"
    for constraint in entityConstraints:
        pairs = constraint.split(",")
        for pair in pairs:
            [option,setting] = pair.split("=")
            if testCase[option] == "*":
                testCase[option] = setting
            elif testCase[option] != setting:
                return []
    for option in testCase:
        if testCase[option] == "*":
            testCase[option] = str(randint(domains[option][0], domains[option][1]))
    solution = [opt + "=" + testCase[opt] for opt in testCase]
    return solution
    
        
def _satisfiable(systemConstraints, entityConstraints):
    return _solve(systemConstraints, entityConstraints) != []


        
