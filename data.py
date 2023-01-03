class Data():
    favs = [] #class

    def __init__(self, name, number,date,time):
        self.name = name
        self.number = number
        self.date = date
        self.time = time

    def is_short(self):
        if self.number < 100:
            return True

    #What happens when you pass object to print?
    def _str_(self):
        return f"{self.name}, {self.number} pages long"

    #What happens when you use ==?
    def _eq_(self, other):
        if(self.name == other.name and self.number == other.number):
            return True
    
    #It's appropriate to give something for _hash_ when you override _eq_
    # #This is the recommended way if mutable (like it is here):
    _hash_ = None

    def _repr_(self): #added to make list of items invoke str
        return self._str_()