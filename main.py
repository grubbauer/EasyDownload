import os
import shutil

user = 'Rapha'
filedir = 'C:\\Windows\\EasyDownload\\'  # Replace with the dir you want to use
downdir = f'C:\\Users\\{user}\\Downloads'  # Replace Rapha with your Username

# Defining the paths(I don't know what I'm doing!)
directory_paths = {
    'audios': f'C:\\Users\\{user}\\Downloads\\Audio',
    'compressed': f'C:\\Users\\{user}\\Downloads\\Compressed',
    'databases': f'C:\\Users\\{user}\\Downloads\\Databases',
    'documents': f'C:\\Users\\{user}\\Downloads\\Documents',
    'executables': f'C:\\Users\\{user}\\Downloads\\Executables',
    'images': f'C:\\Users\\{user}\\Downloads\\Images',
    'programming': f'C:\\Users\\{user}\\Downloads\\Programming',
    'sysfiles': f'C:\\Users\\{user}\\Downloads\\Sysfiles',
    '3D': f'C:\\Users\\{user}\\Downloads\\3D',
    'videos': f'C:\\Users\\{user}\\Downloads\\Videos',
}

# Like making directorys and reading or smth
for directory in directory_paths.values():
    os.makedirs(directory, exist_ok=True)

def read_extensions(file_path):
    with open(file_path, 'r') as file:
        return [extension.strip() for extension in file.readlines()]

audext = read_extensions(f'{filedir}audext')
comext = read_extensions(f'{filedir}comext')
datext = read_extensions(f'{filedir}datext')
docext = read_extensions(f'{filedir}docext')
exeext = read_extensions(f'{filedir}exeext')
imgext = read_extensions(f'{filedir}imgext')
proext = read_extensions(f'{filedir}proext')
sysext = read_extensions(f'{filedir}sysext')
trdext = read_extensions(f'{filedir}trdext')
vidext = read_extensions(f'{filedir}vidext')

def move_files(source_directory, destination_directory, extensions):
    for file in os.listdir(source_directory):
        file_path = os.path.join(source_directory, file)

        if os.path.isfile(file_path) and any(file.lower().endswith(ext) for ext in extensions):
            source = file_path
            destination = os.path.join(destination_directory, file)
            shutil.move(source, destination)

# Like I made an more efficient method 
# Heres the og:
#move_files(downdir, directory_paths['audios'], audext)
#move_files(downdir, directory_paths['compressed'], comext)
#move_files(downdir, directory_paths['databases'], datext)
#move_files(downdir, directory_paths['documents'], docext)
#move_files(downdir, directory_paths['executables'], exeext)
#move_files(downdir, directory_paths['images'], imgext)
#move_files(downdir, directory_paths['programming'], proext)
#move_files(downdir, directory_paths['sysfiles'], sysext)
#move_files(downdir, directory_paths['3D'], trdext)
#move_files(downdir, directory_paths['videos'], vidext)

# Heres the new:

extensions_mapping = {
    'audios': 'audext',
    'compressed': 'comext',
    'databases': 'datext',
    'documents': 'docext',
    'executables': 'exeext',
    'images': 'imgext',
    'programming': 'proext',
    'sysfiles': 'sysext',
    '3D': 'trdext',
    'videos': 'vidext',
}
for category, file_extension_key in extensions_mapping.items():
    extensions = read_extensions(os.path.join(filedir, f'{file_extension_key}'))
    move_files(downdir, directory_paths[category], extensions)


print("Files moved successfully!")