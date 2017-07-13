#author:mrtang
#date:2017.7
#version:1.0
#email:mrtang@nudt.edu.cn

anchors ={ 'lefttop':       (0,0),
           'left':    (0,-0.5),
           'leftbottom':    (0,-1),
           'righttop':      (-1,0),
           'right':   (-1,-0.5),
           'rightbottom':   (-1,-1),
           'top':           (-0.5,0),
           'bottom':        (-0.5,-1),
           'center':        (-0.5,-0.5)}

def blit_pos(surface,position,anchor):
    if anchors.has_key(anchor):
        x,y = position
        w,h = surface.get_size()
        s1,s2 = anchors[anchor]
        return map(int,[x+s1*w,y+s2*h])
    else:
        return position