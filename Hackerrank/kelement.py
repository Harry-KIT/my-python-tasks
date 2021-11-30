MOD = 10 ** 9 + 7
table = [0] * 1000005


def inverse(a, mod):
    t, newt = 0, 1
    r, newr = mod, a;
    while newr != 0:
        q = r / newr
        t, newt = newt, t - q * newt
        r, newr = newr, r - q * newr
    if t < 0:
        t += mod
    return t


def preprocess():
    for k in range(1, 1000005):
        table[k] = inverse(k, MOD)


def solve(n, k):
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)
    res = 1
    for i in range(k):
        res = (res * (n - i)) % MOD
        res = (res * table[i + 1]) % MOD
    return res


if __name__ == "__main__":
    preprocess()
    t = int(input())
    for _ in range(t):
        [n, k] = map(int, input().split())
        print(solve(n - 1, k - 1))
