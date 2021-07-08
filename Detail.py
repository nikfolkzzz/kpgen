def area(arr):
    return f"a*b={arr[0]*arr[1]}"

square = {"a":5,"b":6,"func":area}



class Detail:
    def __init__(self,unit):
        args = list(unit.values())
        self.func_args = args[:-1]
        self.func = args[len(args)-1]

    def val_returner(self):
        return self.func(self.func_args)




sq1 = Detail(square)

print(sq1.val_returner())






