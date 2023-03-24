sum = 0
for i in range(1,5):
    grade=float(input('Insert your grade '+str(i)+': '))
    sum+=grade
sum/=4
    
print('Your average is: '+str(sum))