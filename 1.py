name = {"Alice":90,"Mahatam":89,"Talha":78, "David": 88,"Eva": 76}

Namereq = input("Enter the name of the student: ")

if Namereq in name:
    print(Namereq,"marks are:",name[Namereq])
else:
    print("Student name not in database")
