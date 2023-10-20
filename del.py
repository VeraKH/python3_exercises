#DEL is instruction - the same as __delitem__

my_dict = {1:'1', 2:'2', 3:'3'}

del my_dict[1]
my_dict.__delitem__(2)
print(my_dict)
