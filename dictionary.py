phone_no={'dipak':9797987,'ketan':8977637,'pranay':848299,'dipak':90898,0:122.222}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
numbers=({'dipak':9797987,'ketan':8977637,'pranay':848299,'dipak':90898})
numbers1=(['dipak',9797987,'ketan',8977637,'pranay',848299,'dipak',90898])
print(numbers1)
print(numbers)
print(phone_no)
print(phone_no['pranay'])
print(phone_no['dipak'])
phone_no['bhushan']=123455
phone_no['ketan']=['home',44444,"office",55555]
print(phone_no['ketan'][2])
print(phone_no)
phone_no['dipak']=111111
print(phone_no)
name={1:'dipak',2:'ketan',0:'suraj'}
print(name[0])
print(phone_no.get('dipak'))
del phone_no['pranay']
print(phone_no)
phone_no.pop('bhushan')    #it will deletet the perticcular item
print(phone_no)
phone_no.popitem()       # it will deleten the last one item
print(phone_no)
numbers.clear()         #its removes all data
print(numbers)
phone_no={'dipak':9797987,'ketan':8977637,'pranay':848299,'mandar':90898}
print(phone_no.keys())
print(phone_no.values())
print(phone_no)
phone_no_2=phone_no.copy()     #its used to copy the data of any other dictionary
print(phone_no_2)
print(len(phone_no_2))      #it is used to find the length of dictionary
x=(phone_no.items())        #it is used to seperate the dictionary
for i in x:
    print(i)
for i in phone_no:     
    print(i)

for i in phone_no.items():      #its print each item seperately
    print(i)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             