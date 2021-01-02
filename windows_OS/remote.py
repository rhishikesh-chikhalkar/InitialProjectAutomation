import sys
import os
from github import Github

os.environ['mp'] = 'D:\Programs\GitHub'
os.environ['gt'] = '6534b22c879956aa28e6c2ad055a4b5c7de3e7b0'

foldername = str(sys.argv[1])
path = os.environ.get('mp')         # add projects dirctory to the env vars
token = os.environ.get('gt')        # add github token to the env vars
_dir = path + '/' + foldername

gt = Github(token)
user = gt.get_user()
login = user.login
repo = user.create_repo(foldername)

commands = [f'echo "# {repo.name}" >> README.md',
            'git init',
            f'git remote add origin https://github.com/{login}/{foldername}.git',
            'git add .',
            'git commit -m "Initial commit"',
            'git push -u origin master']


os.mkdir(_dir)
os.chdir(_dir)

for c in commands:
    os.system(c)

print(f'{foldername} created locally')
os.system('code .')
print("create <fldername>")
