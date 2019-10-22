##entering a no.
a=int(input('enter a no. having less than 9 digits\n'))


##all the terms required
b=[' zero',' one',' two',' three',' four',' five',' six',' seven',' eight',' nine']
tens=[' ',' ten',' twenty',' thirty',' fourty','  fifty',' sixty',' seventy',' eighty',' ninety']
teen=[' ',' eleven',' twelve',' thirteen',' fourteen',' fifteen',' sixteen',' seventeen',' eighteen','nineteen']
misc=[' hundread',' thousand',' ',' lakh',' ',' crore']
z=0
d=[]
ans=' '


##putting nos. into list
while a>=1:
    c=a%10
    z+=1
    d.append(c)
   
    a//=10
    


##converting int to string
if z<=8:
    for i in range(z):
        if d[i]==0:
            if i==3 or i==5 or i==7:
                alp=misc[(i-2)]
                ans=alp + ans
            continue
        if i==0:
            alp=b[(d[i])]
        if i==1 or i==4 or i==6 or i==8:
            alp=tens[(d[i])]        
        if i==2 or i==3 or i==5 or i==7:
            alp=b[(d[i])] + misc[(i-2)]
        ans=alp + ans

    
    
else:
    print(d,'\n\n\n you lose a screw?')
        

print(ans)
    
