from _Functions import *


# Run this on 10, 15 vertices

# n = 12
# key = coord_map(n) 
# N = number_zeros(n)[0]
# r = number_zeros(n)[1]
# k = 3000
# guesses = nrk_subsets(N, r, k)


rigid = 0
flex = 0
flex_tight = 0
dim_coker_one = 0
dim_coker_two = 0
coker_special = []
conn2_circ = 0
conn2_circ_deg4 = 0
conn2_circ_deg5 = 0
conn3_circ = 0
circ_special = []
conn2_circuit_colours = []
conn3_circuit_colours = []

# flexible = example_search(n, k)[1]


L = [[0, 1], [0, 5], [0, 7], [0, 9], [0, 10], [0, 11], [0, 12], [1, 7], [1, 8], [1, 10], [1, 11], [2, 6], [2, 8], [2, 9], [3, 4], [3, 6], [3, 7], [3, 10], [4, 8], [4, 11], [4, 12], [5, 8], [5, 9], [5, 12], [6, 9], [6, 12], [7, 8], [7, 11], [8, 9], [8, 10], [8, 11], [8, 12], [9, 12]]
K = [[0, 4], [0, 7], [0, 8], [0, 9], [1, 2], [1, 3], [1, 5], [1, 6], [1, 7], [1, 8], [2, 3], [2, 5], [2, 9], [3, 5], [3, 9], [4, 6], [4, 7], [4, 9], [5, 9], [6, 8], [6, 9], [7, 8], [7, 9], [8, 9]]


# print(circuit(10, K))
# print(draw(circuit(13, L)))


# print(circuit(13, L[0]))
# for F in flexible:
#     E = circuit(11, F)
#     if min(deg_seq(E)) == 5:
#        print(draw(E))


# flex_tight = len(flexible)

# for E in flexible: # out of all our guesses
#     dim = 3*n - 6 - np.linalg.matrix_rank(R(n, E))
#     print(dim)
#     if dim == 0:
#         continue
#     if dim > 1:
#         coker_special.append(E)
#     if dim == 1:
#         dim_coker_one += 1
#         circ = circuit(n, E)
#         connectivity = len(cutset(circ))
#         if connectivity == 2:
#             conn2_circ += 1
#             if min(deg_seq(E)) == 4:
#                 conn2_circ_deg4 += 1
#             if min(deg_seq(E)) == 5:
#                 conn2_circ_deg5 += 1
#             chrom = colour(E)
#             conn2_circuit_colours.append(chrom)
#         if connectivity == 3:
#             conn3_circ += 1
#             circ_special.append(E)
#             conn3_circuit_colours.append(colour(E))




for guess in flexible: # out of all our guesses
    A = np.ones((n, n)) - np.identity(n)

    for i in guess:
        A[key[i][0], key[i][1]] = 0
        A[key[i][1], key[i][0]] = 0
    
    G = nx.from_numpy_array(A)

    E = edges(A)

    if is_rigid(n, E) == True:
        rigid += 1
    
    if is_rigid(n, E) == False:
        flex += 1
        if subgraph_checker(n, E) == True:
            flex_tight += 1
            dim = 3*n - 6 - np.linalg.matrix_rank(R(n, E))
            if dim == 0:
                continue
            if dim > 1:
                coker_special.append(E)
            if dim == 1:
                dim_coker_one += 1
                print(E)
                circ = circuit(n, E)
                connectivity = len(cutset(circ))
                if connectivity == 2:
                    conn2_circ += 1
                    if min(deg_seq(E)) == 4:
                        conn2_circ_deg4 += 1
                    if min(deg_seq(E)) == 5:
                        conn2_circ_deg5 += 1
                    chrom = colour(E)
                    conn2_circuit_colours.append(chrom)
                if connectivity == 3:
                    conn3_circ += 1
                    circ_special.append(E)
                    conn3_circuit_colours.append(colour(E))

print("n = ", n, "  k = ", k)
print("%.1f%%" % (100 * rigid/k), " rigid")
print("\n")
print("%.1f%%" % (100 * flex/k), " flexible")
print("\n")
# print("%.5f%%" % (100 * flex_tight/flex), " flexible (3, 6)-tight")
print("\n")
print("%.6f%%" % (100 * dim_coker_two/flex_tight), " dim coker > 1")
print("\n")
print("%.6f%%" % (100 * dim_coker_one/flex_tight), " dim coker = 1")
print("\n")
print("%.5f%%" % (100 * conn2_circ/dim_coker_one), " circuits 2-connected")
print("\n")
print("%.5f%%" % (100 * conn3_circ/dim_coker_one), " circuits 3-connected")
print("\n")
if conn2_circ > 0:
    print("%.1f%%" % (100 * conn2_circ_deg4/conn2_circ), " 2-connected circuits min deg 4")
    print("\n")
    print("%.1f%%" % (100 * conn2_circ_deg5/conn2_circ), " 2-connected circuits min deg 5")
    print("\n")
    print(conn2_circuit_colours, " 2-connected circuits colours")
    print("\n")
    print(conn3_circuit_colours, " 3-connected circuits colours")
    print("\n")
    print(circ_special, " graphs with non-unique circuit")
    print("\n")






            

# dim coker > 1 vs dim coker = 1

# 2-connected vs 3 connected circuit

# minimum degree 4 vs 5
# chromatic number of circuits

# [save 3-connected circuits and their pregraph] 

