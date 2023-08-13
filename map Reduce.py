#Reduce:
from functools import reduce

emp = ['Ali' , 'Nasser' , 'Hamed' , 'Saif' ]
hoursworked = [1,3,5,7]
payPerHour=[2,4,6,8]
result = list(map(lambda hours,pay : hours * pay, hoursworked, payPerHour))
print(result)
totalPayment = reduce(lambda a , b:a+b , result)
print ("total : " , totalPayment)
