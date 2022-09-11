class Parent1:                                                                  
    def __init__(self, a, b):                                                   
        self.a = a;                                                             
        self.b = b;                                                             
                                                                                
    def showab(self):                                                           
        print("a and b: %d %d" %  (self.a, self.b));                                                                                                                                                                
class Parent2:                                                                  
    def __init__(self, c, d):                                                   
        self.c = c;                                                             
        self.d = d;                                                             
                                                                                
    def showcd(self):                                                           
        print("c and d: %d %d" %  (self.c, self.d));                            
     
# multiple inheritance                                                                           
class Child(Parent1, Parent2):                                                  
    def __init__(self, a, b, c, d, e):                                          
        Parent1.__init__(self, a, b);                                           
        Parent2.__init__(self, c, d);                                           
        self.e = e;                                                             
                                                                                
    def showc(self):                                                            
        print("e: %d" % self.e);                                                
                                                                                
    def sum(self):                                                              
        print("sum(a+b+c+d+e): %d" % (self.a+self.b+self.c+self.d+self.e));     
                                                                                
                                                                                
superObj1 = Parent1(20, 30);                                                    
superObj2 = Parent2(40, 50);                                                    
subObj = Child(11, 12, 13, 14, 15);                                             
superObj1.showab();                                                             
superObj2.showcd();                                                             
                                                                                
subObj.showab();                                                                
subObj.showcd();                                                                
subObj.showc();                                                                 
subObj.sum();   
