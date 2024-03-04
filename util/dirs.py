"""
@Description：创建文件目录
@Author：mysondrink@163.com
@Time：2024/1/8 16:25
"""
import os

def makedir(dir_path) -> None:
    """
    判断当前目录是否存在，不存在则创建新目录
    Args:
        dir_path: 文件目录

    Returns:
        None
    """
    dir_path = os.path.dirname(dir_path)
    bool = os.path.exists(dir_path)

    if bool:
        pass
    else:
        os.makedirs(dir_path)