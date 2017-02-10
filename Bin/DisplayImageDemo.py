#!usr/bin/python
# -*- coding: utf-8 -*-

# 加载模块
from Package.QtEngine import *
from Package.Image import *
from Package.ImageCtrlWnd import *

# 启动Qt引擎
QtEngine.startup()

# 读取图片
imgHandle = Image.init()
Image.read(imgHandle, r'../Package/Images/tools.png')
print 'image width=%d'%Image.width(imgHandle)

# 在控件上显示图片
windowHandle = ImageCtrlWnd.create(0, 0, 0, 768, 512)
ImageCtrlWnd.displayImage(windowHandle, imgHandle)

# Qt消息循环
QtEngine.looper()

# 销毁控件对象
ImageCtrlWnd.destory(windowHandle)


