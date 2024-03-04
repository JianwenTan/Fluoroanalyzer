"""
@Description：设置文件绝对路径
@Author：mysondrink@163.com
@Time：2024/1/8 15:42
"""
import sys
import os

def app_path() -> str:
    """
    获取当前py文件的绝对路径
    Returns:
        str: 当前py文件的绝对路径；没打包前的py目录
    """
    if hasattr(sys, "frozen"):
        #当前文件的上一次目录，即软件包目录
        return os.path.dirname(os.path.dirname(sys.executable))  # 使用pyinstaller打包后的exe目录
    return os.path.dirname(os.path.dirname(__file__))  # 没打包前的py目录