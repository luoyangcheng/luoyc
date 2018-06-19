
class A:
    def __init__(self,name):
        self.name = name

    def sum(self,hh):
        dd = self.name*hh
        return dd

luoyc = A(5).sum(5)
you = A(6).sum(6)

print(luoyc)
print(you)