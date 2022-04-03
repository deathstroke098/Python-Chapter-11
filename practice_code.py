#class test:
   # def a(self):
      #  print("This belongs to test")

#class test1:
   # def a(self):
     #   print("This belongs to test1")

#class test2(test , test1):
   # def a(self):
      #  test.a(self)
      #  test1.a(self)
       # print("This belongs to test2")


#t = test2()
#t.a()        


from re import T


class Tyres:
    def __init__(self, branch, belted_bias, opt_pressure):
        self.branch = branch
        self.belted_bias = belted_bias
        self.opt_pressure = opt_pressure
        
    def __str__(self):
        return ("Tyres: \n \tBranch: " + self.branch +
               "\n \tBelted-bias: " + str(self.belted_bias) + 
               "\n \tOptimal pressure: " + str(self.opt_pressure))
        
class Engine:
    def __init__(self, fuel_type, noise_level):
        self.fuel_type = fuel_type
        self.noise_level = noise_level
        
    def __str__(self):
        return ("Engine: \n \tFuel type: " + self.fuel_type +
                "\n \tNoise level:" + str(self.noise_level))
        
class Body:
    def __init__(self, size):
        self.size = size
        
    def __str__(self):
        return "Body:--\n \tSize: " + self.size
        
class Car():
    def __init__(self,name ,  tyres, engine, body):
        self.name = name 
        self.tyres = tyres
        self.engine = engine
        self.body = body
        
    def __str__(self):
        return str(self.tyres) + "\n" + str(self.engine) + "\n" + str(self.body) + " " + str(self.name)

        
t = Tyres('Pirelli', True, 2.0)
e = Engine('Diesel', 3)
b = Body('Medium')
c = Car("dcsc",T, e, b)
print(c)
