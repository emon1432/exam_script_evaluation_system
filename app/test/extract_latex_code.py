import os
import zipfile

# https://mathpix.com/docs/snip/mpx-cli


# file_path = 'app/generated/output2.tex.zip'

# rename the file
# os.rename(file_path, 'app/generated/output2.tex')

# read the file
with open('app/generated/output2.tex', 'r') as file:
    data = file.read()

print(data)
print(type(data))

# remove ' ' from the string
data = data.replace(' ', '')

print(data)

# remove first '\[' and last '\]' if they exist
if data.startswith('\['):
    data = data[2:]
if data.endswith('\]'):
    data = data[:-2]

print(data)

