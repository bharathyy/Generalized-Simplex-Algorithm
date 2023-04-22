import numpy as np
"""
def generalized_simplex(c, A, b, lb=None, ub=None, tol=1e-8, maxiter=1000):
    m, n = A.shape
    # Create a tableau
    tableau = np.zeros((m+1, n+m+1))
    tableau[:-1,:n] = A
    tableau[:-1,n:n+m] = np.eye(m)
    tableau[:-1,-1] = b
    tableau[-1,:n] = -c

    # Add upper and lower bounds to the tableau
    if lb is not None:
        tableau[:-1,:n][np.eye(m)==1] = lb
    if ub is not None:
        tableau[:-1,:n][np.eye(m)==-1] = -ub
    

    # Simplex iterations
    for i in range(maxiter):
        # Choose pivot column
        j = np.argmin(tableau[-1,:n])
        if tableau[-1,j] >= -tol:
            break
        # Choose pivot row
        ratios = tableau[:-1,-1] / tableau[:-1,j]
        ratios[ratios < 0] = np.inf
        k = np.argmin(ratios)
        if ratios[k] == np.inf:
            raise Exception('Problem is unbounded')
        # Update tableau
        pivot = tableau[k,j]
        tableau[k,:] /= pivot
        for l in range(m+1):
            if l != k:
                tableau[l,:] -= tableau[l,j] * tableau[k,:]
    
    # Extract solution and objective value
    x = np.zeros(n)
    for i in range(m):
        if tableau[i,:n].sum() == 1 and (lb is None or lb[i] is None or lb[i] <= 0) and (ub is None or ub[i] is None or ub[i] >= 0):
            x[np.where(tableau[i,:n]==1)[0][0]] = tableau[i,-1]
    obj = -tableau[-1,-1]
    return x, obj
"""
from scipy.optimize import linprog

# Define the objective function and constraints


# Solve the problem using the generalized simplex method

def solution_(c,A,b):
    """
    c = [0,0,-2]
    A = [[1,-2,2], [-1, 1, 1], [2, -1, 4]]
    b = [-8, 4, 10]
    """
    result = linprog(c, A_ub=A, b_ub=b, method='simplex')
    return str(round(result.fun,3))

# Print the optimal solution and objective value
#print(result.x)
#sol = str(result.fun)

#print(result.fun)



"""
c = np.array([3, 2, 1])
A = np.array([[2, 1, 1], [4, 3, 1], [3, 2, 0]])
b = np.array([5, 10, 8])
lb = np.array([0, 0, 0])
ub = np.array([2, 0, 0])

x, obj = generalized_simplex(c, A, b, lb, ub)

print('Optimal solution:', x)
print('Optimal objective value:', obj)
"""