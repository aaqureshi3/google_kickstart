def solve():
    t = int(input())

    for i in range(1,t+1):
        n,d = [int(s) for s in input().split(" ")]
        buses = input().split(" ")
        
        first = int(buses[0])
        start = 0
        end = d + 1

        #binary search
        while start < end:
            center = (start + end + 1)//2 
            day = center
            for b in buses:
                b = int(b)
                if day%b != 0:
                    q = day//b
                    day = (q + 1)*b
            if day > d:
                end = center - 1
            else:
                start = center
            
        print("Case #{}: {}".format(i,start))

if __name__ == "__main__":
    solve()