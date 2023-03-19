
S = 0
result = 0

def gigachad(W, L, H, K, T1, T2):
    global S, result
    S += W * L
    result += (S * H * K * (T1 - T2)) / 860 
    return S, result
