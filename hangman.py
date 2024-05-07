# import os
# pathname = os.path.join("Users", 'bob', 'st.txt')
# print(pathname)

# st = open("st.txt", "w")
# st.write("Hi from Python!")
# st.close()

# with open("st.txt", "w") as f:
#     f.write("Hi from Python!")

# with open("st.txt", "r") as f:
#     print(f.read())

# my_list = []

# with open("st.txt", "r") as f:
#     my_list.append(f.read())

# print(my_list)



# import csv

# with open("st.csv", "w") as f:
#     w = csv.writer(f,
#                    delimiter=",")
#     w.writerow(["one",
#                 "two",
#                 "three"])
#     w.writerow(["four",
#                 "five",
#                 "six"])
    


# import csv

# with open("st.csv", "r") as f:
#     r = csv.reader(f, delimiter=",")
#     for row in r:
#         print(",".join(row))


# 练习：
# chatgpt答案
import csv

data = [["Top Gun", "Risky Business", "Minority Report"], 
        ["Titanic", "The Revenant", "Inception"], 
        ["Training Day", "Man on Fire", "Flight"]]

with open('movies.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)