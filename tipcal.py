class Single:
    
    def __init__(self,num):
        self.num = num
        
    def Per1(self):
        Perc1 = 0.1*self.num
        print(f"\n Total Tip of {self.num} is: {Perc1}\n")
        print(f" So The Total Bill With 10% Tip is: {Perc1+self.num}")
    
    def Per2(self):
        Perc2 = 0.15*self.num
        print(f"\n Total Tip of {self.num} is: {Perc2}\n")
        print(f" So The Total Bill With 15% Tip is: {Perc2+self.num}")
    
    def Per3(self):
        Perc3 = 0.2*self.num
        print(f"\n Total Tip of {self.num} is: {Perc3}\n")
        print(f" So The Total Bill With 20% Tip is: {Perc3+self.num}")
        
    def Per4(self,m):
        Perc4 = m/100*self.num
        print(f"\n Total Tip of {self.num} is: {Perc4}\n")
        print(f" So The Total Bill With {m}% Tip is: {Perc4+self.num}")

class Split:

    def __init__(self,num):
        self.num = num
        self.nofs= int(input(" Enter the Number of People: "))
        
    def Perc1(self):
        Percn1 = (0.1*self.num)/self.nofs
        print(f"\n Total Tip of ${self.num} is: {Percn1}\n")
        print(f" So The Total Bill With 10% Tip is: {(Percn1+self.num)/self.nofs}")
    
    def Perc2(self):
        Percn2 = (0.15*self.num)/self.nofs
        print(f"\n Total Tip of {self.num} is: {Percn2}\n")
        print(f" So The Total Bill With 15% Tip is: {(Percn2+self.num)/self.nofs}")
    
    def Perc3(self):
        Percn3 = (0.2*self.num)/self.nofs
        print(f"\n Total Tip of {self.num} is: {Percn3}\n")
        print(f" So The Total Bill With 20% Tip is: {(Perc3+self.num)/self.nofs}")
        
    def Perc4(self,m):
        Percn4 = (m/100*self.num)/self.nofs
        print(f"\n Total Tip of {self.num} is: {Percn4}\n")
        print(f" So The Total Bill With {m}% Tip is: {(Perc4+self.num)/self.nofs}")

 
print(" Welcome To TipZ :D\n")
print("\n Choose The Mode\n 1. Single Tip\n 2. Split Tip\n")

def singlelection(): #single tip function
    print("\n Select The Tip Percent\n 1. 10%\n 2. 15%\n 3. 20%\n 4. Enter Manually\n")
    select = int(input(" Select: "))
    match select:
        case 1:
            a.Per1()
        case 2:
            a.Per2()
        case 3:
            a.Per3()
        case 4:
            i=int(input("Enter your Percet: "))
            a.Per4(i)
        case _:
            print("Something went wrong...")

def splitelection(): #split tip selection
    
    print("\n Select The Tip Percent\n 1. 10%\n 2. 15%\n 3. 20%\n 4. Enter Manually\n")
    select = int(input(" Select: "))
    match select:
        case 1:
            ai.Perc1()
        case 2:
            ai.Perc2()
        case 3:
            ai.Perc3()
        case 4:
            i=int(input("Enter your Percet: "))
            ai.Perc4(i)
        case _:
            print("Something went wrong...")
            
s= int(input(" Select: ")) #choose option between single tip and split tip
match s:
    case 1:
        n= float(input(" Enter Your Bill Amount: "))
        if n<=0:
            print("Invalid Bill Amount")
        else:
            a = Single(n)
            singlelection()
    case 2:
        n= float(input(" Enter Your Bill Amount: "))
        if n<=0:
            print("Invalid Bill Amount")
        else:
            ai = Split(n)
            splitelection()
    case _:
        print("Are you on d**gs?!")
