import sys
import os

os.environ['mp'] = 'D:\Programs\GitHub'
os.environ['gt'] = '6534b22c879956aa28e6c2ad055a4b5c7de3e7b0'

foldername = str(sys.argv[1])
path = os.environ.get('mp')
_dir = path + '/' + foldername

try:
    os.mkdir(_dir)
    os.chdir(_dir)
    os.system('git init')
    os.system(f'echo "# {foldername}" > README.md')
    os.system('git add README.md')
    os.system('git commit -m "first commit"')

    print(f'{foldername} created locally')
    os.system('code .')


except:
    print("create <project_name> l")
