# -*- coding:utf-8 -*-
# 遗传算法求解函数最大值：f(x)=x+10sin(5x)+7cos(4x),0<=x<=9
import math
import random
popsize = 960  # 种群规模
genelength = 17  # 染色体长度
pgm = 0.5 # 基因突变的概率
pgc = 0.5  # 基因交叉的概率
breeding_algebra = 100  # 繁殖代数
m=int(popsize/8)
pop = [[0, 0, 0 , 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0] for i in range(m)]  # 初始化种群
pop.extend([[0, 0, 1 , 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0] for i in range(m)])
pop.extend([[0, 1, 0 , 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0] for i in range(m)])
pop.extend([[0, 1, 1 , 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0] for i in range(m)])
pop.extend([[1, 0, 0 , 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0] for i in range(m)])
pop.extend([[1, 0, 1 , 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0] for i in range(m)])
pop.extend([[1, 1, 0 , 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0] for i in range(m)])
pop.extend([[1, 1, 1 , 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0] for i in range(m)])
def b2d(b): #将二进制转化为十进制
    y = 0
    for j in range(len(b)):
        y=y+b[j]*(math.pow(2,len(b)-j-1))
    y = y * 9 / ( 2**genelength- 1)
    return y
def b2t(pop):  # 将种群的二进制基因转为十进制数,位于[0,9]
    temp = []
    for i in range(len(pop)):
        t=b2d(pop[i])
        temp.append(t)
    return temp
def objvaluefunc(pop):  # 计算目标函数值
    objvalue = []
    temp1 = b2t(pop)
    for i in range(len(temp1)):
        x = temp1[i]
        p=x+10*math.sin(5*x)+7*math.cos(4*x)
        objvalue.append(p)
    return objvalue
def fitvaluefunc(objvalue):  # 本例中适应函数即为所求函数本身，也可以重新更改定义,
    # 重新修订一下，当objvalue的值低于0时，设为0。
    fitvalue = []
    for i in range(len(objvalue)):
        if (objvalue[i] > 0):
            fitvalue.append(objvalue[i])
        else:
            fitvalue.append(0)
    return fitvalue
def best(pop, fitvalue):  # 计算最适合个体和最适应值
    bestvalue = fitvalue[0]
    bestindividual = pop[0]
    for i in range(1, len(fitvalue)):
        if (fitvalue[i] > bestvalue):
            bestvalue = fitvalue[i]
            bestindividual = pop[i]
    return [bestvalue,bestindividual]
def sumfitvalue(fitvalue):
    total = 0
    for i in range(len(fitvalue)):
        total += fitvalue[i]
    return total
def cumsumfitvalue(fitvalue):
    t=0
    for i in range(len(fitvalue)):
        t+=fitvalue[i]
        fitvalue[i]=t
def selection(pop, fitvalue):  # 自然选择，轮盘赌算法
    totalvalue = sumfitvalue(fitvalue)
    newfitvalue = []
    for i in range(len(fitvalue)):
        m=fitvalue[i]/totalvalue
        newfitvalue.append(m)
    cumsumfitvalue(newfitvalue)
    ms = []
    poplen = len(pop)
    for i in range(poplen):
        ms.append(random.random())
    ms.sort()
    msin = 0
    fitin = 0
    newpop = pop
    while msin < poplen:
        if(ms[msin] < newfitvalue[fitin]):
            newpop[msin] = pop[fitin]
            msin = msin + 1
        else:
            fitin = fitin + 1
    pop = newpop
def cross(pop, pgc):  # 基因交换
    for i in range(len(pop) - 1):
        if (random.random() < pgc):
            cnum = random.randint(0, len(pop[i]))
            t1 = []
            t2 = []
            t1.extend(pop[i][0:cnum])
            t1.extend(pop[i + 1][cnum:len(pop[i])])
            t2.extend(pop[i + 1][0:cnum])
            t2.extend(pop[i][cnum:len(pop[i])])
            pop[i] = t1
            pop[i + 1] = t2
def muta(pop, pgm):  # 基因突变
    for i in range(len(pop)):
        if (random.random() < pgm):
            mnum = random.randint(0, len(pop[i]) - 1)
            if (pop[i][mnum] == 0):
                pop[i][mnum] = 1
            else:
                pop[1][mnum] = 0
#主函数
results = []
for i in range(breeding_algebra):
    objvalue = objvaluefunc(pop)
    fitvalue = fitvaluefunc(objvalue)
    totalvalue = sumfitvalue(fitvalue)
    [bestvalue,bestindividual] = best(pop,fitvalue)
    results.append([bestvalue,b2d(bestindividual),bestindividual])
    print([bestvalue,b2d(bestindividual),bestindividual])
    selection(pop,fitvalue)
    cross(pop,pgc)
    muta(pop,pgm)
results.sort()
print(results[-1])

