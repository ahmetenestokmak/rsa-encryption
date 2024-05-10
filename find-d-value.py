def extended_euclidean_algorithm(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        d, xp, yp = extended_euclidean_algorithm(b, a % b)
        return (d, yp, xp - (a // b) * yp)
      
def modular_inverse(a, m):
    d, x, y = extended_euclidean_algorithm(a, m)
    if d != 1:
        raise ValueError("a and m must be coprime")
    else:
        return x % m
p=443
q=571  
phi_n = (p-1) * (q-1)
e = 7
d = modular_inverse(e,phi_n)
print(d)
