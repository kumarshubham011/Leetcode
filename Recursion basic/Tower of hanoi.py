def toh(n, s, t, d):
    if n == 1:
        print(f"move 1 from {s} to {d}")
        return
    toh(n-1, s, d, t)
    print(f" move {n} from {s} to {d}")
    toh(n-1, t, s, d)


toh(3, 'A', 'B', 'C')
