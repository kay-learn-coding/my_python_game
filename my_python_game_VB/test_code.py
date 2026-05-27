num=[1,3,4,6,8,9,11]
max=num[0]
for i in num:
    if i>max:
        max=i
print(max)

sorted_num=[1,2,3,4,5,6,7,8]
n_sorted_num=[2,5,6,9,3,5,6]

def check_num(list):
    if list==sorted(list):
          print(f"yes")
    else:
         print("no")
check_num(sorted_num)
check_num(n_sorted_num)