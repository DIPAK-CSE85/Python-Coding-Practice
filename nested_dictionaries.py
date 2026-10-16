general={'dipak':{'roll':14,'sgpa':{'sem1':9.25,'sem2':9.35,'sem3':9.20},'branch':'CSE'},'ketan':{'roll':34,'sgpa':{'sem1':8.7,'sem2':8.5,'sem3':8.2},'branch':'civil'},'prem':45}
print(general['ketan']['sgpa']['sem3'])  #for dictionaries you need to pass the keys
print(general['dipak']['sgpa']['sem3'])        #for list you need to pass the index numbers of a perticular keys or values
general['ketan']['phone']=9645765656
general['ketan']['phone']={'home':75867567,'office':576889878}
general['ketan']['phone']['home']=999999
general['ketan']['sgpa']['sem4']=8.0
print(general)
data={'pranay':[12,13,{'roll_no':{'dipak':19,'suraj':12}},15,16,[1,2,3,4,5,],23],'suraj':[45,56,78,99,['mark','branch'],54,32,21]}
print(data)
print(data['suraj'])
print(data['suraj'][4][1])
print(data['pranay'][2]['roll_no']['suraj'])
info=[
    {
        'Name':'dipak',
        'Roll_no':16,
        'Age':20,
        "course":"python"
    },                           #dictioneries in a list
    {
        'Name':'mandar',
        'Roll_no':34,
        'Age':19,
        "course":"java"
    }
]  
print(info[1]['Age'])