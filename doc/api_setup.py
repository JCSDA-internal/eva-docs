from os import listdir
from os.path import isfile, join
import sys

# Get all .rst filenames in API to write to index.md
# In github workflow, script is called outside the doc directory

api_path = sys.argv[1]
api_files = [f for f in listdir(api_path) if isfile(join(api_path, f))]

api_names = []
for f in api_files:
    f_parts = f.split('.')
    if (len(f_parts) == 3):
        if f_parts[1] != 'tests':
            api_names.append(f_parts[0] + '.' + f_parts[1])

# Open API/index.md to modify
f_api = open(api_path + '/index.md', 'a')
for api_name in api_names:
    # Write api file names
    f_api.write(api_name + '\n')
# Close toctree
f_api.write('```')
f_api.close()
