import sys
import pygame

from setting import *

from component.Background import Background
from component.Button import Button
from component.Player import Player
from component.Search import Search
from component.Timer import Timer


class Game:
    def __init__(self):
        pygame.init()
        # pygame.scrap.init()
        # pygame.scrap.set_mode(pygame.SCRAP_CLIPBOARD)

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Subtitle')
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.search = Search()
        self.background = Background()
        self.timer = Timer()

    def run(self):
        btn_music_list = Button("musiclist", (80, 80), (120, 120))
        # btn_music = Button("music", (80, 80), (190, 120))
        btn_next = Button("next", (60, 60), (1060, 150))
        # btn_clock = Button("clock",(80, 80),(190,120))

        pygame.time.set_timer(pygame.USEREVENT, self.background.fps)
        pygame.time.set_timer(pygame.USEREVENT + 1, self.player.song_name.fps)
        pygame.time.set_timer(pygame.USEREVENT + 2, self.timer.fps)

        t = pygame.time.get_ticks()
        get_ticks_last_frame = t

        self.player.change_song(
            "musics/deeper.mp3")

        while True:
            t = pygame.time.get_ticks()
            delta_time = (t - get_ticks_last_frame) / 1000.0
            get_ticks_last_frame = t

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == self.background.fps_counter:
                    self.background.animation()

                if event.type == self.player.song_name.fps_counter:
                    self.player.song_name.animation()

                if event.type == self.timer.fps_counter:
                    if self.timer.start_count:
                        self.timer.animation()
                    else:
                        pass

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.player.player_pressed(event.pos)
                    self.timer.timer_pressed(event.pos)
                    if self.search.search_pressed(event.pos):
                        self.player._active = False
                    else:
                        self.player._active = True

                if event.type == pygame.MOUSEBUTTONUP:
                    self.player.player_compressed()
                    self.search.search_compressed()
                    self.timer.timer_compressed()

                if event.type == pygame.MOUSEMOTION:
                    # print(event.pos)
                    self.player.player_mov(event.pos)

                if event.type == pygame.KEYDOWN:
                    self.search.search_bar_key_down(event)

            self.background.load_bg_img(self.screen)
            btn_music_list.show(self.screen)

            btn_next.show(self.screen)

            self.timer.show(self.screen)
            self.player.show(self.screen, delta_time)
            self.search.show(self.screen)
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
