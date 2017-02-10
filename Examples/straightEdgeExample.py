#!usr/bin/python
# -*- coding: utf-8 -*-


# 加载模块
from Package.QtEngine import *
from Package.Image import *
from Package.ROI import *
from Package.Overlay import *
from Package.ScriptPlugin import *
from Package.ImageCtrlWnd import *
from Package.StraightEdge import *


class StraightEdgeExample:
    
    imgHandle,windowHandle = c_long(0), c_long(0)
    parentWindowHandle, x, y, width, height = 0, 0, 0, 768, 680

    @staticmethod
    def OnCreate_Event():
        StraightEdgeExample.imgHandle = Image.init()
        Image.read(StraightEdgeExample.imgHandle, r'..\Package\Images\straight_edge.bmp')
        #!<AnyLib: ShareParams>
        StraightEdgeExample.windowHandle = ImageCtrlWnd.create(StraightEdgeExample.parentWindowHandle,
                                                               StraightEdgeExample.x,
                                                               StraightEdgeExample.y,
                                                               StraightEdgeExample.width,
                                                               StraightEdgeExample.height)
        ImageCtrlWnd.displayImage(StraightEdgeExample.windowHandle, StraightEdgeExample.imgHandle)

        ROIHandle = ROI.init()
        OverlayHandle = Overlay.init()
        edgeHandle = StraightEdge.init()
        direction, type, polarity = 0, 0, 2
        #!<AnyLib: InputParams>
        StraightEdge.setDirection(edgeHandle, direction)
        StraightEdge.setType(edgeHandle, type)
        StraightEdge.setPolarity(edgeHandle, polarity)
        def ImageCtrlWnd_OnShapeResizeEvent(wid, ID):
            ImageCtrlWnd.getROI(wid, ID, ROIHandle)
            print ROI.type(ROIHandle)
            if 'rect2' != ROI.type(ROIHandle):
                return
            
            centerX, centerY, width, height, angle = ROI.getRect2(ROIHandle)
            print centerX, centerY, width, height, angle
            startX, startY, endX, endY = StraightEdge.search(edgeHandle, StraightEdgeExample.imgHandle, ROIHandle)
            #!<AnyLib: OutputParams>

            ImageCtrlWnd.clearAllOverlay(wid)
            Overlay.genLine(OverlayHandle, c_double(startX), c_double(startY), c_double(endX), c_double(endY))
            ImageCtrlWnd.drawOverlay(wid, OverlayHandle)
            ImageCtrlWnd.refresh(wid)
         
        ImageCtrlWnd.registeShapeResizeEvent(StraightEdgeExample.windowHandle, ImageCtrlWnd_OnShapeResizeEvent)


    @staticmethod    
    def OnRunning_Event():
        ImageCtrlWnd.displayImage(StraightEdgeExample.windowHandle, StraightEdgeExample.imgHandle)

 
    @staticmethod
    def OnDestory_Event():
        Image.release(StraightEdgeExample.imgHandle)
        ImageCtrlWnd.destory(StraightEdgeExample.windowHandle)
        


#!<AnyLib: Example>
if __name__ == "__main__":
    QtEngine.startup()
    StraightEdgeExample.OnCreate_Event()
    ImageCtrlWnd.looper(StraightEdgeExample.windowHandle)
    StraightEdgeExample.OnDestory_Event()
