import math
z=16
class verify:
def __init__(self,a,b,c,d,e,f):
self.p=a
self.alpha=b
self.beta=c
self.m=d
self.r=e
self.s=f
def v1(self,b,c,d):
a=int(((b**c)*(c**d))%self.p)return a
def v2(self,b,c):
a=int((b**c)%self.p)
return a
def verified(self):
if(self.v1(self.beta,self.r,self.s)==self.v2(self.alpha,self.m)):
print(" SIGNATURE VERIFIED USING ELGAMAL PROBLEM
SOLVED. ")
print("The value of v1 mod p:
"+str(self.v1(self.beta,self.r,self.s)))
print("The value of v2 mod p: "+str(self.v2(self.alpha,self.m)))
else:
print("SIGNATURE MISMATCH!!!")
print("The value of v1 mod p:
"+str(self.v1(self.beta,self.r,self.s)))
print("The value of v2 mod p: "+str(self.v2(self.alpha,self.m)))
class digsignElgamal :
def __init__(self,a,b,c,d):
self.p=a
self.alpha=b
self.beta=int(pow(self.alpha,z)%self.p)
self.m=c
self.k=dself.r=self.createR()
self.s=self.createS()
print ("THE GENERATED SIGNED MESSAGE TRIPLETS ARE :
("+str(self.m)+","+str(self.r)+","+str(self.s)+")")
def gcd(self,a,b):
if a<b:
return gcd(self,b,a)
elif a%b==0:
return b
else:
return gcd(b,a%b)
def invK(self):
kc=self.k
mc=self.p-1
y=0
x=1
if (mc==1):
return 0
while (kc>1):
quotient=kc//mc
temp=mc
mc=kc%mc
kc=temptemp=y
y=x-quotient*y
x=temp
if (x<0):
x=x+self.p-1
return x
def createR(self):
a=int((self.alpha**self.k)%self.p)
return a
def createS(self):
a=(self.invK()*(self.m-z*self.r))%(self.p-1)
return a
p=int(input("ENTER THE VALUE OF PRIME p : "))
alpha=int(input("ENTER THE VALUE OF alpha(primitive root of p) : "))
m=int(input("ENTER THE VALUE OF m (hash value) : "))
k=int(input("ENTER THE VALUE OF k : "))
sign=digsignElgamal(p,alpha,m,k)
print
print ("VERIFICATION OF ELGAMAL SIGNATURE BELOW: ")
print ("SAURABH SINGH 19BCI0184")
v=verify(sign.p,sign.alpha,sign.beta,sign.m,sign.r,sign.s)v.verified()
