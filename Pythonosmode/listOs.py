import os
folders = os.listdir("nabil")
# print(folders);
for folder in folders:
  print(folder);
  print(os.listdir(f"nabil/{folder}"))