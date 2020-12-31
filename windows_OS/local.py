import sys
import os

os.environ['mp'] = 'D:\CodeWithHarryPrograms\GitHub'
os.environ['gt'] = '095b5f26db73a48cc63aef20f08b07b8f4f91e6f'

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
