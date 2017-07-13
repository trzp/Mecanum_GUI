import pygame
from pygame.locals import *
import os.path
pygame.font.init()
from pygame_anchors import *
from pygame_button import *

class label:
    """
    author:mrtang
    date:2017.7
    version:1.0
    email:mrtang@nudt.edu.cn
    """
    def __init__(self,  root,
                        position,
                        anchor = 'center',
                        borderon = 0,
                        bordercolor = (0,0,0),
                        forecolor = (255,255,255,255),
                        textcolor = (0,255,255),
                        textfont = 'arial',
                        textsize = 28,
                        text = 'label1',
                        visible = True):

        self.root = root
        self.position = position
        self.anchor = anchor
        self.borderon = borderon
        self.bordercolor = bordercolor
        self.forecolor = forecolor
        self.textcolor = textcolor
        self.textfont = textfont
        self.textsize = textsize
        self.text = text
        self.visible = visible

        if not os.path.isfile(self.textfont): self.textfont = pygame.font.match_font(self.textfont)
        self.font_object = pygame.font.Font(self.textfont,self.textsize)

        self.__place()

    def __place(self):
        if self.visible:
            caption = self.font_object.render(self.text,1,self.textcolor)
            blit_p = blit_pos(caption,self.position,self.anchor)
            self.siz = caption.get_size()
            if self.forecolor[3]==0:
                self.root.blit(caption,blit_p)
            else:
                sur = pygame.Surface(self.siz).convert_alpha()
                sur.fill(self.forecolor)
                sur.blit(caption,(0,0))
                self.root.blit(sur,blit_p)
            if self.borderon:
                pygame.draw.rect(self.root,self.bordercolor,pygame.Rect(blit_p,self.siz),1)

    def update(self):
        self.__place()

    def getsize(self):
        return self.siz