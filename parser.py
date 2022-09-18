import json
import os
import subprocess
import sys


def run_hupy_file():
    if len(sys.argv) != 2:
        raise Exception("Egy hupy fájlnak kell lennie a bemenetnek!")
    else:
        if sys.argv[1].split(".")[len(sys.argv[1].split("."))-1].replace("\n", "") != "hupy":
            raise Exception("Egy hupy fájlnak kell lennie a bemenetnek!")
        else:
            file = file_to_string(sys.argv[1])
            data = read_json_file()
            python_file = replace_hupy_to_py(file, data)
            save_python_file(python_file)
            run_python_file()
            delete_python_file()


def read_json_file():
    f = open("/home/abelsz/PycharmProjects/hupy/dict.json", "r")
    data = json.load(f)
    f.close()
    return data


def file_to_string(file):
    f = open(file, "r")
    return f.read()


def replace_hupy_to_py(file: str, data: dict):
    f = file
    for i in data:
        f = f.replace(i, data[i])
    return f


def save_python_file(file):
    f = open("tmp.py", "w")
    f.write(file)
    f.close()


def run_python_file():
    subprocess.call("python3 tmp.py", shell=True)


def delete_python_file():
    os.remove("tmp.py")


if __name__ == "__main__":
    run_hupy_file()