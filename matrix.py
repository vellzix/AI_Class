import numpy as np

np.random.seed(5)

a = np.random.randint(0,10,(2, 3))
b = np.random.randint(0,10,(3, 4))

print("Matrix A : \n", a)
print("\n")
print("Matrix B : \n", b)
print("\n")
hasil_kali = np.dot(a, b)
print("Hasil perkalian matrix : \n", hasil_kali)

