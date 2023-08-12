
class bank:
	def __init__(self,name,acc):
		self.acc_name=name
		self.acc_no=acc
		self.baln=0
		self.e_si=0
		self.lst=[]

	def display(self):
		
		self.lst=[self.acc_name,self.acc_no,self.baln,self.e_si]
		
		fp=open("bankfile.txt","w")
		fp.write(str(self.lst))
		fp=open("bankfile.txt","r")
		data=fp.read()
		print(data)
		

	def deposit(self):
		dep=int(input("enter the amount of deposite="))
		self.baln=self.baln+dep
		print("after deposite :",self.baln)
	def widrawel(self):
		wid=int(input("enter the amount of widrawel="))
		if self.baln>=wid:
			self.baln=self.baln-wid
			print("after widrawel ",self.baln)
		else:
			print("no balance")
	def loan(self):
		p=int(input("enter the principal amount="))
		t=int(input("enter the time period is="))
		r=int(input("enter the rate of interest="))
		self.e_si=(p*t*r)/100
		print("The simple interest is",self.e_si)
	def transfer(self):
			m=input("enter the user name")
			acc=input("ente the account number")
			amount=int(input("enter the amount"))
			if self.baln>=amount:
				self.baln=self.baln-amount
				print("transaction completed")
				print("balance=",self.baln)
			else:
				print("no balance")	

name=input("enter the name")
acc=int(input("enter the account number"))
obj=bank(name,acc)
while(True):
	print("choice 1:display")
	print("choice 2:deposite")
	print("choice 3:widrawel")
	print("choice 4:loan")
	print("choice 5:transfer")
	print("choice 6:Exit")
	choice=int(input("enter the choice:"))
	
	if choice==1:
		obj.display()
	elif choice==2:
		obj.deposite()
	elif choice==3:
		obj.widrawel()
	elif choice==4:
		obj.loan()
	elif choice==5:
		obj.transfer()
	else:
		break
