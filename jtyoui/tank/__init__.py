import random
import sys
import time
import pygame
from urllib.request import urlretrieve
import os

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 700
MY_TANK_SPEED = 4
MY_BIRTH_LEFT, MY_BIRTH_TOP = SCREEN_WIDTH / 2, SCREEN_HEIGHT - 60
img = pygame.image
music = pygame.mixer.music
DIRECTION = [U, D, L, R] = ['U', 'D', 'L', 'R']

url = 'https://raw.githubusercontent.com/jtyoui/logo/master/img/'


def load_img(name_img):
    save = 'C:\\tank_img' + os.sep + name_img + '.gif'
    if not os.path.exists(save):
        urlretrieve(url + name_img + '.gif', save)
    return img.load(save)


def load_music(name_music):
    save = 'C:\\tank_img' + os.sep + name_music + '.wav'
    if not os.path.exists(save):
        urlretrieve(url + name_music + '.wav', save)
    music.load(save)
    music.play()


class TankGame:
    my_bullet_list = list()
    enemy_bullet_list = list()
    enemy_tank_list = list()
    wall_list = list()

    def __init__(self):
        if not os.path.exists('C:\\tank_img'):
            os.makedirs('C:\\tank_img')
        pygame.init()
        pygame.font.init()
        self.display = pygame.display
        self.window = self.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT], pygame.RESIZABLE, 32)
        self.display.set_caption('坦克世界')
        self.my_tank = MyTank(MY_BIRTH_LEFT, MY_BIRTH_TOP, self.window)
        self.creat_enemy_number = 10
        self.my_tank_lift = 3
        self.creat_enemy(self.creat_enemy_number)
        self.creat_walls()
        self.font = pygame.font.SysFont('kai_ti', 18)
        self.number = 1

    def creat_enemy(self, number):
        for _ in range(number):
            left = random.randint(0, SCREEN_WIDTH - self.my_tank.tank_width)
            enemy_tank = EnemyTank(left, 20, self.window)
            TankGame.enemy_tank_list.append(enemy_tank)

    def creat_walls(self):
        for i in range(SCREEN_WIDTH // 60 + 1):
            wall_h = random.randint(100, 500)
            w = Wall(60 * i, wall_h, self.window)
            TankGame.wall_list.append(w)

    @staticmethod
    def show_walls():
        for w in TankGame.wall_list:
            if w.live:
                w.display_wall()
            else:
                TankGame.wall_list.remove(w)

    def start_game(self):
        load_music('start')
        while True:
            self.window.fill([0, 0, 0])
            self.get_event()
            len_enemy = len(TankGame.enemy_tank_list)
            self.window.blit(
                self.draw_text('敌方坦克*{0},我方生命值*{1},当前{2}关'.format(len_enemy, self.my_tank_lift, self.number)), (10, 10))
            if len_enemy == 0:
                self.creat_enemy_number += 10
                self.number += 1
                self.my_tank_lift += 1
                self.creat_enemy(self.creat_enemy_number)
                self.wall_list.clear()
                self.creat_walls()
            self.show_my_tank()
            self.show_enemy_tank()
            self.show_bullet(TankGame.enemy_bullet_list)
            self.show_bullet(TankGame.my_bullet_list)
            self.show_walls()
            self.display.update()
            time.sleep(0.02)

    def show_my_tank(self):
        if self.my_tank.live:
            self.my_tank.display()
            self.my_tank.tank_collide_tank()
            self.my_tank.tank_collide_wall()
        else:
            Explode(self.my_tank, self.window).display_explode()
            del self.my_tank
            if self.my_tank_lift == 0:
                self.end_game()
            self.my_tank_lift -= 1
            load_music('add')
            self.my_tank = MyTank(MY_BIRTH_LEFT, MY_BIRTH_TOP, self.window)
        if not self.my_tank.move_stop:
            self.my_tank.move(self.my_tank.direction)

    def show_enemy_tank(self):
        for e in TankGame.enemy_tank_list:
            e.random_move()
            e.tank_collide_wall()
            if e.live:
                e.display()
            else:
                TankGame.enemy_tank_list.remove(e)
                Explode(e, self.window).display_explode()
            e.random_fire()

    def show_bullet(self, ls):
        for b in ls:
            b.bullet_move()
            b.bullet_collide_wall()
            if ls is TankGame.my_bullet_list:
                b.hit_enemy_tank()
                b.bullet_collide_bullet()
            else:
                b.hit_my_tank(self.my_tank)
            if b.live:
                b.display_bullet()
            else:
                ls.remove(b)

    def get_event(self):
        global SCREEN_WIDTH, SCREEN_HEIGHT
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.VIDEORESIZE:
                SCREEN_WIDTH, SCREEN_HEIGHT = event.size
                self.window = self.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT], pygame.RESIZABLE, 32)

            if event.type == pygame.QUIT:
                self.end_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.my_tank.direction = U
                elif event.key == pygame.K_s:
                    self.my_tank.direction = D
                elif event.key == pygame.K_a:
                    self.my_tank.direction = L
                elif event.key == pygame.K_d:
                    self.my_tank.direction = R
                else:
                    return None
                self.my_tank.move_stop = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if len(TankGame.my_bullet_list) < 3:
                    bullet = self.my_tank.fire()
                    load_music('fire')
                    TankGame.my_bullet_list.append(bullet)
            elif event.type == pygame.KEYUP:
                self.my_tank.move_stop = True

    def end_game(self):
        self.display.quit()
        sys.exit()

    def draw_text(self, content):
        text_sf = self.font.render(content, True, [255, 0, 0])
        return text_sf


class BaseItem(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


class Tank(BaseItem):
    def __init__(self, left, top, window, image, direction, speed):
        super().__init__()
        self.window = window
        self.load_image = image
        self.direction = direction
        self.img = self.load_image[self.direction]
        self.rect = self.img.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.speed = speed
        self.tank_width = self.rect.width
        self.tank_height = self.rect.height
        self.wall_switch = False
        self.move_stop = True
        self.live = True
        self.old_left = 0
        self.old_top = 0

    def fire(self):
        return Bullet(self, self.window)

    def display(self):
        self.img = self.load_image[self.direction]
        self.window.blit(self.img, self.rect)

    def wall_not(self, direction):
        if direction == U:
            return self.rect.top > 0
        elif direction == D:
            return self.rect.top <= SCREEN_HEIGHT - self.tank_height
        elif direction == L:
            return self.rect.left > 0
        else:
            return self.rect.left <= SCREEN_WIDTH - self.tank_width

    def wall_yes(self, direction):
        if direction == U:
            if self.rect.top < 0:
                self.rect.top = SCREEN_HEIGHT
        elif direction == D:
            self.rect.top %= SCREEN_HEIGHT
        elif direction == L:
            if self.rect.left < 0:
                self.rect.left = SCREEN_WIDTH
        else:
            self.rect.left %= SCREEN_WIDTH

    def move(self, direction):
        self.old_left = self.rect.left
        self.old_top = self.rect.top
        if self.wall_switch:
            self.wall_yes(direction)
        elif not self.wall_not(direction):
            return None
        if direction == U:
            self.rect.top -= self.speed
        elif direction == D:
            self.rect.top += self.speed
        elif direction == L:
            self.rect.left -= self.speed
        else:
            self.rect.left += self.speed

    def stay(self):
        self.rect.left = self.old_left
        self.rect.top = self.old_top

    def tank_collide_wall(self):
        for wall in TankGame.wall_list:
            if pygame.sprite.collide_rect(self, wall):
                self.stay()

    def tank_collide_tank(self):
        for tank in TankGame.enemy_tank_list:
            if pygame.sprite.collide_rect(self, tank):
                self.stay()


class MyTank(Tank):
    def __init__(self, left, top, window):
        self.img = dict(U=load_img('p2tankU'), D=load_img('p2tankD'), L=load_img('p2tankL'), R=load_img('p2tankR'))
        super().__init__(left, top, window, self.img, U, MY_TANK_SPEED)


class EnemyTank(Tank):
    def __init__(self, left, top, window):
        self.img1 = dict(U=load_img('enemy1U'), D=load_img('enemy1D'), L=load_img('enemy1L'), R=load_img('enemy1R'))
        self.img2 = dict(U=load_img('enemy2U'), D=load_img('enemy2D'), L=load_img('enemy2L'), R=load_img('enemy2R'))
        self.img3 = dict(U=load_img('enemy3U'), D=load_img('enemy3D'), L=load_img('enemy3L'), R=load_img('enemy3R'))
        self.img31 = dict(U=load_img('enemy3U_1'), D=load_img('enemy3D_1'), L=load_img('enemy3L_1'),
                          R=load_img('enemy3R_1'))
        self.img32 = dict(U=load_img('enemy3U_2'), D=load_img('enemy3D_2'), L=load_img('enemy3L_2'),
                          R=load_img('enemy3R_2'))
        # 不同的坦克击中的次数不一样
        image, self.click_count, speed = random.choice([(self.img1, 1, 4), (self.img3, 3, 3), (self.img2, 1, 5)])
        super().__init__(left, top, window, image, self.random_direction(), speed)
        self.step = 100

    @staticmethod
    def random_direction():
        n = random.randint(0, 3)
        return DIRECTION[n]

    def random_move(self):
        if self.step == 0:
            self.direction = self.random_direction()
            self.step = random.randint(10, 100)
        else:
            self.move(self.direction)
            self.step -= 1

    def random_fire(self):
        if random.randint(0, 50) == 1 and len(TankGame.enemy_bullet_list) < 30:
            enemy_bullet = self.fire()
            TankGame.enemy_bullet_list.append(enemy_bullet)


class Bullet(BaseItem):
    def __init__(self, tank, window):
        super().__init__()
        self.direction = tank.direction
        self.speed = tank.speed * 3
        self.img = load_img('bullet')
        self.rect = self.img.get_rect()
        self.window = window
        self.live = True
        if self.direction == U:
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top - self.rect.height
        elif self.direction == D:
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.height
        elif self.direction == L:
            self.rect.left = tank.rect.left - self.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.height / 2 - self.rect.height / 2
        else:
            self.rect.left = tank.rect.left + tank.rect.width
            self.rect.top = tank.rect.top + tank.rect.height / 2 - self.rect.height / 2

    def display_bullet(self):
        self.window.blit(self.img, self.rect)

    def bullet_move(self):
        if self.direction == U:
            if self.rect.top > 0:
                self.rect.top -= self.speed
                return
        elif self.direction == D:
            if self.rect.top < SCREEN_HEIGHT:
                self.rect.top += self.speed
                return
        elif self.direction == L:
            if self.rect.left > 0:
                self.rect.left -= self.speed
                return
        else:
            if self.rect.left < SCREEN_WIDTH:
                self.rect.left += self.speed
                return
        self.live = False

    def hit_enemy_tank(self):
        for enemy in TankGame.enemy_tank_list:
            hit = pygame.sprite.collide_rect(self, enemy)
            if hit:
                self.live = False
                if enemy.click_count == 1:
                    enemy.live = False
                    return None
                enemy.click_count -= 1
                if enemy.click_count == 2:
                    enemy.load_image = enemy.img32
                if enemy.click_count == 1:
                    enemy.load_image = enemy.img31
                load_music('hit')

    def hit_my_tank(self, tank):
        hit = pygame.sprite.collide_rect(self, tank)
        if hit:
            self.live = False
            tank.live = False

    def bullet_collide_wall(self):
        for wall in TankGame.wall_list:
            result = pygame.sprite.collide_rect(self, wall)
            if result:
                self.live = False
                if wall.count == 1:
                    wall.live = False
                else:
                    load_music('hit')

    def bullet_collide_bullet(self):
        for bullet in TankGame.enemy_bullet_list:
            if pygame.sprite.collide_rect(bullet, self):
                bullet.live = False
                self.live = False


class Explode(BaseItem):
    def __init__(self, tank, window):
        super().__init__()
        self.img = [load_img('blast0'), load_img('blast1'), load_img('blast2'), load_img('blast3'), load_img('blast4'),
                    load_img('blast5')]
        self.rect = tank.rect
        self.stop = 0
        self.window = window
        self.rect.left = tank.rect.left - tank.rect.width / 2

    def display_explode(self):
        load_music('blast')
        while self.stop < len(self.img):
            self.window.blit(self.img[self.stop], self.rect)
            self.stop += 1


class Wall(BaseItem):
    def __init__(self, left, top, window):
        super().__init__()
        self.count = random.randint(0, 1)
        self.img = [load_img('steels'), load_img('walls')][self.count]
        self.rect = self.img.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.window = window
        self.live = True

    def display_wall(self):
        self.window.blit(self.img, self.rect)


if __name__ == '__main__':
    g = TankGame()
    g.start_game()
