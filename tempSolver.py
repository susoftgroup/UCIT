

def _solve(systemConstraints, entityConstraints):
    # systemConstraints: List of system constraints
    # entityConstraints: List of constraints, each of which represents
    #                    a testable entity to be covered
    # If all of the constraints in systemConstraints and entityConstraints 
    # are satisfiable together, returns a solution, i.e., a  list of constraints
    # representing the solution. Otherwise, returns an empty list.
    solution = []  
    # ...
    return solution


def _satisfiable(systemConstraints, entityConstraints): 
    # systemConstraints: List of system constraints
    # entityConstraints: List of constraints, each of which represents
    #                    a testable entity to be covered
    # If all of the constraints in systemConstraints and entityContsraints 
    # are satisfiable together, returns true. Otherwise, returns false. 
    return _solve(systemConstraints, entityConstraints) != []



