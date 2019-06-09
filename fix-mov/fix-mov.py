import os
import sys

path = os.path.dirname(__file__)

for folder in ('input', 'output'):
    if not os.path.isdir(folder): os.mkdir(folder)

if sys.platform == 'darwin':
    ffmpeg = os.path.join(path, "ffmpeg")
    cmd = ''

if sys.platform == 'win32':
    ffmpeg = os.path.join(path, "ffmpeg.exe")
    cmd = '{0}  -i "{1}" -vcodec png  -acodec aac  "{2}"'
    # {0} path ffmeg, {1} path to source file, {2} path where save file

pathin = os.path.join(path, 'input')
pathout = os.path.join(path, 'output')

files = os.listdir(os.path.join(path, 'input'))
for file in files:
    os.system(cmd.format(ffmpeg,
                         os.path.abspath(os.path.join(pathin, file)),
                         os.path.abspath(os.path.join(pathout, file))))