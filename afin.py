import numpy as np
import collections

#a debe ser primo relativo con 26
class Afin:
    def __init__(self, data, a,b):
        self.data = data.replace(' ','')
        self.a = a
        self.b = b

    def encriptar(self):
        num_data = np.array([ord(c)-97 for c in self.data])
        data_encryption = (self.a*num_data + self.b) % 26
        encryption = [chr(c+97) for c in data_encryption]
        return ''.join(encryption)

    def desencriptar(self):
        
        num_data = np.array([ord(c)-97 for c in self.data])
        data_decryption = (pow(self.a, -1, 26)*(num_data - self.b)) % 26
        decryption = [chr(c+97) for c in data_decryption]
        return ''.join(decryption)

    def getLetterFrecuency(self):
        lettersFreq = []
        for i in range(26):
          lettersFreq.append([chr(i+97),0])
        for j in self.data:
          k = ord(j)-97
          lettersFreq[k][1] +=1
        return lettersFreq

    def criptoanalisis(self,FirstCryptedLetter, FirstDecryptedLetter, SecCryptedLetter, SecDecryptedLetter ):

      FCL = ord(FirstCryptedLetter) -97
      FDL = ord(FirstDecryptedLetter)-97
      SCL = ord(SecCryptedLetter) -97
      SDL = ord(SecDecryptedLetter) -97
      
      phi = [1,3,5,7,9,11,15,17,19,21,23,25]

      if abs(SDL-FDL)not in phi or abs(SCL - FCL) not in phi:
        print('Con estas parejas no es posible encontrar una clave a que sea primo relativo con 26',SDL-FDL,SCL - FCL)
        return ''

      else:
        
        self.a =  (pow(SDL-FDL, -1, 26)*(SCL-FCL))% 26
        self.b = (FCL- (self.a*FDL)) % 26

        print(self.a, self.b)
        
        decryption = self.desencriptar()
        return decryption