def vchk(ch):
    if(ch=='a'or ch=='A'or ch=='e'or ch=='E'or ch=='i'or ch=='I'
       or ch=='o' or ch=='u'or ch=='U'):
        print(ch,"is a vowel.")
    else:
        print(ch,"is not a vowel.")
ch=input("Enter any char(A-Z/a-z)only:")
vchk(ch)
    
