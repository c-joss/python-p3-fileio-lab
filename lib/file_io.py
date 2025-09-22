def write_file(file_name, file_content):
    name = str(file_name)
    if not name.endswith(".txt"):
        name += ".txt"
    with open(name, "w", encoding="utf-8") as f:
        f.write(file_content)

def append_file(file_name, append_content):
    name = str(file_name)
    if not name.endswith(".txt"):
        name += ".txt"
    with open(name, "a", encoding="utf-8") as f:
        f.write(append_content)

def read_file(file_name):
    name = str(file_name)
    if not name.endswith(".txt"):
        name += ".txt"
    with open(name, "r", encoding="utf-8") as f:
        return f.read()
