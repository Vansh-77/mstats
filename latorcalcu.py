import random , csv , datetime ,time ,os
file = f"{os.getcwd()}/latorcalcu.csv"
def csvwrite(tnum , canswer , ttime):
    acc = round(canswer/tnum * 100 , 3)
    avgtime = round(ttime / tnum , 2)
    date  = str(datetime.datetime.now()).split()[0]
    with open(file,"a") as f:
        writer = csv.writer(f)
        data = [date,tnum,canswer,(tnum-canswer),acc,avgtime]
        writer.writerow(data)

def latorcalcu(n):
    opt = ["+","-","*","/"]
    canswer =0 
    t1 = time.perf_counter()
    for q in range(n):
        i1 = random.randint(2,999)
        i2 = random.randint(2,99)
        optitr = random.randrange(0,4)
        if i2>i1:
            i1 ,i2 = i2,i1
        if optitr == 0: ogans = round(i1 + i2 , 2)
        if optitr == 1: ogans = round(i1 - i2 , 2)
        if optitr == 2: ogans = round(i1 * i2 , 2)
        if optitr == 3: ogans = round(i1 / i2 , 2)
        print(f"{q+1}. {i1} {opt[optitr]} {i2} ")
        ans = round(float(input("enter your answer :")) , 2)
        if ogans == ans :
            canswer +=1
        else :
            print("1!0!1!0!1!0!1!0!WrOnG aNsWeR!1!0!1!0!1!0!1!0")
            print(f"{i1} {opt[optitr]} {i2} = {ogans}")      
    t2 = time.perf_counter() 
    total_time = t2-t1
    print(f"Total number of question answerd: {n}")
    print(f"Total number of wrong answers: {n - canswer}")
    csvwrite(n,canswer,total_time)


n = int(input("enter no. of questions: "))        
latorcalcu(n)     