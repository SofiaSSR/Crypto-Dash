import numpy as np
import itertools

class permutacion:
    def __init__(self, data, permutation):
        self.data = data
        self.m = len(permutation)
        self.listdata = self.separar()
        self.permutation = permutation

    def encrypt(self):
        encryption = ''
        for i in self.listdata:
            a = "".join(self.permuPartition(i, self.permutation))
            encryption += a
        return encryption

    def desencrypt(self):
        self.permutation = self.inverPermutation()
        return self.encrypt()

    def cryptanalysis(self):
        print(self.data)
        divisores = []
        for i in range(1, (len(self.data)//2)+1) :
            if(len(self.data))%i == 0 and i <=6 :
                divisores.append(i)
        possibilities = []
        for d in divisores:
            print(d)
            self.m = d
            
            listdata = self.separar()
            permutations = list(itertools.permutations(list(range(d))))
            permutations.pop(0)
            for k in permutations :
                p = ""
                for l in listdata:
                    p += "".join(self.permuPartition(l,k))
                possibilities.append(p)
        return possibilities

    def separar(self):
        if int(len(self.data)) % self.m != 0:
            nx = (self.m * (int(len(self.data)/self.m)+1)) - len(self.data)
            self.data = self.data + 'x'*nx

        listData = []
        j = int(len(self.data)/self.m)
        for i in range(j):
            list1 = list(self.data[i*self.m : (i+1)*self.m])
            listData.append(list1)
        return listData
        
    def permuPartition(self, list, permutation):
        listFinal = []
        for i in permutation:
            listFinal.append(list[i])
        return listFinal

    def inverPermutation(self):
        inverpermutation = []
        for i in range(len(self.permutation)):
            inverpermutation.append(self.permutation.index(i))
        return inverpermutation