#  HARSHAD NUMBER:
        #  A number is divisible by sum of its digits is called harshad
        #  ex: 156=1+5+6=12
        #      156%12==0
a=int(input('enter number:'))
b=a
sum=0
while a>=1:
    rem=a%10
    sum=sum+rem
    a=a//10
    #print(sum)
if b%sum==0:
    print('harshad')
else:
    print('not harshad')
enter number:156
harshad

# STRONG NUMBER:
#     sum of the factorial of digits is equal to the givennumber
#     ex=145=1!+4!+5!=1+24+120=145
#      145==145
a=int(input('enter number:'))
b=a
sum=0
while a>0:
    rem=a%10
    fact=1
    print(rem)
    for i in range(1,rem+1):
        fact=fact*i
    sum=sum+fact
    a=a//10
if sum==b:
    print('strong')
else:
    print('not strong')
enter number:145
5
4
1
strong

# AREM STRONG NUMBER:
#     SUM OF CUBES OF ITS DIGITS IS EQUAL TO NUMBER ITSELF
#     ex=371=3^3+7^3+1^3=27+343+1=371
a=int(input('enter number:'))
sum=0
b=a
while a>0:
    rem=a%10
    sum=sum+(rem**3)
    a=a//10
if sum==b:
    print('arm strong')
else:
    print('not arm strong')
enter number:371
arm strong

# PALINDROME: A NUMBER IT READS THE SAME AS FORWARD AND BACKWARD
#   EX=121=121
a=int(input('eneter number:'))
rev=0
b=a
while a>0:
    rem=a%10
    rev=rev*10+rem
    a=a//10
if b==rev:
    print('palindrome')
else:
    print('not palindrome')

#FIBONACCI NUMBER: IS THE SEQUENCE OF NUMBER START WITH 0 AND 1 
# WE GET THIRD ELEMENT ADD FIRET 2 PREVIOUS ELEMTS 
# EX=0,1,1,2,3,5,......
n=int(input('enter series how many:'))
a=0
b=1
count=0
while count<n:
    print(a,end=' ')
    d=a+b
    a=b
    b=d
    count+=1
enter series how many:5
0 1 1 2 3 

# SUM OF DIGITS:GIVEN NUMBER EACH DIDITS IS ADDING
# EX: 123=1+2+3=6
n=int(input('enter number:'))
sum=0
b=n
while n>0:
    rem=n%10
    sum=sum+rem
    n=n//10
print(sum)
enter number:345
12

#FACTORIAL NUMBER: it is the product of all postive integers less than are equal to that numbere 
# ex=5!=1*2*3*4*5=120
a=int(input('enter factorial number:'))
fact=1 
for i in range(1,a+1):
    fact=fact*i
print(fact)

a=int(input('enter factorial number:'))
fact=1
i=1
while i<=a:
    fact=fact*i
    i+=1
print(fact)
enter factorial number:5
120
enter factorial number:5
120

# PERFECT NUMBER: POSITIVE INTEGERS THAT IS EQUAL TO SUM OF ITS PROPER DIVISORS 
# EX=6=1+2+=6
a=int(input('enter number:'))
sum=0
for i in range(1,a):
    if a%i==0:
        sum=sum+i
if sum==a:
    print('perfect')
else:
    print('not perfect')
enter number:4
not perfect
enter number:6
perfect

# HAPPY NUMBER: SUM OF SQUARES OF INDIVIDUAL DIGITS
# UNTIL THE SUM BECAMES SINGLE DIGITS THE AT SYUM IS EQUAL TO 1 IS CALLED HAPPY NUMBER 
# EX=13=1^2+3^=1+9+10=1+0=1 SUM==1
a=int(input('enter number:'))
b=a
while a>=10:
    sum=0
    while a>0:
        rem=a%10
        sum=sum+(rem**2)
        a=a//10
    a=sum
if sum==1:
    print('happy')
else:
    print('not happy')
enter number:13
happy

# MAGIC NUMBER: GIVEN NUMBER EACH DIGIS SUM ,THE SUM BECAMES SINGLE DIGITS SUM==1,THEN IS CALLED MAGIC NUMBER 
# EX=123=1+2+3=6 NOT MAGIC NUMBER 
#   190=1+9+0=10=1+0=1
a=int(input('enter number:'))
b=a
while a>=10:
    sum=0
    while a>0:
        rem=a%10
        sum=sum+rem
        a=a//10
    a=sum
if sum==1:
    print('magic')
else:
    print('not magic')
enter number:190
magic

# DUCK NUMBER: given number has atleast one 0 is called duck number ,starting with zero not duck number
# ex=1023 ,023
a=int(input('enter number:'))
b=a
count=0
while a>0:
    rem=a%10
    a=a//10
    if rem==0:
        count+=1
if count>=1:
    print('duck number')
else:
    print('not duck number')
enter number:10006
duck number
enter number:00123
not duck number

#PRIME NUMBER: DIVISIBLE BY NUMBER IS ONE AND ITSELF IS CALLED PRIME
# EX=5 1 AND 5
for i in range(1,21):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
a=int(input('enter number:'))
for i in range(2,a):
    if a%i==0:
        print('not prime')
        break
else:
    print('prime')

#PRODUCT NUMBER: A NUMBER HAVING EACH DIGIT HAVE MULTIPLY OF NUMBER
# EX: 123=1*2*3=6
a=int(input('enter number:'))
mul=1
while a>0:
    rem=a%10
    mul=mul*rem
    a=a//10
print(mul)

REVERSE NUMBER
a=int(input('enter number:'))
b=a
while a>0:
    rem=a%10
    a=a//10
    print(rem,end=' ') 

             PATTERNS
a=int(input('enter character:'))
k=ord('A')
for i in range((a)):
    for j in range(i+1):
        print(chr(k),end=' ')
    k+=1
    print()
output:
A 
B B
C C C
D D D D
E E E E E


              

           

    

        
        


    



  

    


        