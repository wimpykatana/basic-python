import os

# get current working directory
print(os.getcwd())

# create directory
os.mkdir("test_dir")

# rename directory
os.rename("test_dir", "new_dir")

# remove directory
os.rmdir("new_dir")

# remove file
os.remove("sample.txt")