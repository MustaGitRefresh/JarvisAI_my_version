def reader(file):
    with open(file, 'r') as f:
        content = str(f.read())
    return content
