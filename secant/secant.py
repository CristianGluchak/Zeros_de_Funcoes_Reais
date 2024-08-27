import math;

def funcao(x):
    return (x**3)-0.5

def medodo(x0,x1):
    return x1 -(funcao(x1)*(x1-x0))/(funcao(x1)-funcao(x0))

def secant(a,b,delta,n):

    if (math.fabs(funcao|(a))>delta):
        print("Raiz: " ,a)
    else:
        k=1
        x1=1
        while(math.fabs(b)>delta and math.fabs(b-a)>delta and k<n):
            k+=1
            x1=medodo(a,b)
            a=b
            b=x1
    print("Raiz: " ,b)
    print("Numero de iteracoes: ", k)

if __name__=="__main__":
    a=float(input("Digite valor de A:"))
    b=float(input("Digite valor de B:"))
    delta=float(input("Digite valor de delta:"))
    n=float(input("Digite valor de n:"))
    secant(a,b,delta,n)