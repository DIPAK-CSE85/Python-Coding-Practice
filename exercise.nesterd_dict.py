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
def new_info(name,roll,age,course):
    new_dict={}
    new_dict['Name']=name
    new_dict['Roll_no']=roll
    new_dict['Age']=age
    new_dict['Course']=course
    info.append(new_dict)            #info.insert(2,new_dict) also used
new_info(name='ketan',roll=89,course="c++",age=21)  
print(info)  