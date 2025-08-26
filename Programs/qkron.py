import numpy as np

def q_product(x, y, q: float):
    """
    q-produto de Borges, vetorizado.
    - Aceita escalares ou arrays (broadcast).
    - Para q=1 retorna x*y.
    - Se x<=0 ou y<=0: retorna 0 (absorvente), consistente com o [·]_+.
    """
    if q == 1.0:
        return np.asarray(x) * np.asarray(y)

    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    # Handle scalar inputs by expanding dimensions
    if x.ndim == 0:
        x = x[np.newaxis]
    if y.ndim == 0:
        y = y[np.newaxis]

    # Result with broadcast shape
    out_shape = np.broadcast(x, y).shape
    out = np.zeros(out_shape, dtype=float)

    # Positive domain mask
   # mask = (x > 0) & (y > 0)

    #if not np.any(mask):
    #    return out

    xm = x
    ym = y

    base = np.power(abs(xm), 1.0 - q) + np.power(abs(ym), 1.0 - q) - 1.0
    base = np.maximum(base, 0.0)

    # Where base>0 apply power; else 0
    res = np.zeros_like(base)
    ok = base > 0.0
    if np.any(ok):
        res[ok] = np.power(base[ok], 1.0 / (1.0 - q))

    out = res
    return out

def q_kron(A: np.ndarray, B: np.ndarray, q: float) -> np.ndarray:
    """
    Produto de Kronecker 'q' (A ⊗_q B):
      (A ⊗_q B)_{(i,α),(j,β)} = A_{ij} ⊗_q B_{αβ}
    - Substitui a multiplicação escalar do bloco por q_product.
    - Para q=1 recupera np.kron(A, B).
    """
    A = np.asarray(A, dtype=float)
    B = np.asarray(B, dtype=float)

    # Reshape 1D arrays to 2D column vectors
    if A.ndim == 1:
        A = A[:, np.newaxis]
    if B.ndim == 1:
        B = B[:, np.newaxis]

    if q == 1.0:
        return np.kron(A, B)
    
    print("A:")

    m = A.shape[0]
    n = A.shape[1]
    p = B.shape[0]
    r = B.shape[1]

    print("m,n,p,r") 
    print(m,n,p,r)
    out = np.zeros((m * p, n * r), dtype=float)

    for i in range(m):
        for j in range(n):
            # bloco (i,j) recebe A[i,j] ⊗_q B, elemento a elemento

            out[i*p:(i+1)*p, j*r:(j+1)*r] = q_product(A[i, j], B, q)

    return out



# Example usage:
# Generate two random arrays
#A = np.random.rand(1, 1)
#B = np.random.rand(2, 2)

#print("Array A:")
#print(A)
#print("\nArray B:")
#print(B)

#q_kron(A  = A ,B = B,q=0.8)
#print("\nKronecker q-product of A and B with q=0.8:")