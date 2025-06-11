import py_compile
import os
import shutil
from pyarmor import obfuscate

# Create dist directory if it doesn't exist
if not os.path.exists('dist'):
    os.makedirs('dist')

# Compile to .pyc first
py_compile.compile('main.py', cfile='dist/main.pyc')
py_compile.compile('connector.py', cfile='dist/connector.pyc')

# Then obfuscate with pyarmor
obfuscate(
    'main.py',
    output='dist',
    obf_module=True,
    obf_code=True,
    restrict_mode=1
)

obfuscate(
    'connector.py',
    output='dist',
    obf_module=True,
    obf_code=True,
    restrict_mode=1
)

# Copy requirements.txt to dist
shutil.copy('requirements.txt', 'dist/')

print("Obfuscation complete. Files are in the dist folder.")