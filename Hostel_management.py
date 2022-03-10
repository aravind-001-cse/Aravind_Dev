from traceback import print_tb
from cv2 import copyTo

class hotelmange:
    def __init__(self,rt='',s=0,p=0,r=0,t=0,a=1000,name='',address='',cindate='',coutdate='',rno=1):
        print("\n\n****WELCOME TO HOTEL***\n")
        print("\U0000263A")
        self.rt=rt
        self.r=r
        self.t=t
        self.p=p
        self.s=s
        self.a=a
        self.name=name
        self.address=address
        self.cindate=cindate
        self.coutdate=coutdate
        self.rno=rno
    def inputdate(self):
        self.name=input("1.Enter your Fullname:\n")
        self.address=input("2.Enter your address:\n")
        self.cindate=input("3.Enter your check in date:\n")
        self.coutdate=input("4.Enter your checkout date:\n")
        print("Your room no..",self.rno,"\n")
    def roomrent(self):
        print("We have the following rooms for you")
        print("1.Class A<~~~> $4000")
        print("2.Class B<~~~> $3000")
        print("3.Class C<~~~> $2000")
        print("4.Class D<~~~> $1000")
        x=int(input("Enter the number of your choice please->"))
        n=int(input("For how many nights Did you stay:"))
        if(x==1):
            print("You have choose room Class A")
            self.s=4000*n
        elif(x==2):
            print("you have choose room class B")
            self.s=3000*n
        elif(x==3):
            print("you have choose room Class C")
            self.s=2000*n
        elif(x==4):
            print("you have choose room Class D")
            self.s=1000*n
        else:
            print("please choose a room")
        print("Your choosen room rent is=",self.s,"\n")
    def foodpurchased(self):
        print("*******REATAURANT MENU********")
        #print("\U000AF34S")
        for i in range(5):
            print("\U0001F49A",end="")
        print("1.Dessert----->100\n","2.Drinks--->50\n","3.Breakfast--->90\n","4.Lunch--->110\n","5.Dinner-->150\n","6.Exit")
        while(1):
            c=int(input("Enter the number of your choice:"))

            if(c==1):
                d=int(input("Enter the quantity:"))
                self.r=self.r+100*d
            elif(c==2):
                d=int(input("Enter the quantity:"))
                self.r=self.r+50*d
            elif(c==3):
                d=int(input("Enter the quantity:"))
                self.r=self.r+90*d
            elif(c==4):
                d=int(input("Enter the quantity:"))
                self.r=self.r+110*d
            elif(c==5):
                d=int(input("Enter the quantity:"))
                self.r=self.r+150*d
            elif(c==6):
                break;
            else:
                print("You've Enter an Invalid Key")
        print("Total food Cost=Rs",self.r,"\n")
    def display(self):
        print("*****HOTEL BILL*****")
        print("Customer details:")
        print("Customer name:",self.name)
        print("Customer address:",self.address)
        print("Check in date",self.cindate)
        print("Check out date",self.coutdate)
        print("Room no:",self.rno)
        print("Your Room rent is:",self.s)
        print("Your food bill is:",self.r)

        self.rt=self.s+self.t+self.p+self.r

        print ("Your sub total Purchased is:",self.rt)
        print ("Additional Service Charges is",self.a)
        print ("Your grandtotal Purchase is:",self.rt+self.a,"\n")
    
def main():
    a=hotelmange()
    while(1):
        print("1.Enter Customer Data")
        print("2.Calculate Room Rent")
        print("3.Calculate Food Purchased")
        print("4.show total cost")
        print("5.EXIT")

        b=int(input("\n Enter the number of your choice:"))
        if(b==1):
            a.inputdate()
        if(b==2):
            a.roomrent()
        if(b==3):
            a.foodpurchased()
        if(b==4):
            a.display()
        if(b==5):
            quit()
main()
