import numpy as np
import itertools




class Vigenere:
  
    def __init__(self, data, k):
      
        
        self.data = data.replace(' ','')
        key = ''
        for i in range(len(self.data)):
          key += k[i%len(k)]
          
        self.k = key


  
    def encriptar(self):

      num_data = np.array([ord(c)-97 for c in self.data])
      num_key = np.array([ord(d)-97 for d in self.k])

      data_encryption = np.array([(num_data[i]+ num_key[i])%26 for i in range(len(num_data))]) 

      encryption = [chr(c+97) for c in data_encryption]
      return ''.join(encryption)

    def desencriptar(self):
      
        num_data = np.array([ord(c)-97 for c in self.data])
        num_key = np.array([ord(d)-97 for d in self.k])
      
        data_decryption = np.array([(num_data[i]- num_key[i])%26 for i in range(len(num_data))]) 
      
        decryption = [chr(c+97) for c in data_decryption]
        return ''.join(decryption)

    def criptoanalisis(self, MaxLonKey):
      KeyLonFound = False
      
      m=2
      while not(KeyLonFound):

        m+=1
        
        if m > MaxLonKey:
          return 0
        Y=[]
        for a in range(m):
          Y.append('')
        
        for b in range(len(self.data)):
          Y[(b%m)] += self.data[b]

        bool = True
        for c in range(m):

          
          p = self.IC(Y[c])
          
          if 0.06>=p :
            bool = False
            break
            
        KeyLonFound = bool

      key = ''

      for i in range(m):
        best = ['',10]
        for g in range(26):
          sum = self.MG(Y[i],g)
          if abs(0.65-sum)<best[1]:
            best = [chr(g+97),abs(0.65-sum)]
            
        key += best[0]
          
                    
        
      return key

    def IC(self,x):
      
      Ic = 0
      for i in range(26):
        Ic+=(x.count(chr(i+97))/len(x))**2

      return Ic

    def MG(self,y,g):

      Mg = 0
      
      LetterProb = [['a', 0.0834 ],['b', 0.0154 ],['c', 0.0273 ],['d', 0.0414 ],['e', 0.126 ],['f', 0.0203 ],['g', 0.0192 ],['h', 0.0611 ],['i', 0.0671 ],['j', 0.0023 ],['k', 0.0087 ],['l', 0.0424 ],['m', 0.0253 ],['n', 0.068 ],['o', 0.077 ],['p', 0.0166 ],['q', 0.0009 ],['r', 0.0568 ],['s', 0.0611 ],['t', 0.0937 ],['u', 0.0285 ],['v', 0.0106 ],['w', 0.0234 ],['x', 0.002 ],['y', 0.0204 ],['z', 0.0006 ]]

      for i in range(26):
        Mg += (LetterProb[i][1] * (y.count(chr(((i+g)%26)+97)))) / len(y)

      return Mg