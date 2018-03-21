X = [0,0,0,1,1,1,1,0,0,0,
     0,0,0,1,0,0,1,0,0,0,
     0,0,0,1,0,0,1,0,0,0,
     0,0,0,1,1,1,1,0,0,0,
     0,0,0,1,0,0,1,0,0,0,]

Y = [0,0,0,0,1,1,0,0,0,0,
     0,0,0,1,0,0,1,0,0,0,
     0,0,0,1,1,1,1,0,0,0,
     0,0,0,1,0,0,1,0,0,0,
     0,0,1,1,0,1,1,0,0,0,]

Z = [0,1,1,1,1,1,1,1,1,0,
     0,1,1,1,1,1,1,1,1,0,
     0,1,1,1,1,1,1,1,1,0,
     0,1,1,1,1,1,1,1,1,0,
     0,1,1,1,1,1,1,1,1,0,]

def spr(A,B):

    def tversky1(A,B):

        AiB=0

        roznicaAB=0

        roznicaBA=0

        for i in range(len(A)):
            if A[i] != 0 and A[i]==B[i]:
                AiB+=1

        for i in range(len(A)):
            if A[i]==1 and B[i]==0:
                roznicaAB+=1

        for i in range(len(A)):
            if B[i]==1 and A[i]==0:
                roznicaBA+=1


        #print(AiB)
        #print(roznicaAB)
        #print(roznicaBA)

    #Tversky indeks
        tversky_indeks=AiB/(AiB+0.1*roznicaAB+0.9*roznicaBA)

        print(tversky_indeks)

        return tversky_indeks

    def tversky2(A,B):

        AiB=0

        roznicaAB=0

        roznicaBA=0

        for i in range(len(A)):
            if A[i] != 0 and A[i]==B[i]:
                AiB+=1

        for i in range(len(A)):
            if A[i]==1 and B[i]==0:
                roznicaAB+=1

        for i in range(len(A)):
            if B[i]==1 and A[i]==0:
                roznicaBA+=1


        #print(AiB)
        #print(roznicaAB)
        #print(roznicaBA)

    #Tversky indeks
        tversky_indeks=AiB/(AiB+0.9*roznicaAB+0.1*roznicaBA)

        print(tversky_indeks)

        return tversky_indeks

    spr=(tversky1(A,B)-tversky2(A,B))
    return(spr)

def T(A,B):
    print(spr(A,B))

T(X,Y)
T(X,Z)