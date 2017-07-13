import pygame
from pygame.locals import *
import os.path
pygame.font.init()
from pygame_anchors import *

class button:
    """
    author:mrtang
    date:2017.7
    version:1.0
    email:mrtang@nudt.edu.cn
    """
    def __init__(self,  root,
                        position,
                        anchor = 'center',
                        size = (200,30),
                        bordercolor = (0,0,0),
                        forecolor = (255,255,255,255),
                        textcolor = (0,255,255),
                        textfont = 'arial',
                        textsize = 28,
                        text = 'button1',
                        enable = True):

        
        self.root = root
        self.position = position
        self.anchor = anchor
        self.size = size
        self.bordercolor = bordercolor
        self.forecolor = forecolor
        self.textcolor = textcolor
        self.textfont = textfont
        self.textsize = textsize
        self.enable = enable
        self.text = text

        self.focused = False

        if not os.path.isfile(self.textfont): self.textfont = pygame.font.match_font(self.textfont)
        self.font_object = pygame.font.Font(self.textfont,self.textsize)

    def __place(self):
        caption = self.font_object.render(self.text,1,self.textcolor)
        btsur = pygame.Surface(self.size).convert_alpha()
        btsur.fill(self.forecolor)
        btsur.blit(caption,blit_pos(caption,[0.5*i for i in self.size],'center'))   #blit caption on the center of the button surface
        bp = blit_pos(btsur,self.position,self.anchor)
        self.root.blit(btsur,bp)
        self.rect = pygame.Rect(bp,btsur.get_size())
        if self.focused:    borderwidth = 2
        else:               borderwidth = 1
        pygame.draw.rect(self.root,self.bordercolor,self.rect,borderwidth)


    def update(self,ev,callback=None,args=None):
        self.__place()
        if self.enable:
            if self.rect.collidepoint(pygame.mouse.get_pos()):  self.focused = 1
            else:                                               self.focused = 0

            for e in ev:
                if e.type == MOUSEBUTTONUP and self.focused:
                    if not callback == None:
                        if not args==None:  callback(args)
                        else:               callback()