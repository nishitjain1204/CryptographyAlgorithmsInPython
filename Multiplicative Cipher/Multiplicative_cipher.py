print("Multiplicative Cipher....")
s=input("Enter the text to encrypt or decrypt:")
key=int(input("enter the key:"))
 
 
s=s.lower()
 
print("encrypted text:")
    
c=[]
p=[]
for i in range(0,len(s)):
    c.append(chr((((ord(s[i])-97) *key)%26)+97))
c="".join(c)
print(c)
 
print("----------------------------------------------")
def findkeyInverse(r1,r2):
    t1=0
    t2=1
    while(r2>0):
        q=int(r1/r2)
        r=r1-(q*r2)
        r1=r2
        r2=r
        t=t1-(q*t2)
        t1=t2
        t2=t
        print(r1)
        print("and")
        print(r2)
        print(".....")
        
        
    if r1==1:
        b_inv=t1
    else:
        b_inv=1
    k_inv= b_inv % 26
    return k_inv
 
 
print("decryption")
 
z= findkeyInverse(26,key)
print("key inverse is",z)
 
print("-------------------------------------------")
 
for i in range(0,len(s)):
    p.append(chr((((ord(c[i])-97) *z)%26)+97))
p="".join(p)
print("decrypted text:")
print(p)