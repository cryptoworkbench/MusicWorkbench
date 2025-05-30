import subprocess
import os
import sys

audio_file = '448602__tedagame__d4.wav'

# Cross-platform way to open a detached subprocess with no output
startupinfo = None
creationflags = 0

# Windows-specific setup
if sys.platform == 'win32':
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    creationflags = subprocess.CREATE_NEW_PROCESS_GROUP

# Open in detached/background mode with output suppressed
def p():
    with open(os.devnull, 'w') as devnull:
        subprocess.Popen(
            ['ffplay', '-nodisp', '-autoexit', audio_file],
            stdout=devnull,
            stderr=devnull,
            stdin=devnull,
            startupinfo=startupinfo,
            creationflags=creationflags,
            close_fds=True # needed for proces child process detachment in unix systems
        )

p();
