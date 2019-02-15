print("RSA CRYPTOSYSTEM")
#def autogeneration()
import random

WORDLIST_FILENAMEp128 = "p128.txt"# 39 digits (minimum)
WORDLIST_FILENAMEq128 = "q128.txt"
WORDLIST_FILENAMEp256 = "p256.txt"#77 digits (minimun)
WORDLIST_FILENAMEq256 = "q256.txt"
WORDLIST_FILENAMEp512 = "p512.txt"#154 digits (minimum)
WORDLIST_FILENAMEq512 = "q512.txt"
WORDLIST_FILENAMEp1024 = "p1024.txt"#308 digits (minimum)
WORDLIST_FILENAMEq1024 = "q1024.txt"
WORDLIST_FILENAMEp2048 ="p2048.txt"#616 digits(minimum)
WORDLIST_FILENAMEq2048 ="q2048.txt"
  


def loadWords(c,k):
    s=int(c)
    q=int(k)
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading numbers  from file...")
    # inFile: file
    if s==1:
        if q==1:
            inFile = open(WORDLIST_FILENAMEp128, 'r')
        elif q==2:
            inFile = open(WORDLIST_FILENAMEq128, 'r')
    elif s==2:
        if q==1:
            inFile = open(WORDLIST_FILENAMEp256, 'r')
        elif q==2:
            inFile = open(WORDLIST_FILENAMEq256, 'r')
    elif s==3:
        if q==1:
            inFile = open(WORDLIST_FILENAMEp512, 'r')
        elif q==2:
            inFile = open(WORDLIST_FILENAMEq512, 'r')
    elif s==4:
        if q==1:
            inFile = open(WORDLIST_FILENAMEp1024, 'r')
        elif q==2:
            inFile = open(WORDLIST_FILENAMEq1024, 'r')
    elif s==5:
        if q==1:
            inFile = open(WORDLIST_FILENAMEp2048, 'r')
        elif q==2:
            inFile = open(WORDLIST_FILENAMEq2048, 'r')
        
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    #print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)



   
def gcd(n1,n2):
    if n2 != 0:
       return gcd(n2, n1 % n2)
    else :
       return n1
def miller_rabin(n, k=10):
    if n == 2:
        return True
    if not n & 1:
        return False
    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for i in range(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
    return x == n - 1

    s = 0
    d = n - 1

    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in range(k):
        a = randrange(2, n - 1)
        if not check(a, s, d, n):
            return False
    return True

def cb(p1,q1,t1):
    for i in range(p1+1,t1):
        if gcd(t1,i)==1:
            return i
            break
def multiinverse(a,m):
    m0 = m
    x0 = 0
    x1 = 1
    if m == 1:
      return 0
 
    while a>1:
        # q is quotient
        q = a // m
        t = int(m)
        # m is remainder now, process same as
        # Euclid's algo
        m = (a % m)
        a= t
        t = x0
        x0 = x1 - (q * x0)
        x1 = t
    if a==None:
        a=0
 
    # Make x1 positive
    if (x1 < 0):
       x1 += m0
 
    return x1
def ca(b1,t1):
    f=multiinverse(b1,t1)
    
    return int(f%t1)


def squareAndMultiply(base,exponent,modulus):
    #Converting the exponent to its binary form
    binaryExponent = []
    while exponent != 0:
        binaryExponent.append(exponent%2)
        exponent = exponent//2
    
    #Appllication of the square and multiply algorithm
    result = 1
    binaryExponent.reverse()
    for i in binaryExponent:
        if i == 0:
            result = (result*result) % modulus
        else:
            result = (result*result*base) % modulus
        #print i,"\t",result
    return result


option=int(input("1.128 bits  2.256 bits  3.512 bits   4.1024 bits  5.2048 bits\n Select no of bits"))
wordlist1 = loadWords(option,1)
p = int(chooseWord(wordlist1))

wordlist2=loadWords(option,2)
q = int(chooseWord(wordlist2))
n=p*q
t=(p-1)*(q-1)
b=cb(p,q,t)
while b==None:
    wordlist2=loadWords(option,2)
    q = int(chooseWord(wordlist2))
    print("q ",q)
    n=p*q
    print(n)
    t=(p-1)*(q-1)
    b=cb(p,q,t)
    
    
print("PUBLIC KEY N  ",n)
print ("PUBLIC KEY b ",b)

a=ca(b,t)
#print( a)

alphac={'a':'0','b':'1','c':'2','d':'3','e':'4','f':'5','g':'6','h':'7','i':'8','j':'9','k':'10','l':'11','m':'12','n':'13','o':'14','p':'15','q':'16','r':'17','s':'18','t':'19','u':'20','v':'21','w':'22','x':'23','y':'24','z':'25',' ':'26','0':'27','1':'28','2':'29','3':'30','4':'31','5':'32','6':'33','7':'34','8':'35','9':'36','A':'37','B':'38','C':'39','D':'40','E':'41','F':'42','G':'43','H':'44','I':'45','J':'46','K':'47','L':'48','M':'49','N':'50','O':'51','P':'52','Q':'53','R':'54','S':'55','T':'56','U':'57','W':'58','V':'59','X':'60','Y':'61','Z':'62'}
alphap={'0':'a' ,'1':'b','2':'c','3':'d','4':'e','5':'f','6':'g','7':'h','8':'i','9':'j','10':'k','11':'l','12':'m','13':'n','14':'o','15':'p','16':'q','17':'r','18':'s','19':'t','20':'u','21':'v','22':'w','23':'x','24':'y','25':'z','26':' ','27':'0','28':'1','29':'2','30':'3','31':'4','32':'5','33':'6','34':'7','35':'8','9':'36','37':'A','38':'B','39':'C','40':'E','41':'E','42':'F','43':'G','44':'H','45':'I','46':'J','47':'K','48':'L','49':'M','50':'N','51':'O','52':'P','53':'Q','54':'R','55':'S','56':'T','57':'U','58':'W','59':'V','60':'X','61':'Y','62':'Z'}
s=input("ENTER PLAINTEXT(ALL IN LOWERCASE)     ")
ptxt=''
for i in s:
    valuec =alphac[i]
    ctxt=squareAndMultiply(int(valuec),b,n)
    print(ctxt)
    valuep=squareAndMultiply(int(ctxt),a,n)
    #print(valuep)
    #ptxt=ptxt+alphap[str(valuep)]
choice=int(input("\nTO DECRYPT PRESS 1"))
if choice==1:
    #if len(ptxt)>0:
        #print(ptxt)
    if len(s)>0:
        print(s)
    else:
        print("CANNOT DECRYPT WITHOUT ENCRYPT")
else:
    print("THANK YOU")



