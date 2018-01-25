#!/usr/bin/env

import os
import subprocess

os.chdir('..')
subprocess.run(['ls', '-l'])
os.chdir('postman_travis')
subprocess.run(['git', 'rev-parse', 'HEAD'])
