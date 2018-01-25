#!/usr/bin/env

import os
import subprocess

postman_travis = os.path.join(os.getcwd(), '..', 'postman_travis')

os.chdir(postman_travis)
subprocess.run(['ls', '-l'])
subprocess.run(['git', 'rev-parse', 'HEAD'])
