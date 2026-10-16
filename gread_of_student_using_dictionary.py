import marks_dictionary
new_record={}
for name,mark in marks_dictionary.students_marks.items():
    if mark>90:
        new_record[name]='A+'
    elif mark>80:
        new_record[name]='A'
    elif mark>70:
        new_record[name]='B+'
    elif mark>60:
        new_record[name]='B'
    elif mark>50:
        new_record[name]='C'
    elif mark>=40:
        new_record[name]='D'
    else:
        new_record[name]='F'        
print(new_record)
