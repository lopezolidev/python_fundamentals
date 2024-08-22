class BaseClass:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def method_BaseClass(self):
        print(f"This method shows {self.a}, {self.b} and {self.c} from the Base Class")

    def method_A(self):
        pass

class DerivedClass(BaseClass):

    def __init__(self, a, b, c, d, e, f):
        super().__init__(a, b, c)
        self.d = d
        self.e = e
        self.f = f

    def caller_BaseClass(self):
        BaseClass.method_BaseClass()

    #overriding a method from the BaseClass
    def method_a(self):
        print("this is the method A")

    def show_all_attributes(self):
        print(self.a, self.b, self.c, self.d, self.e, self.f) # using "self" we make the call to the attributes from the BaseClass
    
    def only_show_BaseClass(self):
        return super().method_BaseClass() # using "super()" for calling methods from the BaseClass
    
# "self" for attributes of the BaseClass
# "super()" for methods of the BaseClass


derived_object = DerivedClass('a', 'b', 'c', 'd', 'e', 'f')
derived_object.method_BaseClass()
derived_object.method_a()
derived_object.show_all_attributes()
derived_object.only_show_BaseClass() # This method shows a, b and c from the Base Class

print(derived_object.__str__()) # <__main__.DerivedClass object at 0x7fe61ab93be0>
print(derived_object.__repr__()) # <__main__.DerivedClass object at 0x7ffb6cf97be0>