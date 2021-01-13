lord = ['hirwa', 'claude', 'SCriptKIng']
print(lord[1])
lord[1] = 'niyibizi'
print('______________________________')
print(lord)
print('______________________________')
for x in lord:
    print(x)
print('______________________________')
if 'hirwa' in lord:
    print("My name is HIRWA is Avilable")
print('______________________________')
print(len(lord))  
print('______________________________')
lord.insert(1 , 'claude')
print(lord)

print('______________________________')
lord.pop(1)
print(lord)

print('______________________________')
lord.clear()
print(lord)