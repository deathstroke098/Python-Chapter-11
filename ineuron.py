#class test:
  #  def a(self):
        #print("This belongs to test")

#class test1:
#    def b(self):
#        print("This belongs to test1")

#class test2(test , test1):
#    t1 = test()
#    t1.a() # calling function of 
#    t2 = test1()
#    t2.n()
#    print("this is test2")
    
#t = test2()    
#t.a()    



class iNeuron:
    num_of_courses = 20
 
 
class Datascience(iNeuron):
    course_type = 'Data-Science'
 
 
class AI(Datascience):
    def __init__(self):
        self.company = "iNeuron"
       #print('The company {0} offers total {1} different types of courses. Most trending course is {2}'.format(self.company,self.num_of_courses,self.course_type))
        print(f"The company {self.company} offers {self.num_of_courses} courses and the most trending course is {self.course_type}")
 
 
A_I = AI()