#!/usr/bin/env

import os
import subprocess

os.chdir('..')
subprocess.run(['ls', '-l'])

subprocess.run(['git', 'clone', 'https://github.com/fayeezahmed/postman_travis.git'])

os.chdir('postman_travis')

subprocess.run(['git', 'rev-parse', 'HEAD'])
