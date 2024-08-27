import math;

def funcao(x):
    return 
#  return math.e**(-x**2) - math.cos(x)  #2 ativ
#  return x**3-3*x**2-6*x+8
#  return x**3-10

def bisec(a,b,delta,n):
    k=0
    if (math.fabs(b-a)<delta):
        print("Raiz: " ,b)
    else:
        while(math.fabs(b-a)>delta and k<n):
            k+=1
            finicio = funcao(a)
            meio=(a+b)/2.0
            fmeio= funcao(meio)
            if(finicio*fmeio<0):
                b=meio
            else:
                a=meio
    print("Raiz: " ,meio)
    print("Numero de iteracoes: ", k)

if __name__=="__main__":
    a=float(input("Digite valor de A:"))
    b=float(input("Digite valor de B:"))
    delta=float(input("Digite valor de delta:"))
    n=float(input("Digite valor de n:"))
    bisec(a,b,delta,n)