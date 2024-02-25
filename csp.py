from constraints import *
class Task2Solver: # class idea used from https://www.geeksforgeeks.org/constraint-satisfaction-problems-csp-in-artificial-intelligence/amp/
    def __init__(self):
        self.nva = 0

    def findValues(self, problem):
        variables = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
        domains = {var: list(range(1, 121)) for var in variables}
        
        '''
        constraints would be defined here but to clean up code, I defined them in constraints.py and imported them.
        new constraints can be added to constraints.py and imported here. Altough, if variables and domains are changed, 
        the constraints would need to be updated to match the new variables and domains.
        '''

        # use only the constraints necessary for the problem.
        if problem == 'A':
            variables = variables[:6]
        elif problem == 'B':
            variables = variables[:10]
            pass 

        solution = self.backtrack({}, variables, domains, constraints) # call the backtrack function
        if solution:
            return solution, self.nva
        else:
            return "No solution found for constraint given"

    def backtrack(self, assignment, variables, domains, constraints): # backtracking function
        if len(assignment) == len(variables): # check if all variables are assigned
            if self.constraintsWork(assignment, constraints): # check if all constraints work
                return assignment 
            return None

        var = self.selectUnassigned(variables, assignment, domains) # select an unassigned variable
        for value in domains[var]: # iterate through the domain of the variable
            assignment[var] = value
            self.nva += 1
            if self.constraintsWork(assignment, constraints): # check if all constraints are satisfied
                result = self.backtrack(assignment.copy(), variables, domains, constraints) # call the backtrack function recursively
                if result is not None: 
                    return result
            del assignment[var] 
        return None

    def constraintsWork(self, assignment, constraints):  # check if all constraints are satisfied
        return all(constraint(assignment) for constraint in constraints) # return True if all constraints are satisfied, else False

    def selectUnassigned(self, variables, assignment, domains): # select an unassigned variable
        for var in variables: # iterate through the variables
            if var not in assignment: 
                return var

solver = Task2Solver() # use the class to solve the problems.
solution_A, nva_A = solver.findValues('A')
print("Solution to Problem A:", solution_A)
print("Number of Variable Assignments for A:", nva_A)

solution_B, nva_B = solver.findValues('B')
print("Solution to Problem B:", solution_B)
print("Number of Variable Assignments for B:", nva_B)

solution_C, nva_C = solver.findValues('C')
print("Solution to Problem C:", solution_C)
print("Number of Variable Assignments for C:", nva_C)
