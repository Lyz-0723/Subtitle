import pygame
from setting import *
from component.Text import Text
from component.Button import Button


class Timer:
    def __init__(self):
        self.fps = 1000
        self.fps_counter = pygame.USEREVENT + 2
        self.current_time = WORKING_LENGTH
        # self.font = pygame.font.Font('fonts/字体管家方萌.TTF', 120)
        # self.timer_text = self.font.render(f'{self.current_time // 60:02}:{self.current_time % 60:02}', True,
        #                                    DEFAULT_COLOR)
        # self.timer_text_rect = self.timer_text.get_rect(center=(710, 140))
        self.color = DEFAULT_COLOR_GRAY
        self.timer_text = Text('字体管家方萌.TTF', '25:00', 120, (710, 140), self.color)
        self.start_count = False
        self.end = False
        self.state = False

    def animation(self):
        self.current_time -= 1
        # self.timer_text = self.font.render(f'{self.current_time // 60:02}:{self.current_time % 60:02}', True,
        # DEFAULT_COLOR)

    def update_time(self, time):
        self.current_time = time

    def show(self, screen: pygame.Surface):
        if self.current_time >=0 :
            m, s = self.current_time // 60, self.current_time % 60
        else:
            m,s=0,0
            self.color = DEFAULT_COLOR_GRAY
            self.start_count = False #數到0的時候暫停數數，顯示灰色
            self.end = True

        self.timer_text.update(f"{m:02}:{s:02}", self.color)
        self.timer_text.show(screen)
        # screen.blit(self.timer_text, self.timer_text_rect)

    def timer_pressed(self, pos):  # 被按下的瞬間的設定
        print("state = ",self.start_count)
        if self.timer_text.rect.collidepoint(pos):
            self.state = True
            if self.end:
                self.current_time = WORKING_LENGTH
                self.end = False

        else:
            self.state = False

    def timer_compressed(self):  # 按下放開瞬間的讀取_動作集合
        self._count_compressed()

    def _count_compressed(self):
        if self.state:
            if self.current_time == 0 :
                self.current_time = 1500
            self.start_count = not self.start_count
            self.color = DEFAULT_COLOR if self.color == DEFAULT_COLOR_GRAY else DEFAULT_COLOR_GRAY
