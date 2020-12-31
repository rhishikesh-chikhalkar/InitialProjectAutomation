import sys
import os
from github import Github

os.environ['mp'] = 'D:\CodeWithHarryPrograms\GitHub'
os.environ['gt'] = '095b5f26db73a48cc63aef20f08b07b8f4f91e6f'

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
