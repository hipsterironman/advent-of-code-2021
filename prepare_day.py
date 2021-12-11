from os import mkdir, environ
from sys import argv
from pathlib import Path
from dotenv import load_dotenv
from requests import get

DAY = argv[1]

load_dotenv()
cookies = {
    'session': environ.get('AOC_SESSION'),
}
response = get(
    'https://adventofcode.com/2021/day/{}/input'.format(DAY), cookies=cookies)

mkdir('{0}/day{1}'.format(str(Path.cwd()), DAY))

with open('{0}/day{1}/input.txt'.format(str(Path.cwd()), DAY), 'w') as f:
    f.write(response.text)

with open('{0}/day{1}/problem.py'.format(str(Path.cwd()), DAY), 'w') as f:
    f.write("""from pathlib import Path
contents = []
with open(str(Path(__file__).resolve().parent) + '/input.txt') as f:
    contents = f.read().split('\\n')""")
