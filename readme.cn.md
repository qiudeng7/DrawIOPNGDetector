# drawio.png detector

简体中文 | [English](./readme.md)

问题背景是，我不想让windows使用普通的图片查看器打开.drawio.png，但是windows又无法区分.drawio.png和.png。

于是我做了一个python脚本，想让windows通过它打开png文件，脚本来检测文件的结尾是.png还是.drawio.png，如果是.drawio.png，就用drawio打开它。

但问题是windows设置默认应用时，不太好直接设置一条命令（windows设置里不行，也许注册表里可以，但是我不想改注册表）。

于是我把这个脚本通过pyinstaller做成一个exe，我们可以通过`app_path.txt`文件来设置drawio.exe和默认PNG查看器的位置。

## 使用

你可以在release下载到压缩包，压缩包包含一个run.exe和_internal文件夹，这是通过pyinstaller打包生成的，我不确定这个exe是否在别人的电脑上可以正常工作，如果不能，你可能需要重新使用pyinstaller打包。

下载之后解压压缩包，_internal目录下有一个`app_path.txt`，文件内容需要包含两行：
- 第一行：你的drawio.exe的路径
- 第二行：你的默认PNG查看器的路径

然后你就可以通过run.exe来打开.png文件了，如果是普通的.png，他会使用`app_path.txt`第二行指定的应用打开，如果是.drawio.png，他会使用`app_path.txt`第一行指定的应用去打开。

## 重新打包

如果release中下载的exe不能在你的电脑上正常运行，你需要用pyinstaller重新打包:

（其实我也不太会用pyinstaller 这些命令是AI告诉我的，在我的电脑上成功实现了我的需求）

```bash
pip install pyinstaller
pyinstaller --onedir --windowed run.py
```

然后`./dist/run`目录下就是我在release中发布的东西了，你需要在`_internal`目录下自行创建`app_path.txt`文件，并按照上述格式填写两行路径。