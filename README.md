# embed_pyinstaller_testing_package


### 開源
```bash=
https://qfluentwidgets.com/pages/install/
```


### 打包
```bash=
// cd 根目錄
.\python3.11.1\python.exe -m PyInstaller demo.py
```

暫時先這樣測試，如果不行就再換方法，目前採取應急的方式處理

公司電腦沒辦法直接下載，還需要再試錯


### 包內容
```bash=
C:\Users\rex09\Desktop\測試用embed\python3.11.1\Scripts>pip list
Package                   Version
------------------------- -----------
altgraph                  0.17.4
astroid                   3.3.5
attrs                     24.2.0
beautifulsoup4            4.12.3
calendra                  7.9.1
certifi                   2024.8.30
cffi                      1.17.1
charset-normalizer        3.4.0
colorama                  0.4.6
colorthief                0.2.1
contourpy                 1.3.0
convertdate               2.4.0
cycler                    0.12.1
darkdetect                0.8.0
dill                      0.3.9
et_xmlfile                2.0.0
fonttools                 4.54.1
h11                       0.14.0
idna                      3.10
iniconfig                 2.0.0
isort                     5.13.2
Jinja2                    3.1.4
kiwisolver                1.4.7
loguru                    0.7.2
lunardate                 0.2.2
lxml                      5.3.0
MarkupSafe                3.0.2
matplotlib                3.9.2
mccabe                    0.7.0
more-itertools            10.5.0
numpy                     2.1.3
openpyxl                  3.1.5
outcome                   1.3.0.post0
packaging                 24.1
pefile                    2023.2.7
pillow                    11.0.0
pip                       24.3.1
platformdirs              4.3.6
pluggy                    1.5.0
pycparser                 2.22
pyinstaller               6.11.0
pyinstaller-hooks-contrib 2024.9
pylint                    3.3.1
pyluach                   2.2.0
PyMeeus                   0.5.12
pyparsing                 3.2.0
PyQt-Fluent-Widgets       1.7.1
PyQt5                     5.15.11
PyQt5-Frameless-Window    0.4.3
PyQt5-Qt5                 5.15.2
PyQt5_sip                 12.15.0
PySocks                   1.7.1
pytest                    8.3.3
python-dateutil           2.9.0.post0
pywin32                   308
pywin32-ctypes            0.2.3
qt-material               2.14
requests                  2.32.3
schedule                  1.2.2
scipy                     1.14.1
selenium                  4.26.1
setuptools                75.3.0
six                       1.16.0
sniffio                   1.3.1
sortedcontainers          2.4.0
soupsieve                 2.6
tk                        0.1.0
tomlkit                   0.13.2
trio                      0.27.0
trio-websocket            0.11.1
typing_extensions         4.12.2
tzdata                    2024.2
urllib3                   2.2.3
websocket-client          1.8.0
wheel                     0.44.0
win32-setctime            1.1.0
wsproto                   1.2.0
```

### 基本運行
使用方式：
```cmd=
.\\python-3.11.1\python.exe ./{檔名}.py
```
