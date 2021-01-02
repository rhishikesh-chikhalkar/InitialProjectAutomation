import sys
import os

os.environ['mp'] = 'FILEPATH WHERE YOU WANT TO STORE THE PROJECT'
os.environ['gt'] = 'GITHUB_TOKEN_GENERATED_ON_GITHUB.COM'

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
