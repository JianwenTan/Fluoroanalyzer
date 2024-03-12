import zipfile
import os
import tempfile
import shutil
import sys
sys.path.append("..")
try:
    import util.frozen as frozen
except ModuleNotFoundError:
    import qt0922.util.frozen as frozen


def main():
    MY_ZIP = frozen.app_path() + r'/update.zip'

    with tempfile.TemporaryDirectory() as tempdir:
        with zipfile.ZipFile(MY_ZIP, 'r') as zip_ref:
            zip_ref.extractall(tempdir)
        # copying tempfile to target directory
        shutil.copytree(tempdir, os.path.dirname(os.path.dirname(MY_ZIP)), dirs_exist_ok=True)


if __name__ == '__main__':
    main()