from _Functions import *

# Recursively and randomly apply extensions to a random vertices

K5_e = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4]]


# Repeated extensions

def extension(n, E, i):
    """
    For input edge list E and random number 0 ≤ i ≤ 3, perform extension i to E
    """ 
    N = list(range(n))

    if i == 0:
        U = selection(N, 3)
        return zero_ex(n, E, U)
    
    if i == 1:
        F = random.choice(E)
        N.remove(F[0]) 
        N.remove(F[1])
        D = selection(N, 2)
        U = [F[0], F[1], D[0], D[1]]
        return one_ex(n, E, U)
    
    if i == 2: # V-rep
        F = random.choice(E)
        E.remove(F)
        U = [F[0], F[1]]
        N.remove(F[0])
        N.remove(F[1])
        for e in E:
            if e[0] in F:
                N.remove(e[1])
                E.remove(e)
                U.append(e[1])
                break
            if e[1] in F:
                N.remove(e[0])
                E.remove(e)
                U.append(e[0])
                break

        S = selection(N, 2)
        U.append(S[0])
        U.append(S[1])

        for u in U: # add extension edges
            E.append([u, n])
            
        return E

    if i == 3: # X-rep
        U = random.choice(E) # pick edge
        E.remove(U) # remove edge
        N.remove(U[0])
        N.remove(U[1])
    
        for e in E:
            if len(intersection(e, U)) == 0:
                E.remove(e)
                N.remove(e[0])
                N.remove(e[1])
                U.append(e[0])
                U.append(e[1])
                break 

        S = random.choice(N)
        U.append(S)

        for u in U: # add extension edges
            E.append([u, n])

        return E


def rand_seq(n):
    choices = [0, 1, 2, 3]
    seq = []
    for i in range(n):
        seq.append(random.choice(choices))
    return seq

def multi_ext(k): # perform k extensions
    n = 5
    E = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4]]
    for i in rand_seq(k):
        E = extension(n, E, i)
        n += 1
    return E

# Run repeated V / X-replacements and check rigid at each step:

def multi_V(k): # perform k extensions
    n = 5
    E = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4]]
    for i in range(k):
        E = extension(n, E, 2)
        n += 1
    return E

def multi_V(k): # perform k extensions
    n = 5
    E = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4]]
    for i in range(k):
        E = extension(n, E, 2)
        n += 1
    return E

def multi_X(k): # perform k extensions
    n = 5
    E = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4]]
    for i in range(k):
        E = extension(n, E, 3)
        n += 1
    return E



# cok_v = R_coker(16, E).nullspace()
# print(cok_v)

for i in range(100):
    E = multi_V(13)
    if is_rigid(18, E) == False:
        if subgraph_checker(18, E) == True:
            print(E)
            print('Rigidity lost')

A = [[0, 2], [0, 3], [1, 4], [2, 3], [2, 4], [1, 5], [3, 5], [0, 5], [2, 5], [0, 6], [2, 6], [1, 7], [2, 7], [0, 7], [3, 7], [7, 8], [4, 8], [1, 8], [5, 8], [6, 9], [8, 9], [5, 9], [1, 9], [7, 9]]
B = [[1, 3], [2, 4], [1, 5], [3, 5], [4, 6], [5, 6], [0, 6], [2, 6], [3, 6], [1, 7], [4, 7], [2, 7], [0, 7], [6, 7], [2, 8], [5, 8], [3, 8], [4, 8], [7, 8], [0, 9], [5, 9], [3, 9], [6, 9], [8, 9]]
C = [[1, 4], [2, 3], [2, 4], [0, 5], [1, 5], [3, 6], [5, 6], [0, 6], [1, 6], [2, 6], [2, 7], [5, 7], [0, 7], [3, 7], [1, 8], [7, 8], [3, 8], [2, 8], [6, 8], [4, 9], [5, 9], [0, 9], [6, 9], [7, 9]]
D = [[0, 4], [1, 4], [2, 5], [4, 5], [0, 5], [1, 5], [2, 6], [0, 6], [3, 6], [4, 6], [1, 7], [6, 7], [2, 7], [5, 7], [3, 8], [5, 8], [0, 8], [4, 8], [6, 8], [3, 9], [7, 9], [2, 9], [5, 9], [6, 9]]
E = [[2, 4], [2, 5], [3, 5], [0, 5], [4, 5], [1, 6], [5, 6], [0, 6], [3, 6], [4, 7], [6, 7], [0, 7], [2, 7], [3, 7], [1, 8], [4, 8], [2, 8], [5, 8], [7, 8], [0, 9], [3, 9], [1, 9], [5, 9], [7, 9]]
F = [[1, 3], [1, 4], [2, 4], [3, 5], [4, 5], [2, 6], [3, 6], [0, 6], [1, 6], [5, 6], [2, 7], [5, 7], [1, 7], [4, 7], [0, 8], [7, 8], [4, 8], [1, 8], [5, 8], [0, 9], [5, 9], [1, 9], [3, 9], [6, 9]]
G = [[1, 3], [2, 3], [2, 4], [1, 5], [4, 5], [2, 5], [3, 5], [2, 6], [0, 6], [3, 6], [5, 6], [0, 7], [5, 7], [3, 7], [2, 7], [6, 8], [7, 8], [1, 8], [0, 8], [4, 9], [8, 9], [0, 9], [6, 9], [7, 9]]
H = [[0, 3], [2, 5], [3, 5], [0, 5], [1, 5], [1, 6], [3, 6], [0, 6], [2, 6], [4, 6], [4, 7], [5, 7], [0, 7], [3, 7], [6, 7], [1, 8], [2, 8], [5, 8], [6, 8], [4, 9], [8, 9], [2, 9], [5, 9], [6, 9]]
I = [[1, 3], [1, 4], [2, 3], [2, 4], [2, 5], [3, 5], [5, 6], [2, 6], [3, 6], [0, 7], [2, 7], [3, 7], [1, 7], [6, 7], [0, 8], [5, 8], [1, 8], [2, 8], [3, 8], [0, 9], [6, 9], [4, 9], [2, 9], [8, 9]]
J = [[0, 3], [2, 3], [2, 4], [1, 5], [2, 5], [3, 5], [0, 6], [5, 6], [2, 6], [3, 6], [4, 6], [1, 7], [2, 7], [3, 7], [6, 7], [5, 8], [7, 8], [0, 8], [1, 8], [4, 9], [8, 9], [1, 9], [5, 9], [7, 9]]
K = [[1, 2], [1, 3], [2, 4], [3, 5], [0, 5], [1, 5], [0, 6], [3, 6], [1, 6], [5, 7], [6, 7], [2, 7], [0, 7], [4, 7], [4, 8], [6, 8], [0, 8], [5, 8], [7, 8], [4, 9], [5, 9], [1, 9], [3, 9], [6, 9]]
L = [[0, 4], [2, 4], [1, 5], [2, 5], [0, 5], [3, 5], [4, 5], [0, 6], [3, 6], [4, 6], [2, 7], [6, 7], [3, 7], [5, 7], [1, 8], [7, 8], [3, 8], [5, 8], [6, 8], [1, 9], [6, 9], [4, 9], [0, 9], [5, 9]]
M = [[0, 4], [2, 4], [3, 5], [0, 5], [2, 5], [4, 5], [2, 6], [3, 6], [4, 6], [0, 7], [6, 7], [3, 7], [1, 7], [5, 7], [5, 8], [6, 8], [1, 8], [3, 8], [7, 8], [1, 9], [2, 9], [4, 9], [5, 9], [6, 9]]
N = [[2, 3], [2, 4], [0, 5], [3, 5], [4, 5], [4, 6], [0, 6], [2, 6], [5, 6], [1, 7], [6, 7], [2, 7], [4, 7], [5, 7], [2, 8], [5, 8], [0, 8], [1, 8], [3, 8], [1, 9], [5, 9], [3, 9], [2, 9], [8, 9]]
O = [[1, 3], [2, 4], [0, 5], [1, 5], [2, 5], [3, 5], [5, 6], [0, 6], [1, 6], [2, 6], [3, 7], [0, 7], [4, 7], [5, 7], [4, 8], [6, 8], [1, 8], [2, 8], [5, 8], [2, 9], [7, 9], [1, 9], [3, 9], [6, 9]]




conn_3_circ = [[1, 3], [1, 4], [3, 5], [4, 5], [3, 6], [1, 6], [5, 6], [5, 7], [1, 7], [4, 7], [7, 8], [4, 8], [1, 8], [5, 8], [5, 9], [1, 9], [3, 9], [6, 9]]

# print(draw([[1, 3], [1, 4], [3, 5], [4, 5], [3, 6], [1, 6], [5, 6], [5, 7], [1, 7], [4, 7], [7, 8], [4, 8], [1, 8], [5, 8], [5, 9], [1, 9], [3, 9], [6, 9]]))

# print(E)
# start further on


# for k in range(1000):
#     n = 10 
#     E = [[0, 5], [3, 5], [1, 5], [2, 5], [4, 5], [0, 6], [4, 6], [2, 6], [1, 6], [3, 6], [1, 7], [3, 7], [0, 7], [5, 7], [2, 8], [7, 8], [3, 8], [1, 8], [5, 8], [1, 9], [4, 9], [2, 9], [3, 9], [6, 9]]
#     for i in range(4):
#         E = extension(n, E, 2)
#         n += 1
#     if is_rigid(14, E) == False:
#         if subgraph_checker(14, E) == True:
#             print(E)

# G = nx.from_edgelist(A)
# nx.draw(G, with_labels = True)
# plt.show()




    
    








































# E_class = search[0]
# E_nrigid = search[1]
# print("All examples: ", len(E_class))
# E_keep = []
# E_keep.append(E_class[0])
# X2 = []
# X3 = []
# X4 = []
# X5 = []
# X6 = []
# for F in E_class:
#     if isnot_isomorphic(F, E_keep) == True:
#         E_keep.append(F)
# # print("Distinct examples: ", len(E_class))
# for E in E_class:
#     if colour(E) == 2:
#         X2.append(E)
#     if colour(E) == 3:
#         X3.append(E)
#     if colour(E) == 4:
#         X4.append(E)
#     if colour(E) == 5:
#         X5.append(E)
#     if colour(E) == 6:
#         X6.append(E)

# print("X = 2: ", len(X2), "X = 3: ", len(X3), "X = 4: ", len(X4), "X = 5: ", len(X5), "X = 6: ", len(X6))
# print("X6: ", X6)
# print(E_nrigid)

# print(X3)
