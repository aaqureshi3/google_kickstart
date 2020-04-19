def move(p,move):
    w,h = p
    if move == 'N':
        if h == 1:
            h = 10**9
        else:
            h -= 1
    elif move == "S":
        if h == 10**9:
            h = 1
        else:
            h += 1
    elif move == "E":
        if w == 10**9:
            w = 1
        else:
            w += 1
    else:
        if w == 1:
            w = 10**9
        else:
            w -= 1
    return (w,h)

def solution(p,prog):
    end = 0
    while end < len(prog):
        c = prog[end]
        try:
            c = int(c)
        except:
            if c == "(":
                end += 1
            elif c == ")":
                end += 1
                break
            else:
                p = move(p,c)
                end += 1
        else:
            for t in range(0,int(c)):
                p, x = solution(p,prog[end+1:])
            end += x
    return (p,end + 1)

def driver():
    t = int(input())

    for i in range(1,t+1):
        prog = input()
        start = (1,1)
        res,_ = solution(start,prog)


        print("Case #{}: {} {}".format(i,res[0],res[1]))

if __name__ == "__main__":
    driver()