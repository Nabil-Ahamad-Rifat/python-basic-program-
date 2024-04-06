# import os;
# if(not os.path.exists('nabil')):
#   os.mkdir("nabil")
# if(os.path.exists('name')):
#   os.mkdir('name')
#   if(os.path.exists('name/ahmad')):
#     os.mkdir('name/ahmad');
# for i in range (0,100):
#   # os.mkdir(f"nabil/day{i+1}")
#   # os.rename(f"nabil/day{i+1}",f"nabil/inprder{i+1}")
#   os.mkdir(f'name/ahmad/day{i+1}');
import os

if not os.path.exists('nabil'):
    os.mkdir("nabil")

if not os.path.exists('name'):
    os.mkdir('name')

if not os.path.exists('name/ahmad'):
        os.mkdir('name/ahmad')
if not os.path.exists('name/rifat'):
        os.mkdir('name/rifat')

for i in range(100):
    if not os.path.exists(f'name/ahmad/day{i+1}'):
      os.mkdir(f'name/ahmad/day{i+1}')