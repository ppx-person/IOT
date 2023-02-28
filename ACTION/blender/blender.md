
# 技巧
* 在Edit->Preference中打开python tooltip，鼠标悬浮在对应的控件上，就会显示对应的python代码是什么。

* 安装包
import sys
sys.exec_prefix
.\bin\python.exe -m pip install <你要安装的python module> --target=.\lib\site-packages
如果不指定
这里，--target后面指定了site-packages目录为Blender安装位置下的site-packages。
如果不指定，那么pip会安装到C:\Users\<用户>\AppData\Roaming\Python中的site-packages，
而这个目录在blender启动时是不会加载的，你会发现尽管直接启动python.exe可能正常import，
但在blender中import会报Module Not Found（一个解决办法是import sys，
然后sys.path.insert(0, <AppData\Roaming的site-packages目录>)，之后可以import，但就比较麻烦）
