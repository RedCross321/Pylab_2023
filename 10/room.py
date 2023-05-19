def schet(L, W, H, T1, T2, K):
    S = L * W
    result = round(((L * H * W * (T2 - T1) * K) / 860), 3)
    return S, result
