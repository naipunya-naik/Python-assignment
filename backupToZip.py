creating file to zip file :

import zipfile
zip_file = zipfile.ZipFile('the.zip','w')
zip_file.write('the.txt', compress_type=zipfile.ZIP_DEFLATED)
zip_file.close()

from zipfile import ZipFile
import os

def get_all_file_paths(directory):

 file_paths = []

for root, directories, files in os.walk(directory):
  for filename in files:
   
   filepath = os.path.join(root, filename)
   file_paths.append(filepath)

 
 return file_paths

def main():
 
 directory = './myfolder'


 file_paths = get_all_file_paths(directory)

 
 print('Following files will be zipped in this program:')
 for file_name in file_paths:
  print(file_name)

 
 with ZipFile('myzipfile.zip','w') as zip:
  # writing each file one by one
  for file in file_paths:
   zip.write(file)

 print('All files zipped successfully!')


if __name__ == "__main__":
    main()





showing all paths in that file:

import zipfile
zip_file = zipfile.ZipFile('the.zip','w')
zip_file.write('the.txt', compress_type=zipfile.ZIP_DEFLATED)
zip_file.close()

from zipfile import ZipFile
import os
def get_all_file_paths(directory):
file_paths = []
for root, directories, files in os.walk(directory):
  for filename in files:
   filepath = os.path.join(root, filename)
   file_paths.append(filepath)
return file_paths

def main():
 directory = './myfolder'
   file_paths = get_all_file_paths(directory)

 
 print('Following files will be zipped in this program:')
 for file_name in file_paths:
  print(file_name)

 
 with ZipFile('myzipfile.zip','w') as zip:
  
  for file in file_paths:
   zip.write(file)

 print('All files zipped successfully!')


if __name__ == "__main__":
    main()
    
