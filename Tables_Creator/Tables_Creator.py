from tabulate import tabulate
data = [["Name", "Place", "Gender"], ["Sai Ashish", "Mumbai", "Male"], ["Sai Ansul", "New Delhi", "Male"], ["Ganesh", "Orissa", "Male"]]
print(tabulate(data, headers='firstrow', tablefmt='fancy_grid'))