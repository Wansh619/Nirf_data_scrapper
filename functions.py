import math

# def fnc():      #  f(NT, NE)    f(NP)   f(BO)   f(BC)

# def SS(NT,NE,NP):
#     return fnc(NT,NE)*15 + fnc(NP)*5


def N(Nt,Np):
    return Nt+Np


def FSR(F,N):
    temp = F/N
    if temp >= 1/15:
        temp = 1/15
    elif temp <= 1/50:
        temp = 0
    
    return 30*15*temp


def FRU(BC,BO):
    temp1 = BC
    temp2 = BO
    temp3 = (BC+BO)
    temp4 = temp1/temp3
    temp5 = temp2/temp3
    return 7.5*min(temp4,1) + 22.5*min(temp5,1)


# def FQE(FQ,FE,FRA,F!,F2,F3):
#         if FRA >= 95%:
#             FQ = 10
#         else:
#             FQ = 10*(FRA/95)

#     FE = 3*min(3*F1,1) + 3*min(3*F2,1) + 4*min(3*F3,1)

#     return FQE = FQ+FE