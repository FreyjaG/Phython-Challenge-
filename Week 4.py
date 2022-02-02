import array as arr
a = arr.array('i', [2, 4, 6, 8])

print("First element:", a[0])
print("Second element:", a[1])
print("Last element:", a[-1])


a = arr.array('i', [2, 4, 6, 8, 10])

print("We are on this bit")
print("First element:", a[0])
print("Second element:", a[1])
print("Last element:", a[2])

res = a[::-1]
print("REsultant new reversed array:" ,res)



print("This is the second bit")



