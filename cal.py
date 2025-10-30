n = int(input("Enter Your Total Subject's :- "))

total =0 

for i in range(1, n+1):
    mark = float(input(f"Enter sfsfsfYour Marks of Subject {i} :-"))
    total += mark

percentage = total / n

print("Your Total Marks of All Subjects:- ", total)
print("Your Percentage of All Subjects :- ", percentage, "%")