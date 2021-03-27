L = [123, 'spam', 1.23]
print(len(L))
print(L[:-1])
L = L + [1, 2, 3]
print(L)
L.append('22')
print(L)

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(M)
print(M[0])

col2 = [row[1] for row in M]
print(col2)

# прибавляет + 1 к второй строке матрицы
col3 = [row[1] + 1 for row in M]
print(col3)

# диагональ матрицы
diag = [M[i][i] for i in [0, 1, 2]]
print(diag)

G = (sum(row) for row in M)
print(next(G))





