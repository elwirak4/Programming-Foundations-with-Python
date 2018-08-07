import os
def file_name():
    file_list = os.listdir(r"C:\Users\Elwira\Documents\udacity\alphabet")
    print(file_list)

file_name()
saved_path = os.getcwd()
print("Current Working Directory is" +saved_path)
os.chdir(r"C:\Users\Elwira\Documents\udacity\alphabet")

file_list = os.listdir(r"C:\Users\Elwira\Documents\udacity\alphabet")
def rename_files():
    for file_name in file_list:
        #print("Old Name - "+ file_name)
        os.rename(file_name, file_name.translate(None, "0123456789"))
        #os.chdir(saved_path)
        print("Old Name - "+ file_name + "  New Name - "+ file_name.translate(None, "0123456789"))
        #print("New Name - "+ file_name.translate(None, "0123456789"))
rename_files()       
