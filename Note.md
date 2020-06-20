# Development Notes
## QT Compiler
`Could not start process "make" qmake_all`:
`sudo apt-get install build-essential`
<!--via https://blog.csdn.net/qq_25116371/article/details/86230538 -->
Linux Qt cannot find -lGL:
```bash
#查找 libGL 所在位置
[root@localhost ~]# locate libGL
/usr/lib64/libGL.so
/usr/lib64/libGL.so.1
/usr/lib64/libGL.so.1.2.0
/usr/share/doc/mesa-libGL-9.2.5
/usr/share/doc/mesa-libGL-9.2.5/COPYING
#创建链接
[root@localhost ~]# ln -s /usr/lib64/libGL.so.1 /usr/lib/libGL.so
```
<!--Via http://c.biancheng.net/view/3901.html-->

`GL/gl.h: No such file or directory # include && cannot find -lGL`:
`sudo apt-get install mesa-common-dev`
<!--Via https://blog.csdn.net/u012689588/article/details/16950089?utm_source=blogxgwz5-->
## QT Creator
Convert LCD component to Digital component inherited from LCD class:
1. promoted widgets
2. Base name: lCD...
3. promoted name:Digital Clock(Loaded Digital.h in example proj preiously)
4. Also:`#include<QTime> #include <QTimer>`
5. See Source Code for more datail.

