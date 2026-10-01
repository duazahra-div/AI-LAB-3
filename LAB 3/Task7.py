#write a python program that prints each item and its corresponding type from the list
datalist = [1452 , 11.23 , 1+2j, True , "w3resource", (0,-1), [5, 12], {"Class":"V","Section":"A"}]

for item in datalist:
    print(item, type(item))