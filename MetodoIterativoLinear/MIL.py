import math;


def fI(x):
    return  (x**3)/9+ 1/3

def funcao(x):
    return x**3 - 9 * x + 3

def MIL(a,delta,n):
    if (math.fabs(funcao(a))<delta):
        print("Raiz: " ,a)
    else:
        k=1
        a1 = fI(a)
        while(math.fabs(funcao(a))>delta and math.fabs(a1-a)>delta and k<n):
            k+=1
            a=a1
            a1 = fI(a)


    print("Raiz: " ,a1)
    print("Numero de iteracoes: ", k)

if __name__=="__main__":
    a=float(input("Digite valor de A:"))
    delta=float(input("Digite valor de delta:"))
    n=float(input("Digite valor de n:"))
    MIL(a,delta,n)