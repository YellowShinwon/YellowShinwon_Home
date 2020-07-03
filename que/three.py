progresses	 = [93,30,55]
speeds	 = [1,30,5]
#return = 8

def solution(prog, spd):
    prog.reverse()
    spd.reverse()
    ans = []
    while 1:
        cnt = 0
        prog = [prog[i]+spd[i] for i in range(len(prog))]
        # prog = [x+y for x,y in zip(prog, spd)]
        while prog[-1] >= 100:
            cnt += 1
            prog.pop()
            spd.pop()
            if prog == []:
                ans.append(cnt)
                return ans
        if cnt != 0:
            ans.append(cnt)

temp = solution(progresses, speeds)
print(temp)


def math_solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q) == 0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]

def meth_solution_shin(prog, spd):
    prog.reverse()
    spd.reverse()
    ans = []
    # while 1:
    cnt = 0
    # prog = [prog[i]+spd[i] for i in range(len(prog))]
    for x, y in zip(prog, spd):
        print(x, y)
        # print(x/y)

meth_solution_shin(progresses, speeds)