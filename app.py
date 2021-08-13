import hashlib

path = r"file"

with open(path,"rb") as f:
    content = f.read()
    sha256 = hashlib.sha256()

    sha256.update(content)

    print("Result: ")
    print(f"{sha256.name} : {sha256.hexdigest()}")
