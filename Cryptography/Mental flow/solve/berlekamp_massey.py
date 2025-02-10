class BerlekampMassey:
    def __init__(self, sequence):
        n = len(sequence)
        C = [0] * n
        B = [0] * n
        C[0] = 1
        B[0] = 1
        L, m, b = 0, -1, 1

        for i in range(n):
            d = sequence[i]
            for j in range(1, L + 1):
                d ^= C[j] & sequence[i - j]
            
            if d == 1:
                T = C[:]
                for j in range(n - i + m):
                    C[i - m + j] ^= B[j]
                if 2 * L <= i:
                    L = i + 1 - L
                    B = T
                    m = i
                    b = d

        self.polynomial = [i for i, x in enumerate(C) if x == 1]
        self.degree = L

    def get_polynomial(self):
        return self.polynomial

    def get_polynomial_degree(self):
        return self.degree

    def __str__(self):
        terms = [f"x^{i}" if i > 0 else "1" for i in sorted(self.polynomial, reverse=True)]
        return " + ".join(terms)

    def __repr__(self):
        return f"<BerlekampMassey polynomial={self.__str__()}>"

