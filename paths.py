from pathlib import Path

path = Path("package1")
print(path.exists())

path2 = Path("carpeta1")
if path2.exists():
    print("there is a directory so now this will be deleted")
    path2.rmdir()
else:
    path2.mkdir()
    print("successfully created")

path3 = Path()
for file in path3.glob('*.py'):
    print(file)

#search for pypi.org
#use pip to install and unistall packages from that website
#and use it like the first import in this file