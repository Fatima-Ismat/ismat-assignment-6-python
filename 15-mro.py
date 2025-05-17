class A:
    def show(self):
        print("A class")

class B(A):
    def show(self):
        print("B class")

class C(A):
    def show(self):
        print("C class")

class D(B, C):
    pass

obj = D()
obj.show()
