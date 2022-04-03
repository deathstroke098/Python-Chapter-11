class Parent:
    parentAttr = 100

    def __init__(self):
        print("Calling parent constructor")

    def parentMethod(self):
        print("Calling parent method")

    def setAttr(self , Attr):
        Parent.parentAttr = Attr

    def getAttr(self):
        print("Parent attribute :" , Parent.parentAttr)

class Child(Parent):
    def __init__(self):
        print("Calling child constructor")

    def childMethod(self):
        print("Calling child method")


c = Child() # instance of child
c.childMethod() # child calls its method
c.parentMethod() # calls parent's method
c.setAttr(300) #again calls parent's method
c.getAttr() # again calls parent method