new_file = r'/Users/gong/Documents/PKU/Courses/python_basic/test_file_backup_new.txt'
f = open(new_file, "w")
f.write("Now you can add a new row")
# f.close()
f = open(new_file, "r")
print(f.read())