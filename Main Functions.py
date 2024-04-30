import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations
import random
import copy
import sympy as sp 


"""
COMBINATORICS
"""

def nr_subsets(n, r): 
    """
    returns all r-subsets of {0,..., n - 1}
    """
    N = list(range(n))
    return list(combinations(N, r))


def intersection(lst1, lst2):
    """
    intersects list 1 and list 2
    """
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def nr_with_triangle(n, r):
    """
    return all r-subsets of {0,..., n -1} containing X
    """
    S = nr_subsets(n, r)
    comb = []
    X = [1, 2, 3]
    for s in S:
        if len(intersection(X, list(s))) == 3:
            comb.append(list(s))
    return comb


def powerset(n):
    """
    returns powerset of {0,..., n - 1}
    """
    set = []
    for r in range(2, n + 1):
        set += nr_subsets(n, r)
    return set

def number_zeros(n):
    """
    for an (n + 1) x (n + 1) adjacency matrix,
    returns [a, b], where
    a is the number of edges in K_n
    b is the number of edges to remove from K_n to make |E| = 3|V| - 6
    """
    return [int((n - 1) * n / 2), int((n - 1)* n / 2 - (3 * n - 6))]



def nrk_subsets(n, r, k):
    """
    returns k random choices from the set n-choose-r
    """
    subsets = []
    selection = []
    N = list(range(n))
    for j in range(k): # create k random selections
        for i in range(r): # choose r out of n
            choice = random.choice(N)
            selection.append(choice)
            N.remove(choice) 
        N = list(range(n))
        subsets.append(selection)
        selection = []
    return subsets

def nrk_subsets_triangle(n, r, k):
    """
    returns k random choices from the set n-choose-r
    """
    subsets = []
    selection = [0, 1, 2]
    N = list(range(n))
    for j in range(k): # create k random selections
        for i in range(r): # choose r out of n
            choice = random.choice(N)
            selection.append(choice)
            N.remove(choice) 
        N = list(range(n))
        subsets.append(selection)
        selection = [0, 1, 2]
    return subsets



""" 
CHECKING (3,6)-TIGHTNESS
"""



def edges(A):
    """
    Convert adjacency matrix to edge list [(0,1), (0,2), ...]
    """
    E = []
    n = len(A[0,:])
    for i in range(n):
        for j in range(i, n):
            if A[i,j] == 1 and [j,i] not in E:
                E.append([i,j])
    return E


def subgraph_checker(n, E): 
    """
    checks that a graph on n vertices with edges E satisfies |i(X)| ≤ 3|V'| - 6 for all subsets X of E 
    """
    for v_sub in powerset(n):
        if len(v_sub) < 3:
            continue
        no_edges = 0
        for e in E:
            if e[0] in v_sub and e[1] in v_sub:
                no_edges += 1 
            else:
                continue
        if  no_edges > 3*len(v_sub) - 6:
            return False
        else:
            continue
    return True



"""
Checking rigidity
"""

def coord(p): 
    """
    creates random real coordinate (x, y, z)
    """
    return [np.random.randint(20), np.random.randint(20), np.random.randint(20)]


# def coord(p): 
#     """
#     creates random real coordinate (x, y, z)
#     """
#     return [np.random, 10*np.random.sample(), 10*np.random.sample()]

def R(n, E):
    """
    creates the rigidity matrix of an n-vertex framework 
    """
    RGp = np.zeros((len(E), 3*n))
    row = 0
    P = [coord(p) for p in range(n)]
    for e in E:
        v_1, v_2 = e[0], e[1] # edge vertices
        p_1, p_2 = P[v_1], P[v_2] # vertex realisations
        for i in range(3): # include point difference
            RGp[row, 3*v_1 + i] = p_1[i] - p_2[i]   
            RGp[row, 3*v_2 + i] = p_2[i] - p_1[i]
        row += 1
    return RGp


def is_rigid(n, E):
    """
    creates a realisation for an n-vertex graph on E edges
    checks if rigidity matrix has full rank
    if not, creates another realisation to double-check flexibility is genuine
    """
    RGp = R(n, E)

    rank = np.linalg.matrix_rank(RGp)

    if rank == 3*n - 6:
        return True
    
    if rank < 3*n - 6: # check three realisations
        RGp = R(n, E)
        if np.linalg.matrix_rank(RGp) == 3*n - 6:
            return True
        else: 
            return False
            # RGp = R(n, E)
            # if np.linalg.matrix_rank(RGp) == 3*n - 6:
            #     return True
            
            # else: 
            #     return False





"""
Finding colour
"""

def colour(E): 
    """
    returns chromatic number of a graph with edges E
    """
    G = nx.Graph()
    G.add_edges_from(E)
    col = nx.greedy_color(G, strategy="largest_first")
    return max(col.values()) + 1 

G = [[1, 3], [2, 3], [2, 4], [1, 5], [4, 5], [2, 5], [3, 5], [2, 6], [0, 6], [3, 6], [5, 6], [0, 7], [5, 7], [3, 7], [2, 7], [6, 8], [7, 8], [1, 8], [0, 8], [4, 9], [8, 9], [0, 9], [6, 9], [7, 9]]
H = [[0, 3], [2, 5], [3, 5], [0, 5], [1, 5], [1, 6], [3, 6], [0, 6], [2, 6], [4, 6], [4, 7], [5, 7], [0, 7], [3, 7], [6, 7], [1, 8], [2, 8], [5, 8], [6, 8], [4, 9], [8, 9], [2, 9], [5, 9], [6, 9]]
I = [[1, 3], [1, 4], [2, 3], [2, 4], [2, 5], [3, 5], [5, 6], [2, 6], [3, 6], [0, 7], [2, 7], [3, 7], [1, 7], [6, 7], [0, 8], [5, 8], [1, 8], [2, 8], [3, 8], [0, 9], [6, 9], [4, 9], [2, 9], [8, 9]]
J = [[0, 3], [2, 3], [2, 4], [1, 5], [2, 5], [3, 5], [0, 6], [5, 6], [2, 6], [3, 6], [4, 6], [1, 7], [2, 7], [3, 7], [6, 7], [5, 8], [7, 8], [0, 8], [1, 8], [4, 9], [8, 9], [1, 9], [5, 9], [7, 9]]


"""
Checking for circuits
"""

def pruner(n, E):
    G = nx.Graph()
    G_copy = nx.Graph()
    G.add_edges_from(E)
    G_copy.add_edges_from(E)
    for i in range(n):
        if G_copy.degree[i] == 3:
            G.remove_node(i)
    return nx.to_numpy_array(G)


    
""" 
Searching tools
"""

def filter(A):
    """
    Filters out |E| = 3|V| - 6 adjacency matrices that fail other basic properties
    """ 
    n = len(A[0])
    count = 0
    for i in range(n):
        if sum(A[i]) < 3:
            # print("minimum degree too small")
            return False
        if sum(A[i]) >= 6:
            count += 1
    if  count == n:
        # print("too connected")
        return False
    G = nx.from_numpy_array(A)
    if nx.is_connected(G) == False:
        # print("not connected")
        return False
    else:
        return True 
    

def coord_map(n): 
    """
    returns an enumeration of the lower [i, j] of an (n + 1) x (n + 1) square matrix 
    (corresponding to the egdes in K_{n+1})
    """
    key = []
    for i in range(1,n):
        for j in range(i):
            key.append([i,j])
    return key 


def example_search(n, k):
    """
    generates k graphs with |E| = 3|V| - 6 and returns those that (3, 6)-tight, their rigidity and chromatic number 
    """ 
    key = coord_map(n) 
    N = number_zeros(n)[0]
    r = number_zeros(n)[1]
    
    zeros_selections = nrk_subsets(N, r, k)
    rigid = []
    non_rigid = []

    count = 0

    for guess in zeros_selections:

        A = np.ones((n, n)) - np.identity(n)

        for i in guess:
            A[key[i][0], key[i][1]] = 0
            A[key[i][1], key[i][0]] = 0
        
        G = nx.from_numpy_array(A)

        E = edges(A)

        if filter(A) == False: # go to next guess
            continue
        
        if is_rigid(n, E) == True: # if rigid, we know it is (3, 6)-tight
  
            rigid.append(E)
            continue
        
        if is_rigid(n, E) == False: # if not rigid, check if (3, 6)-tight

            if subgraph_checker(n, E) == False: # if not (3, 6)-tight, go to next guess
                continue
            else:
                non_rigid.append(E)

    return [rigid, non_rigid]



def deg_seq(E):
    """
    returns sorted degree sequence of a graph
    """
    G = nx.Graph()
    G.add_edges_from(E)
    deg = [d for d in G.degree()]
    return sorted([d[1] for d in deg])



def R_coker(n, E):
    """
    creates the rigidity matrix of an n-vertex framework 
    """
    RGp = sp.zeros(len(E), 3*n)
    row = 0
    P = [coord(p) for p in range(n)]
    for e in E:
        v_1, v_2 = e[0], e[1] # edge vertices
        p_1, p_2 = P[v_1], P[v_2] # vertex realisations
        for i in range(3): # include point difference
            RGp[row, 3*v_1 + i] += p_1[i] - p_2[i]   
            RGp[row, 3*v_2 + i] += p_2[i] - p_1[i]
        row += 1
    return RGp.T

def coker(n, E):
    return R_coker(n, E).nullspace()

def circuit(n, E):
    cok_v = R_coker(n, E).nullspace()
    remove = []
    # print(len(E))
    for i in range(len(E)): # fix this
        if cok_v[0][i] == 0:
            remove.append(E[i])
    return [e for e in E if e not in remove]


def cutset(E): # finds a minimal cutset
    G = nx.from_edgelist(E)
    return max(list(nx.all_node_cuts(G)))



def draw(E):
    G = nx.from_edgelist(E)
    nx.draw_circular(G, with_labels = True)
    plt.show()
    return None

def colour_draw(E):
    G = nx.from_edgelist(E)
    colour_map = []
    col = nx.greedy_color(G, strategy="largest_first")
    cols = {0: 'red', 1: 'blue', 2: 'green', 3: 'orange', 4: 'purple', 5: 'black'}
    for node in G:
       colour_map.append(cols[col[node]])     
    nx.draw_circular(G, node_color=colour_map)
    plt.show()
    return None

def dim_coker(n, E):
    return 3*n - 6 - np.linalg.matrix_rank(R(n, E))

# Extension operations: 

def zero_ex(n, E, U):
    """
    Perform 0-extension on graph: add a new vertex with three edges.
    
    Joins vertex n to vertices U = {v1, v2, v3}
    """
    for i in range(3):
        E.append([n, U[i]])
    return E



def one_ex(n, E, U):
    """
    Perform 1-extension on graph: subdivide an edge and adjoin new vertex to two others.

    U = {v1, v2, v3, v4}: vertices involved in the 1-extension. 

    [v1, v2] --> [v_1, v], [v, v2]; add edges [v, v3], [v, v4]
    """
    E.remove([U[0], U[1]]) # remove edge
    for i in range(4):
        E.append([U[i], n])
    return E

C = [[0, 1], [1, 2], [2, 3], [0, 3]]
# print(_0ext(4, C, [0, 1, 2]))

def V_rep(n, E, U):
    """
    Perform V-replacement on graph: remove two adjacent edges, and connect a new vertex to these and vertices and one other

    U = {v1, v2, v3, v4}: vertices involved in the V-replacement. 

    [v1, v2], [v2, v3], v4, v5 --> [v1, v6], [v2, v6], [v3, v6], [v4, v6], [v5, v6] 
    """
    E.remove([U[0], U[1]])
    E.remove([U[1], U[2]])
    for i in range(5):
        E.append([U[i], n])
    return E


def X_rep(n, E, U):
    """
    Perform X-replacement on graph: remove two non-adjacent edges, and connect a new vertex to these and vertices and one other

    U = {v1, v2, v3, v4}: vertices involved in the V-replacement. 

    [v1, v2], [v3, v4], v5 --> [v1, v6], [v2, v6], [v3, v6], [v4, v6], [v5, v6]
    """
    E.remove([U[0], U[1]])
    E.remove([U[2], U[3]])
    for i in range(5):
        E.append([U[i], n])
    return E


def selection(N, k):
    """
    Returns random k elements from list N
    """
    T = []
    for i in range(k):
        r = random.choice(N)
        T.append(r)
        N.remove(r)
    return sorted(T) 



# repeated 0-extensions

def zero_ex_rep(k):
    for i in range(k):
        K5_e = zero_ex(5 + i, K5_e, selection(4 + i, 3))
    return K5_e


# repeated 1-extensions

def one_ex_rep(k):
    for i in range(k):
        U = selection(4 + i, 4)
        if [U[0], U[1]] not in K5_e:
            U = selection(4 + i, 4)
        K5_e = one_ex(5 + i, K5_e, U)
    return K5_e







# def circuit_check(n, E):
#     for e in E[:]:
#         E.remove(e)
#         RGp = R(n, E)
#         rank = np.linalg.matrix_rank(RGp)
#         print(rank)
#         if rank < ## ##:
#             return False
#         E.append(e)
#     return True

# def circuit_finder(n, E, k):
#     circuits = []
#     m = 3*n - 6
#     for j in nr_subsets(m, k): # choose which edges to remove
#         removals = []
#         for i in j: # remove the edges
#             removals.append(k[0])
#         if circuit_check(n, E) == True:
#             circuits.append(E)
#         for r in removals:
#             E.append(r)
#     return circuits





# def circuit_finder(n, E):
#     """
#     returns any circuits in the graph 
#     """
#     circuits = []
#     E_pruned = edges(pruner(n, E)) # remove degree-3 vertices

#     if len(E_pruned) < 3*10 - 6:
#         return None
    
#     else: 
#         for f in E_pruned: # remove an edge
#             E_pcopy2 = [h for h in E_pruned]
#             E_pruned.remove(f)
#             E_pcopy = [i for i in E_pruned]
#             count = 0
#             if np.linalg.matrix_rank(R(n, E_pruned)) == len(E_pcopy):
#                 E_pruned = E_pcopy2
#                 continue
#             elif np.linalg.matrix_rank(R(n, E_pruned)) < len(E_pcopy):
#                 for e in E_pcopy: # check for full rank when deleting one edge, for each edge 
#                     E_pruned.remove(e)
#                     if np.linalg.matrix_rank(R(n, E_pruned)) != len(E_pruned):
#                         print('no')
#                         E_pruned = E_pcopy
#                         break
#                     else:
#                         count += 1
#                         E_pruned = E_pcopy
#                 if count == len(E_pruned):
#                     circuits.append(E_pruned)
#                 E_pruned = E_pcopy2
#     return circuits




# circuits = []
# for f in E_banana: # remove an edge
#     E_banana.remove(f)
#     count = 0
#     E_pcopy = E_banana.copy()
#     for e in E_pcopy: # check for full rank when deleting one edge, for each edge 
#         E_banana.remove(e)
#         if np.linalg.matrix_rank(R(8, E_banana)) != len(E_banana):
#             print('no')
#             E_banana.append(e)
#             break
#         else:
#             count += 1
#             E_banana.append(e)
#     if count == len(E_banana):
#         circuits.append(E_banana)
#     E_banana.append(f)

