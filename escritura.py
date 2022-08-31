import math
from operator import xor 
palabra=input("Ingrese un mensaje:")
residuo=int
aux=int
d8=int
d7=int
d6=int
d5=int
d6=int
d4=int
d3=int
d2=int
d1=int
p1=int
p2=int
p3=int
p4=int

###############################################################################
a1=int
a2=int
a3=int
a4=int
a5=int
a6=int
a7=int
a8=int


##########################################################
archivo=open('Hamming_correcto.txt','w')
archivo1=open('Hamming_incorrecto.txt','w')

for i in palabra:

    aux=ord(i)

    d8=aux%2
    residuo=math.trunc((aux-d8)/2)
    d7=math.trunc(residuo%2)
    residuo=math.trunc((residuo-d7)/2)
    d6=math.trunc(residuo%2)
    residuo=math.trunc((residuo-d6)/2)
    d5=math.trunc(residuo%2)
    residuo=math.trunc((residuo-d5)/2)
    d4=math.trunc(residuo%2)
    residuo=math.trunc((residuo-d4)/2)
    d3=math.trunc(residuo%2)
    residuo=math.trunc((residuo-d3)/2)
    d2=math.trunc(residuo%2)
    residuo=math.trunc((residuo-d2)/2)
    d1=residuo
    p1=xor(d1,d2)
    p1=xor(p1,d4)
    p1=xor(p1,d5)
    p1=xor(p1,d7)
    p2=xor(d1,d3)
    p2=xor(p2,d4)
    p2=xor(p2,d6)
    p2=xor(p2,d7)
    p3=xor(d2,d3)
    p3=xor(p3,d4)
    p3=xor(p3,d8)
    p4=xor(d5,d6)
    p4=xor(p4,d7)
    p4=xor(p4,d8)
    ######################################################################
    a1=d1
    a2=d2
    a3=d3
    a4=d4
    a5=d5
    a6=d6
    a7=d7
    a8=d8
    #########################################################################
    if aux>=32 and aux<=45:
        if a1==0:
            a1=1
        else: a1=0
    else: a1=d1

    if aux>=46 and aux<=58:
        if a2==0:
            a2=1
        else: a2=0
    else: a2=d2

    if aux>=59 and aux<=71:
        if a3==0:
            a3=1
        else: a3=0
    else: a3=d3

    if aux>=72 and aux<=84:
        if a4==0:
            a4=1
        else: a4=0
    else: a4=d4

    if aux>=85 and aux<=99:
        if a5==0:
            a5=1
        else: a5=0
    else: a5=d5

    if aux>=100 and aux<=110:
        if a6==0:
            a6=1
        else: a6=0
    else: a6=d6

    if aux>=111 and aux<=123:
        if a7==0:
            a7=1
        else: a7=0
    else: a7=d7

    if aux>=124 and aux<=255:
        if a8==0:
            a8=1
        else: a8=0
    else: a8=d8
    ##################################################################################################
    archivo.write(str(p1)+str(p2)+str(d1)+str(p3)+str(d2)+str(d3)+str(d4)+str(p4)+str(d5)+str(d6)+str(d7)+str(d8)+"\n")
    archivo1.write(str(p1)+str(p2)+str(a1)+str(p3)+str(a2)+str(a3)+str(a4)+str(p4)+str(a5)+str(a6)+str(a7)+str(a8)+"\n")
    print("Revisar los archivos txt para ver el mensaje codificado")
    

        

    




