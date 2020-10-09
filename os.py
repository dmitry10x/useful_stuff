import os

#os.getcwd() --> pwd
#os.chdir
#os.listdir() --> ls / get list of file_names located in the directory
#os.mkdir('folder_name')
#os.makekdirs('folder_name/sub_dir')

#os.rmdir('folder_name')
#os.removedirs('folder_name/sub_dir')

#os.rename('old_file_name.txt', 'new_file_name.txt') #on windows may not work properly, instead try os.replace()
os.replace(r'path/old_name',r'path/new_name')

#os.stat('file_name')
#os.stat('file_name').st_size --> file size in bytes

#os.walk()


# print(os.getcwd())
# os.chdir('C:/Users/Дмитрий/')
# print(os.getcwd())
# os.chdir('C:/Users/Дмитрий/Desktop')
# print(os.listdir())


# for dirpath, dirnames, filenames in os.walk('C:/Users/Дмитрий/'):
#     print('Current Path:', dirpath)
#     print('Directories:', dirnames)
#     print('Files', filenames)


# print(os.environ)
print(os.environ.get('HOME'))
print(os.environ.get('OS'))

print(os.environ.get('HOME'))

