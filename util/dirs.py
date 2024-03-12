import os

def makedir(dir_path) -> None:
    dir_path = os.path.dirname(dir_path)
    bool = os.path.exists(dir_path)

    if bool:
        pass
    else:
        os.makedirs(dir_path)