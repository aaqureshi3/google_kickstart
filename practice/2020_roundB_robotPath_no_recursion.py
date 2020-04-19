def solve():
    t = int(input())
    mod = 10**9
    for i in range(1, t + 1):
        w,h = 0,0
        step = 1
        rep = []
        for x in input():
            if x == "N":
                h = (h - step)%mod
            elif x == "E":
                w = (w + step)%mod
            elif x == "S":
                h = (h + step)%mod
            elif x == "W":
                w = (w - step)%mod
            elif x == "(":
                pass
            elif x == ")":
                step //= rep.pop()
            else:
                r = int(x)
                step *= r
                rep.append(r)

        print("Case #{}: {} {}".format(i, w+1, h+1))

if __name__ == "__main__":
    solve()