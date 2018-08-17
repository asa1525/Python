'''
import os
def getAllFiles(path):
  ans = []
  for path, dirs, files in os.walk(path):
    for file in files:
      file_abspath = os.path.abspath(os.path.join(path, file))
      ans.append(file_abspath)
  return ans
 
ans = getAllFiles('/Users/admin/experimental/')
for file_abspath in ans:
  print(file_abspath)
'''
import os
import shutil
 
def getAllFiles(path):
  ans = []
  files = os.listdir(path)
  for file in files:
    file_path = os.path.join(path, file)
    if os.path.isdir(file_path): # 如果是目录，将该目录下所有结果加入返回值
      ans += getAllFiles(file_path)
    else: # 对于普通文件，将绝对路径加入返回值
      ans.append(os.path.abspath(file_path))
  return ans
 
ans = getAllFiles('C:\\Users\\45115\\OneDrive\\Python\\script')
for file_abspath in ans:
  print(file_abspath)