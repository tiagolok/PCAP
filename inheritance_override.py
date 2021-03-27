class Left:
    var = "L"
    varLeft = "LL"
    def fun(self):
        return "Left"


class Right:
    var = "R"
    varRight = "RR"
    def fun(self):
        return "Right"

class Sub(Left, Right):
    pass


obj = Sub()

print(obj.var, obj.varLeft, obj.varRight, obj.fun())
