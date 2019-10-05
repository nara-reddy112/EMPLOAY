class employee:
	def __init__(self):
		self.eno=int(input("enetr the number"))
		self.ename=input("enter the name")
		self.dsg=input("enetr the designation")
		self.bsal=float(input("enetr the basic sal"))
	def calemploy(self):
		self.da=self.bsal*0.2
		self.ta=self.bsal*0.1
		self.cca=self.bsal*0.02
		self.ma=self.bsal*0.05
		self.hra=self.bsal*0.15
		self.lic=self.bsal*0.02
		self.gif=self.bsal*0.02
		self.netsal=(self.da+self.ta+self.cca+self.ma+self.hra+self.bsal)-(self.lic+self.gif)
	def disp(self):
		print("-"*30)
		print("employee details")
		print("employ number=%d"%self.eno)
		print("employ name=%s"%self.ename)
		print("employ designation=%s"%self.dsg)
		print("employ basic salr=%f"%self.bsal)
		print("employ da=%f"%self.da)
		print("employ ta=%f"%self.ta)
		print("employ cca=%f"%self.cca)
		print("employ ma=%f"%self.ma)
		print("employ hra=%f"%self.hra)
		print("employ lic=%f"%self.lic)
		print("employ gpf=%f"%self.gif)
		print("employ netsal=%f"%self.netsal)
eo=employee()
eo.calemploy()
eo.disp()

