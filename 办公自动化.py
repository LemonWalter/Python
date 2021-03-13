import os
print(os.getcwd())
print(os.path.join("A","B","C"))
print(os.listdir())

# files = os.listdir(os.getcwd())
# for file in files:
#     print(file, os.path.isdir(file))


for item in os.listdir():
    print(item, os.path.isdir(item))