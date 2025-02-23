import pandas as pd

student = {
    "name": ["John","Johnnn","Wowsa","Sam"],
    "Class":["4","3","2","1"],
    "Roll":["41","31","21","11"]
}
print(student["Class"])

dtttttttt = pd.DataFrame(student)
print(dtttttttt)

dtttttttt.to_csv('firstcsv.csv', index=False)


#all list should be eaual in lenght
dict1 = {
    "Fruits" : ["Q","W","E"],
    "Veg" : ["Tom","Kom","Pom"],
    "what" : ["Qq","Ww","Ee"],
}

testfram = pd.DataFrame(dict1)
print(testfram)

testfram.to_csv('cccc.csv',index = False)

tert = pd.read_csv("Book1.csv")
print(tert)

for i in range(len(tert)):
    print(tert["C"][i])