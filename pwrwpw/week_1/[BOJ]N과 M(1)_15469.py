def n_and_m(n, m, used, s):
    if len(s) == m:
        print(*s)
        return

    for i in range(1, n + 1):
        if i in used:
            continue
        used.add(i)
        s.append(i)
        n_and_m(n, m, used, s)

        used.remove(i)
        s.pop()

n, m = map(int, input().split())
used = set()
s = []

n_and_m(n, m, used, s)
