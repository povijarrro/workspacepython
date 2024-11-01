#!python
import os

def rename(directory):
 
    files = os.listdir(directory)

    for file in files:
        old_file = os.path.join(directory, file)
        print(old_file)
        spl = old_file.split()
        if len(spl)>=4:
            number = spl[3]
            if number.isdigit():
                new_file = os.path.join(directory, f'Manuelait{number}.{spl[-1].split(".")[-1]}')
                os.rename(old_file, new_file)


if __name__ == "__main__":
    rename("D:\\filmy\\manuela\\it")