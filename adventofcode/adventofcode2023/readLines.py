def readLines(file,sep="\n"):
    with open(file,"r") as f:
        return f.read().strip().split(sep)