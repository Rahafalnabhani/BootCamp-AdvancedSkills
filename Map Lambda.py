# Map

#Without Double:
#emp = ['Ali' , 'Nasser' , 'Hamed' , 'Saif' ]
#hoursworked = [1,3,5,7]
#payPerHour=[2,4,6,8]
#result = list(map(lambda hours,pay : hours * pay, hoursworked, payPerHour))
#print(result)
    
# With double :
emp = ['Ali' , 'Nasser' , 'Hamed' , 'Saif' ]
hoursworked = [1,3,5,7]
payPerHour=[2,4,6,8]
result = list(map(lambda hours,pay : hours * pay, hoursworked, payPerHour))
print(result)
doublePay = list(map(lambda pay :pay* 2, payPerHour))

print(doublePay)
result = list(map(lambda hours,pay : hours * pay, hoursworked, doublePay))
print("after double :" ,result)