#!/usr/bin/env

import os
import subprocess

os.chdir('..'', 'postman_travis')
subprocess.run(['ls', '-l'])
subprocess.run(['git', 'rev-parse', 'HEAD'])
