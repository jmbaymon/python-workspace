#
# Example file for working with classes
#
class myClass():
  def method1(self):
    print("Method1")
  
  def method2(self, Somestring):
    print("myClass Methodd " + Somestring)
# inherits myClass
class anotherClass(myClass):
	def method1(self):
		print("Another Class Methods")
	# override method2 in myclass(the parent class
	def method2(self, Somestring):
		print("anotherClass method")

def main():
  c = myClass()
  c.method1()
  c.method2("Some Some Some") 

  c2 = anotherClass()
  c2.method1()
  c2.method2("This is a string")

  
if __name__ == "__main__":
  main()
