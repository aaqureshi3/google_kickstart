def solve():
    t = int(input())

    for i in range(1,t+1):
        n,d = [int(s) for s in input().split(" ")]
        buses = input().split(" ")
        
        first = int(buses[0])
        max_day = (d // first) * first

        solved = 0
        while solved == 0:
            possible = 1
            day = max_day
            for b in buses:
                b = int(b)
                if day > d:
                    possible = 0 
                    break
                elif day%b == 0:
                    pass
                else:
                    q = day//b
                    day = (q + 1)*b
                    if day > d:
                        possible = 0
                        break
            
            if possible == 0:
                max_day -= first
            else:
                solved = 1
            
        print("Case #{}: {}".format(i,max_day))

if __name__ == "__main__":
    solve()