class StringVar:

    def __init__(self):
         self.s = ''

    def set (self, valuate):
        self.s = valuate

    def get (self):
        return self.s
    
s = StringVar()
print(s.set('The better part of valor is discretion'))
print(s.get())

    
