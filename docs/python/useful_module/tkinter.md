# tkinter实现python的UI界面设计

更新日期：2019-7-9

作者：尹超



## 前言

## 打开文件对话框并获取文件名

```
import tkinter
from tkinter import filedialog

def openfiles2():
    s2fname = filedialog.askopenfilename(title='打开S2文件', filetypes=[('S2out', '*.out'), ('All Files', '*')])
    print(s2fname)
def openfilecgns():
    cgnsfname = filedialog.askopenfilename(title='打开CGNS文件',filetypes=[('CGNSdat', '*.dat'), ('All Files', '*')] )
    print(cgnsfname)
 
root = tkinter.Tk()
#root.geometry('500x300+500+200')
btn1 = tkinter.Button(root, text='打开S2文件',font =("宋体",20,'bold'),width=13,height=8, command=openfiles2)
btn2 = tkinter.Button(root, text='打开CGNS文件',font = ('宋体',20,'bold'),width=13,height=8, command=openfilecgns)
 
btn1.pack(side='left')
btn2.pack(side='left')
root.mainloop()
```



## 实现拖拽功能

备注：此功能目前只支持全英文路径，如有中文路径会变成乱码

tkinter不支持拖拽功能，需要相关插件来支持，根据网上资料所述，目前有一个叫TkinterDnD的插件可以实现。其中tkdnd是拖拽功能的主体实现，TkinterDnD2是tkdnd的一层API封装，更方便用户使用。想要使用该功能还需要费一番力气~

### 环境搭建

1. 先依次下载tkdnd和[TkinterDnD2](https://sourceforge.net/projects/tkinterdnd/)的资源

2. 再安装（以anaconda为例）

- 把tkdnd2.4拷贝到`Anaconda3\tcl\`路径下（python.exe平级目录）
- 把TkinerDnD2拷贝到`Anaconda3\Library\lib\site-packages`

备注：此处尤其注意两点：

- 请确认自己的系统是x86还是x64的，X64的系统不支持最新tkdnd2.8，那个是x86的包，只能找2.4版本的tndnd（支持x64）
- 请把源码包中的TkinterDnD2子文件夹单独拷贝出来，主文件夹不仅有源码，还有sample测试工程，直接拷贝TkinterDnD2-0.3主文件夹是不起作用的）

### 拖拽功能demo

在搭建好tkdnd环境后可以直接上代码测试了

```
import sys
if sys.version_info[0] == 2:
    from Tkinter import *
else:
    from tkinter import *
from TkinterDnD2 import *

class tk_drag:
    def __init__(self):
        self.root = TkinterDnD.Tk()
        self.entry_sv = StringVar()
        self.entry_sv.set('Drop Here...')
        self.entry = Entry(self.root, textvar=self.entry_sv, width=80)
        self.entry.pack(fill=X, padx=10, pady=10)
        self.entry.drop_target_register(DND_FILES)
        self.entry.dnd_bind('<<Drop>>', self.drop)
        
    def drop(self, event):
        # 拖拽事件的处理函数
        self.entry_sv.set(event.data)
        print(event.data) #拖拽事件获得的文件名
    
    def run(self):
        self.root.mainloop()
```

### 更详细的参考链接

[How to Install and Use TkDnD with Python 2.7 Tkinter on OSX?](https://stackoverflow.com/questions/25427347/how-to-install-and-use-tkdnd-with-python-2-7-tkinter-on-osx)

[python drag and drop explorer files to tkinter entry widget](https://stackoverflow.com/questions/14267900/python-drag-and-drop-explorer-files-to-tkinter-entry-widget)

