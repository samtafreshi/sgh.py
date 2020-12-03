import os
size = 0
os.chdir(r"C:\Users\samta\PycharmProjects\samus")
for root, directory, filenames in os.walk(".", topdown = False):
   for i in filenames:
      total=0
      print("{} --size-- {}".format(os.path.join(root, i), os.path.getsize(os.path.join(root, i))))
      size= size+ os.path.getsize(os.path.join(root, i))
print("{}  {}".format("The total size is",size))