def solve():
    t = int(input())

    for i in range(1,t+1):
        n = int(input())
        hills = [int(s) for s in input().split(" ")]

        peaks = 0

        for h in range(1,n-1):
            if hills[h] > hills[h-1] and hills[h] > hills[h+1]:
                peaks += 1

        print("Case #{}: {}".format(i,peaks))

if __name__ == "__main__":
    solve()