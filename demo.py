import sys
# 更換
package_path = r".\python3.11.1\Lib\site-packages"
if package_path not in sys.path:
    sys.path.append(package_path)
import numpy as np


print("Hello World")
input("please input any key to exit!")