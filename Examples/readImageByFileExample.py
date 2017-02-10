#!usr/bin/python
# -*- coding: utf-8 -*-


# 加载模块
from Package.QtEngine import *
from Package.Image import *
from Package.ImageCtrlWnd import *


class ReadImageByFileExample:
    
    imgHandle,windowHandle = c_long(0), c_long(0)
    parentWindowHandle, x, y, width, height = 0, 0, 0, 768, 680
    imageFilePath = r'D:\Image\WD\FL130130-R-01 WD-5mm.bmp'

    @staticmethod
    def OnCreate_Event():
        ReadImageByFileExample.imgHandle = Image.init()
        #!<AnyLib: InputParams>
        Image.read(ReadImageByFileExample.imgHandle, ReadImageByFileExample.imageFilePath)
        print ReadImageByFileExample.imageFilePath
        #!<AnyLib: ShareParams>
        ReadImageByFileExample.windowHandle = ImageCtrlWnd.create(ReadImageByFileExample.parentWindowHandle,
                                                                  ReadImageByFileExample.x,
                                                                  ReadImageByFileExample.y,
                                                                  ReadImageByFileExample.width,
                                                                  ReadImageByFileExample.height)
        ImageCtrlWnd.displayImage(ReadImageByFileExample.windowHandle, ReadImageByFileExample.imgHandle)

        
    @staticmethod
    def OnRunning_Event():
        #!<AnyLib: InputParams>
        Image.read(ReadImageByFileExample.imgHandle, ReadImageByFileExample.imageFilePath)
        ImageCtrlWnd.displayImage(ReadImageByFileExample.windowHandle, ReadImageByFileExample.imgHandle)


    @staticmethod
    def OnDestory_Event():
        Image.release(imgHandle)
        ImageCtrlWnd.destory(windowHandle)


#!<AnyLib: Example>
if __name__ == "__main__":
    QtEngine.startup()
    ReadImageByFileExample.OnCreate_Event()
    ReadImageByFileExample.OnRunning_Event()
    ImageCtrlWnd.looper(ReadImageByFileExample.windowHandle)
