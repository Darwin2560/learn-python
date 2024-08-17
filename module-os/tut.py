import os
from datetime import datetime

print(os.getcwd()) # get the current working directory

os.chdir('/home/darwin/repositories/learn-python/module-os')

mod_time = os.stat('test.txt').st_atime # get file information
print(datetime.fromtimestamp(mod_time)) # convert timestamp to datetime object)

""" for dirpath, dirnames, filenames in os.walk('/home/darwin/repositories/learn-python'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print('-----------------------------------') """

print(os.environ.get('HOME')) # get the value of the HOME environment variable

file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path) # print the full file path

print(os.path.dirname('/tmp/test.txt')) # get the directory path of a file
print(os.path.basename('/tmp/test.txt')) # get the file name from a file path
print(os.path.split('/tmp/test.txt'))
print(os.path.exists('/tmp/test.txt'))
print(os.path.isfile('/tmp/test.txt'))
print(os.path.splitext('/tmp/test.txt'))

print(os.listdir()) # list all files and directories in the current directory

# os.mkdir('OS-Demo-2') # create a new directory
# os.makedirs('OS-Demo-2/Sub-Dir-1') # create more directories in a single line

# os.rmdir('OS-Demo-2') # remove a directory
# os.removedirs('OS-Demo-2/Sub-Dir-1') # remove directories in a single line

# os.rename('name.txt', 'new_name.txt') # rename a file