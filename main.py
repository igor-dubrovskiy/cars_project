import math
import pygame


class main_menu:
    def main_menu(self):
        map_choose_btn = pygame.Rect(40, 20, 300, 73)
        maraphon_btn = pygame.Rect(40, 100, 300, 73)
        settings_btn = pygame.Rect(40, 180, 300, 73)
        escape_btn = pygame.Rect(40, 260, 300, 73)
        arrow_right_btn = pygame.Rect(435, 165, 70, 70)
        arrow_right_im = pygame.image.load('images/arrow_right.png')
        arrow_left_btn = pygame.Rect(0, 165, 70, 70)
        arrow_left_im = pygame.image.load('images/arrow_left.png')
        start_btn = pygame.Rect(160, 345, 180, 41)
        start_im = pygame.image.load('images/start_im.png')
        menu = pygame.image.load('images/menu.png')
        fon = pygame.image.load('images/fon.png')
        control_im = pygame.image.load('images/control_im.png')
        clock = pygame.time.Clock()
        fps = 50
        pygame.display.set_caption("Главное меню")
        running = True
        map_choose = False
        settings = False
        self.maraphon = False
        width = 500
        height = 500
        window = pygame.display.set_mode((width, height))
        while running:
            window.fill((0, 0, 0))
            window.blit(fon, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if settings is False:
                        if map_choose is False:
                            if maraphon_btn.collidepoint(event.pos):
                                self.maraphon = True
                                self.win_count_1 = 0
                                self.win_count_2 = 0
                                self.game_args()
                                self.game()
                                running = False
                            if map_choose_btn.collidepoint(event.pos):
                                map_choose = True
                            if settings_btn.collidepoint(event.pos):
                                settings = True
                            if escape_btn.collidepoint(event.pos):
                                exit()
                        if start_btn.collidepoint(event.pos):
                            self.game_args()
                            self.game()
                            running = False
                        if arrow_left_btn.collidepoint(event.pos):
                            self.map_count -= 1
                        if arrow_right_btn.collidepoint(event.pos):
                            self.map_count += 1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        map_choose = False
                        settings = False
                        window = pygame.display.set_mode((width, height))
                        self.map_count = 0
                if map_choose:
                    window.blit(arrow_right_im, (430, 165))
                    window.blit(arrow_left_im, (0, 165))
                    try:
                        window.blit(pygame.transform.scale(self.maps[self.map_count], (350, 250)), (75, 65))
                    except Exception:
                        if self.map_count < 0:
                            self.map_count = -1
                        else:
                            self.map_count = 0
                    window.blit(start_im, (160, 345))
                elif settings:
                    window = pygame.display.set_mode((1440, 880))
                    window.blit(control_im, (0, 0))
                else:
                    window.blit(menu, (0, 0))
                pygame.display.update()
                clock.tick(fps)


class Game(main_menu):
    def __init__(self):
        pygame.init()
        self.bg = (255, 255, 255)
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Arial', 35)
        self.myfont_2 = pygame.font.SysFont('Arial', 300)
        self.myfont_3 = pygame.font.SysFont('Arial', 50)
        pygame.mixer.init()
        # фоновая музыка
        pygame.mixer.music.load("sounds/fon_music.mp3")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1, 0.0)
        self.maps_append()
        self.main_menu()

    # создаем перечнь карт
    def maps_append(self):
        self.dct = {1: [3, 1, (705, 40)], 2: [5, 2, (815, 50)], 3: [4, 2, (780, 20)], 4: [6, 2, (760, 50)],
                    5: [6, 2, (792, 50)]}
        self.maps = []
        for i in range(1, 6):
            map = 'images/track_' + str(i) + '.png'
            self.maps.append(pygame.image.load(map))
        self.map_count = 0

    # все(почти) переменные использующиеся в коде
    def game_args(self):
        # звуки
        self.expl_sound = pygame.mixer.Sound('sounds/explosion_sound.mp3')
        self.expl_sound.set_volume(0.2)
        self.start_sound = pygame.mixer.Sound('sounds/start_sound.mp3')
        self.start_sound.set_volume(0.2)
        self.otchet_sound = pygame.mixer.Sound('sounds/otshet_ot_5.mp3')
        self.otchet_sound.set_volume(0.2)
        self.race_finish = pygame.mixer.Sound('sounds/race_finish.mp3')
        self.race_finish.set_volume(0.2)
        self.maraphon_finish = pygame.mixer.Sound('sounds/maraphon_finish.mp3')
        self.maraphon_finish.set_volume(0.2)

        self.fps = 50
        self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Mashinki")
        self.window.fill(self.bg)

        road = (100, 100, 100, 255)
        self.barrier = (255, 0, 0, 255)
        self.finish = (255, 255, 0, 255)
        self.chekpoint = (88, 88, 88)
        self.full_speed_all = []
        self.full_speed_all.append(self.chekpoint)
        self.full_speed_all.append(road)

        self.player_1 = pygame.Rect(self.dct[self.maps.index(self.maps[self.map_count]) + 1][2][0],
                                    self.dct[self.maps.index(self.maps[self.map_count]) + 1][2][1], 50, 28)
        self.image_1 = pygame.image.load("images/car_1.png")
        self.player_2 = pygame.Rect(self.dct[self.maps.index(self.maps[self.map_count]) + 1][2][0],
                                    self.dct[self.maps.index(self.maps[self.map_count]) + 1][2][1] + 30, 50, 28)
        self.image_2 = pygame.image.load("images/car_2.png")

        self.explosion = pygame.image.load("images/explosion.png")
        self.cup = pygame.image.load('images/cup.png')
        self.game_stat = pygame.image.load('images/game_stat.png')
        self.win_mass = pygame.image.load('images/win_mass.png')
        self.pause_menu_im = pygame.image.load('images/pause_menu.png')
        self.game_stat.set_colorkey((255, 255, 255))
        self.in_menu_btn = pygame.Rect(300, 75, 620, 440)
        self.exit_btn = pygame.Rect(300, 75, 620, 565)

        # перменнная игрок 1
        self.forward_1 = False
        self.left_1 = False
        self.right_1 = False
        self.back_1 = False

        self.speed_1 = 0
        self.ankel_1 = 0
        self.destroy_1 = 0
        self.destroy_count_1 = 0
        self.chekpoint_1 = 0
        self.round_1 = 0
        self.start_1 = False
        self.finish_1 = False

        # перменнная игрок 2
        self.forward_2 = False
        self.left_2 = False
        self.right_2 = False
        self.back_2 = False

        self.speed_2 = 0
        self.ankel_2 = 0
        self.destroy_2 = 0
        self.destroy_count_2 = 0
        self.chekpoint_2 = 0
        self.round_2 = 0
        self.start_2 = False
        self.finish_2 = False

        # общие переменные
        self.victory = None
        self.pause = False
        self.mvsp = 10
        self.ankel_ch = 0.7
        self.game_start = False

        self.start_sound.play()

    # функция просто изменяет победное окно если "марафон" окончен
    def maraphon_end(self):
        self.maraphon_finish.play()
        window = pygame.display.set_mode((1440, 880))
        if self.win_count_1 > self.win_count_2:
            win = 1
        else:
            win = 2
        running = True
        while running:
            window.fill((0, 0, 0))
            window.blit(self.cup, (602, 335))
            window.blit(self.win_mass, (0, 720))
            window.blit(self.myfont_3.render('Победил игрок ' + str(win), False, (255, 255, 0)), (600, 620))
            window.blit(self.myfont_3.render('Со счетом ' + str(self.win_count_1) + ':' +
                                             str(self.win_count_2), False, (255, 255, 0)), (600, 680))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.main_menu()
                        running = False
            pygame.display.update()

    # сама игра
    def game(self):
        start_ticks = pygame.time.get_ticks()
        s = 0
        s_1 = 0
        countdown = 3
        pause_time = 0
        width, height = 1440, 880
        running = True
        finish_sound = False
        end_sound = False
        clock = pygame.time.Clock()
        while running:
            window = pygame.display.set_mode((width, height))
            # остонавливаем ход времени если пауза
            if self.pause is False:
                current_time = pygame.time.get_ticks() - pause_time
            else:
                pause_time = pygame.time.get_ticks() - current_time
            # возрождение игрока на начальной позиции при смерти
            if self.destroy_1 == 1:
                self.player_1.left = self.dct[self.maps.index(self.maps[self.map_count]) + 1][2][0]
                self.player_1.top = self.dct[self.maps.index(self.maps[self.map_count]) + 1][2][1]
                self.destroy_1 = 0
            if self.destroy_2 == 1:
                self.player_2.left = self.dct[self.maps.index(self.maps[self.map_count]) + 1][2][0]
                self.player_2.top = self.dct[self.maps.index(self.maps[self.map_count]) + 1][2][1] + 28
                self.destroy_2 = 0
            # клавиши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # действия в паузе
                if self.pause:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.in_menu_btn.collidepoint(event.pos):
                            self.main_menu()
                        elif self.exit_btn.collidepoint(event.pos):
                            exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        # если не конец игры ставим на паузу
                        if self.victory is None:
                            self.start_sound.stop()
                            self.otchet_sound.stop()
                            self.pause = not self.pause
                        # если конец игры но "марафон" -- запускаем следущую карту
                        elif self.victory and self.maraphon:
                            if self.victory == 1:
                                self.win_count_1 += 1
                            else:
                                self.win_count_2 += 1
                            self.map_count += 1
                            if self.map_count == 5:
                                self.maraphon_end()
                                break
                            else:
                                self.game_args()
                                self.game()
                        # если конец игры -- выходи в главное меню
                        else:
                            self.main_menu()
                    if self.game_start:
                        if self.pause is False:
                            if event.key == pygame.K_UP:
                                self.forward_1 = True
                            if event.key == pygame.K_LEFT:
                                self.left_1 = True
                            if event.key == pygame.K_RIGHT:
                                self.right_1 = True
                            if event.key == pygame.K_DOWN:
                                self.back_1 = True

                            if event.key == pygame.K_w:
                                self.forward_2 = True
                            if event.key == pygame.K_a:
                                self.left_2 = True
                            if event.key == pygame.K_d:
                                self.right_2 = True
                            if event.key == pygame.K_s:
                                self.back_2 = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.forward_1 = False
                    if event.key == pygame.K_LEFT:
                        self.left_1 = False
                    if event.key == pygame.K_RIGHT:
                        self.right_1 = False
                    if event.key == pygame.K_DOWN:
                        self.back_1 = False

                    if event.key == pygame.K_w:
                        self.forward_2 = False
                    if event.key == pygame.K_a:
                        self.left_2 = False
                    if event.key == pygame.K_d:
                        self.right_2 = False
                    if event.key == pygame.K_s:
                        self.back_2 = False

            window.fill((0, 0, 0))
            window.blit(self.maps[self.map_count], (0, 0))

            # игрок 1
            if self.destroy_1 == 0:
                if self.forward_1 and self.speed_1 < self.mvsp:
                    self.speed_1 += 0.1
                if self.back_1:
                    self.speed_1 -= 0.1

                if self.left_1 and self.speed_1 > 2:
                    self.ankel_1 -= self.ankel_ch * self.speed_1
                elif self.left_1 and self.speed_1 < -2:
                    self.ankel_1 -= self.ankel_ch * self.speed_1

                if self.right_1 and self.speed_1 > 2:
                    self.ankel_1 += self.ankel_ch * self.speed_1
                elif self.right_1 and self.speed_1 < -2:
                    self.ankel_1 += self.ankel_ch * self.speed_1

                if self.forward_1 is False and self.speed_1 > 0:
                    self.speed_1 -= 0.1
                if self.back_1 is False and self.speed_1 < 0:
                    self.speed_1 += 0.1
                # вычисляем на сколько должен повернуться персонаж
                d_x_1 = math.cos(math.radians(self.ankel_1)) * self.speed_1
                d_y_1 = math.sin(math.radians(self.ankel_1)) * self.speed_1
                self.player_1.left += round(d_x_1)
                self.player_1.top += round(d_y_1)
                image_1_neu = pygame.transform.rotate(self.image_1, self.ankel_1 * -1)
            # Обнаружение столкновения игрока 1
            if self.destroy_1 == 0:
                try:
                    # если едем не по дороге -- приписываем штраф к скорости
                    if window.get_at(self.player_1.center) not in self.full_speed_all:
                        if self.speed_1 > 3:
                            self.speed_1 = 2
                        if self.speed_1 < -3:
                            self.speed_1 = -2
                    # авария
                    if window.get_at((self.player_1.left, self.player_1.top)) == self.barrier or \
                            window.get_at((self.player_1.right, self.player_1.bottom)) == self.barrier:
                        self.destroy_1 = 1
                        self.expl_sound.play()
                    # финишная черта -- проверяем прошли ли через все контрольные точки
                    if window.get_at((self.player_1.left, self.player_1.top)) == self.finish or \
                            window.get_at((self.player_1.right, self.player_1.bottom)) == self.finish or \
                            window.get_at(self.player_1.center) == self.finish:
                        if self.start_1 is False:
                            start_time_1 = current_time
                            self.start_1 = True
                        if self.dct[self.maps.index(self.maps[self.map_count]) + 1][0] <= self.chekpoint_1:
                            self.chekpoint_1 = 0
                            self.round_1 += 1
                    # контрольный пункт
                    if window.get_at(self.player_1.center) == self.chekpoint:
                        self.chekpoint_1 += 1
                    # меняем позицию игрока если не взорвался
                    if self.destroy_1 == 0:
                        window.blit(image_1_neu, self.player_1)
                    else:
                        self.chekpoint_1 = 0
                # если вышли за край карты
                except Exception:
                    self.expl_sound.play()
                    self.destroy_1 = 1

            else:
                window.blit(self.explosion, self.player_1)

            # игрок 2
            if self.destroy_2 == 0:
                if self.forward_2 and self.speed_2 < self.mvsp:
                    self.speed_2 += 0.1
                if self.back_2:
                    self.speed_2 -= 0.1

                if self.left_2 and self.speed_2 > 2:
                    self.ankel_2 -= self.ankel_ch * self.speed_2
                elif self.left_2 and self.speed_2 < -2:
                    self.ankel_2 -= self.ankel_ch * self.speed_2

                if self.right_2 and self.speed_2 > 2:
                    self.ankel_2 += self.ankel_ch * self.speed_2
                elif self.right_2 and self.speed_2 < -2:
                    self.ankel_2 += self.ankel_ch * self.speed_2

                if self.forward_2 is False and self.speed_2 > 0:
                    self.speed_2 -= 0.1
                if self.back_2 is False and self.speed_2 < 0:
                    self.speed_2 += 0.1
                # вычисляем на сколько должен повернуться персонаж
                d_x_2 = math.cos(math.radians(self.ankel_2)) * self.speed_2
                d_y_2 = math.sin(math.radians(self.ankel_2)) * self.speed_2
                self.player_2.left += round(d_x_2)
                self.player_2.top += round(d_y_2)
                image_2_neu = pygame.transform.rotate(self.image_2, self.ankel_2 * -1)

            # Обнаружение столкновения игрока 2
            if self.destroy_2 == 0:
                try:
                    # если едем не по дороге -- приписываем штраф к скорости
                    if window.get_at(self.player_2.center) not in self.full_speed_all:
                        if self.speed_2 > 3:
                            self.speed_2 = 2
                        if self.speed_2 < -3:
                            self.speed_2 = -2
                    # авария
                    if window.get_at((self.player_2.left, self.player_2.top)) == self.barrier or \
                            window.get_at((self.player_2.right, self.player_2.bottom)) == self.barrier:
                        self.destroy_2 = 1
                        self.expl_sound.play()
                    # финишная черта -- проверяем прошли ли через все контрольные точки
                    if window.get_at((self.player_2.left, self.player_2.top)) == self.finish or \
                            window.get_at((self.player_2.right, self.player_2.bottom)) == self.finish or \
                            window.get_at(self.player_2.center) == self.finish:
                        if self.start_2 is False:
                            self.start_time_2 = current_time
                            self.start_2 = True
                        if self.dct[self.maps.index(self.maps[self.map_count]) + 1][0] <= self.chekpoint_2:
                            self.chekpoint_2 = 0
                            self.round_2 += 1
                    # контрольный пункт
                    if window.get_at(self.player_2.center) == self.chekpoint:
                        self.chekpoint_2 += 1
                # если вышли за край карты
                except Exception:
                    self.expl_sound.play()
                    self.destroy_2 = 1

                if self.destroy_2 == 0:
                    window.blit(image_2_neu, self.player_2)
                else:
                    self.chekpoint_2 = 0
            else:
                window.blit(self.explosion, self.player_2)

            # проверяем не финишировал ли кто-нибудь
            if self.dct[self.maps.index(self.maps[self.map_count]) + 1][1] <= self.round_1:
                self.finish_1 = True
            if self.dct[self.maps.index(self.maps[self.map_count]) + 1][1] <= self.round_2:
                self.finish_2 = True

            # если взорвались
            if self.destroy_1 == 1:
                window.blit(self.explosion, self.player_1)
                pygame.display.update()
                self.ankel_1 = 0
                self.destroy_count_1 += 1
            if self.destroy_2 == 1:
                window.blit(self.explosion, self.player_2)
                pygame.display.update()
                self.ankel_2 = 0
                self.destroy_count_2 += 1

            # кто финищировал первым
            if self.finish_1 or self.finish_2:
                if finish_sound is False:
                    finish_sound = True
                    self.otchet_sound.play()
                if self.finish_1 and self.finish_2 is False:
                    vict = 1
                elif self.finish_2 and self.finish_1 is False:
                    vict = 2
                # если все успели проехать гонку
                else:
                    self.otchet_sound.stop()
                    self.victory = vict
                # обратный отсчет
                seconds = (current_time - start_ticks) / 1000  # сколько секунд
                if seconds >= 1:
                    start_ticks = current_time
                    s_1 += 1
                elif s_1 >= 5:
                    if s_1 == 5:
                        self.victory = vict
                else:
                    window.blit(self.myfont_2.render(str(5 - s_1), False, (0, 0, 255)), (648, 268))

            if self.victory is None:
                # статистика во время игры
                window.blit(self.game_stat, (0, 0))
                if self.pause:
                    window.blit(self.pause_menu_im, (520, 190))
                window.blit(self.myfont.render(str(self.round_1) + '/' +
                                               str(self.dct[self.maps.index(self.maps[self.map_count]) + 1][1]), False,
                                               (255, 0, 0)), (45, 40))
                window.blit(self.myfont.render(str(self.destroy_count_1), False, (255, 0, 0)), (205, 40))
                if self.start_1 is True:
                    if self.pause is False and self.victory is None:
                        if self.finish_1 is False:
                            time_1 = current_time - start_time_1
                    window.blit(self.myfont.render(str(time_1 // 60000) + ':' + str((time_1 // 1000) % 60) + ':' +
                                                   str(time_1 % 1000)[0:-1], False, (255, 0, 0)), (100, 40))
                window.blit(self.myfont.render(str(self.destroy_count_2), False, (255, 0, 0)), (205, 95))
                window.blit(self.myfont.render(str(self.round_2) + '/' +
                                               str(self.dct[self.maps.index(self.maps[self.map_count]) + 1][1]), False,
                                               (255, 0, 0)), (45, 95))
                if self.start_2 is True:
                    if self.pause is False and self.victory is None:
                        if self.finish_2 is False:
                            time_2 = current_time - self.start_time_2
                    window.blit(self.myfont.render(str(time_2 // 60000) + ':' + str((time_2 // 1000) % 60) + ':' +
                                                   str(time_2 % 1000)[0:-1], False, (255, 0, 0)), (100, 95))
            if not self.pause:
                # стартовый отсчет
                seconds = (current_time - start_ticks) / 1000  # сколько секунд
                if seconds >= 1:
                    start_ticks = current_time
                    s += 1
                elif s >= countdown:
                    self.game_start = True
                    if s == countdown:
                        window.blit(self.myfont_2.render('Старт!', False, (255, 0, 0)), (448, 268))
                else:
                    window.blit(self.myfont_2.render(str(countdown - s), False, (255, 0, 0)), (648, 268))
                if self.maraphon:
                    window.blit(self.myfont_3.render('Счет:  ' + str(self.win_count_1) + ':' + str(self.win_count_2),
                                                     False, (255, 0, 0)), (1200, 20))
                # если игра закончилсь -- "победное окно"
                if self.victory is not None:
                    if end_sound is False:
                        self.race_finish.play()
                        end_sound = True
                    window.fill((0, 0, 0))
                    window.blit(self.cup, (602, 335))
                    window.blit(self.win_mass, (0, 720))
                    window.blit(self.myfont.render('Победил игрок ' + str(self.victory), False, (255, 255, 0)),
                                (610, 720))
                    if self.finish_1 is False:
                        n_f = 1
                        time_1 = '----'
                    elif self.finish_2 is False:
                        n_f = 2
                        time_2 = '----'
                    try:
                        if self.victory == 1:
                            window.blit(self.myfont.render('Время игрока 1' + ': ' + str(time_1 // 60000)
                                                           + ':' + str((time_1 // 1000) % 60) + ':' +
                                                           str(time_1 % 1000), False, (255, 255, 0)), (610, 620))
                            window.blit(self.myfont.render('Время игрока 2' + ': ' + str(time_2 // 60000)
                                                           + ':' + str((time_2 // 1000) % 60) + ':' +
                                                           str(time_2 % 1000), False, (255, 255, 0)), (610, 660))
                        else:
                            window.blit(self.myfont.render('Время игрока 2' + ': ' + str(time_2 // 60000)
                                                           + ':' + str((time_2 // 1000) % 60) + ':' +
                                                           str(time_2 % 1000), False, (255, 255, 0)), (610, 620))
                            window.blit(self.myfont.render('Время игрока 1' + ': ' + str(time_1 // 60000)
                                                           + ':' + str((time_1 // 1000) % 60) + ':'
                                                           + str(time_1 % 1000), False, (255, 255, 0)), (610, 660))
                    except Exception:
                        window.blit(self.myfont.render('Время игрока' + str(n_f) + ': ----'
                                                       , False, (255, 255, 0)), (610, 660))
            pygame.display.update()
            clock.tick(self.fps)
        pygame.quit()


if __name__ == '__main__':
    Game()
