from . import var as var

class SEM(var.Var):
    def get(self): ...

class RollingSEM(var.RollingVar):
    def get(self): ...
