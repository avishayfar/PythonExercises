

class Customer:

    def __init__(self,stam,list=None):
        self.stam = stam
        if list is None:
            list = []
        self.list = list
    

    def __str__(self):
        return ('_'.join(self.list))

    def len(self):
        return len(self.list)


class CustomersDict:

    def __init__(self, dictOfCustomers):
        self.dictOfCustomers = dictOfCustomers

    def show(self):
        for k,v in self.dictOfCustomers.items():
            print(k, '-', v)

    def GetCustomer(self,key):
        return self.dictOfCustomers[key]