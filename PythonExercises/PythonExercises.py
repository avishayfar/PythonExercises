

import Help.functions as func
from Customer import Customer
from Customer import CustomersDict

print ('hello')

func.targil_modoule()

func.factory(4)

func.buildDict(9)

customer = Customer(7, ['a','b','c','d','f','e','h'])
print (customer)
print ("length of customer properties -",customer.len())


c1 = Customer(4, ['a1','b1','c1','d1'])
c2 = Customer(3, ['a2','b2','c2'])
c3 = Customer(2, ['a3','b3'])
c4 = Customer(3, ['a4','b4','c4'])


dict = {'Yossi': c1, 'Ruti': c2, 'Dani': c3 , 'Toto':c4}

customerList = CustomersDict(dict)
customerList.show()
print('value of Yossi =', customerList.GetCustomer('Yossi'))