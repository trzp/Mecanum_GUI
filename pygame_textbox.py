import pygame
from pygame.locals import *
import os.path
pygame.font.init()
from pygame_anchors import *
from pygame_button import *
import time

class textbox:
    """
    give thanks to Nearoo on github
    updated by mrtang
    date:2017.7
    version:1.0
    email:mrtang@nudt.edu.cn
    """
    def __init__(self,  root,
                        position,
                        siz = (300,30),
                        anchor = 'lefttop',
                        borderon = 1,
                        bordercolor = (0,0,0),
                        forecolor = (255,255,255,255),
                        textcolor = (0,255,255),
                        cusorcolor = (0,0,0),
                        textfont = 'arial'):

        self.root = root
        self.position = position
        self.siz = siz
        self.anchor = anchor
        self.borderon = borderon
        self.bordercolor = bordercolor
        self.forecolor = forecolor
        self.textcolor = textcolor
        self.cusorcolor = cusorcolor
        self.textfont = textfont
        self.input_string = ''

        self.focused = False
        self.cursor_position = 0
        self.keyrepeat_counters = {} # {event.key: (counter_int, event.unicode)} (look for "***")

        # will not change after created
        self.cursorsurface = pygame.Surface((2,self.siz[1]-2))
        self.cursorsurface.fill(self.cusorcolor)
        self.sur = pygame.Surface(self.siz).convert_alpha()
        self.sur.fill(self.forecolor)

        if not os.path.isfile(self.textfont): self.textfont = pygame.font.match_font(self.textfont)
        self.font_object = pygame.font.Font(self.textfont,self.siz[1]-6)

        self.__place()

    def __place(self):
        text = self.font_object.render(self.input_string,1,self.textcolor)
        blit_p = blit_pos(self.sur,self.position,self.anchor)
        self.sur.fill(self.forecolor)
        self.sur.blit(text,(1,2))
        self.root.blit(self.sur,blit_p)
        if self.borderon:   pygame.draw.rect(self.root,self.bordercolor,pygame.Rect(blit_p,self.siz),1)
        if self.focused and (int(time.clock()/0.5))%2:
            cursor_x_pos = self.font_object.size(self.input_string[:self.cursor_position])[0]
            self.root.blit(self.cursorsurface,(blit_p[0]+cursor_x_pos,blit_p[1]+1))
        self.rect = pygame.Rect(blit_p,self.siz)

    def update(self,events):
        self.__place()
        for event in events:
            if event.type == MOUSEBUTTONUP:
                self.focused = 1 if self.rect.collidepoint(event.pos) else 0
            if event.type == pygame.KEYDOWN and self.focused:
                if event.key == K_BACKSPACE: # FIXME: Delete at beginning of line?
                    self.input_string = self.input_string[:max(self.cursor_position - 1, 0)] + \
                                        self.input_string[self.cursor_position:]
                    self.cursor_position = max(self.cursor_position - 1, 0)

                    
                elif event.key == K_DELETE:
                    self.input_string = self.input_string[:self.cursor_position] + \
                                        self.input_string[self.cursor_position + 1:]

                elif event.key == K_RETURN:
                    return True

                elif event.key == K_RIGHT:
                    # Add one to cursor_pos, but do not exceed len(input_string)
                    self.cursor_position = min(self.cursor_position + 1, len(self.input_string))

                elif event.key == K_LEFT:
                    # Subtract one from cursor_pos, but do not go below zero:
                    self.cursor_position = max(self.cursor_position - 1, 0)

                elif event.key == K_END:
                    self.cursor_position = len(self.input_string)

                elif event.key == K_HOME:
                    self.cursor_position = 0

                else:
                    # If no special key is pressed, add unicode of key to input_string
                    self.input_string = self.input_string[:self.cursor_position] + \
                                        event.unicode + \
                                        self.input_string[self.cursor_position:]
                    self.cursor_position += len(event.unicode) # Some are empty, e.g. K_UP
    @property
    def gettext(self):
        return self.input_string
