# import module
import os
from datetime import datetime

# print all methodes and attributes
# print(dir(os))

# # print current dir
# print(os.getcwd())

# # change dir

# os.chdir('d:/')
# print(os.getcwd())

# # create dir
# os.mkdir('test')
# # create all dirs in the path
# os.makedirs('test2/test/test')

# # print(os.listdir())

# # remove dir
# os.rmdir('test')
# # remove all all dirs in the path
# os.removedirs('test2/test/test')


# # see files and folders () is cwd of (path)
# print(os.listdir())

# # rename file or folder
# # os.rename('test.txt', 'demo.txt')
# # print(os.listdir())

# # info of file
# print(os.stat('demo.txt'))

# print(os.stat('demo.txt').st_size)
# # size of file

# print(os.stat('demo.txt').st_mtime)
# # last time modified

# mod_time = os.stat('demo.txt').st_mtime
# # made a variable

# print(datetime.fromtimestamp(mod_time))
# # use datetime mod to get real time

# # see dir tree
# for root, dirs, files in os.walk('d:/'):
#     print('Current Path:', root)
#     print('Directories:', dirs)
#     print('Files:', files)
#     print()

# environment variable
# print(os.environ)

# print(os.environ.get('HOMEPATH'))
# # users folder

file_path = os.path.join(os.environ.get('HOMEPATH'),
                         'test.txt')
# make filepath in users folder

print(file_path)

print(os.path.basename('/temp/test.txt'))
# gives filename of the path

print(os.path.dirname('/temp/test.txt'))
# gives dirname of the path

print(os.path.split('/temp/test.txt'))
# gives dirname and filename of the path

print(os.path.exists('/tmp/test.txt'))
# checks if path exists

print(os.path.isdir('c:/Users/jurre/source'))
# check if dir exists

print(os.path.isfile('c:/Users/jurre/NTUSER.DAT'))
# check if file exists

print(os.path.splitext('c:/Users/jurre/text.txt'))
# split path and extension

print(dir(os.path))
# alle opties voor os.path
