from random import randrange as rand
from Testerino import Connection
import pygame, sys


con = Connection()
# Controles:
#       Down - Kubbarnir fara hradar nidur
# Left/Right - Faerir Kubbinn/ana til haegri/vinstri
#         Up - Snyr Kubbunum 90 gradur til haegri
#     Escape - Endar leikinn
#          P - Pasar leikinn
#     Enter - Kubburinn dettur beint nidur

#####################################################  Leikurinn ########################################
cellular_size = 18
dalkar = 10
radir = 22
Manar_a_sek = 30
Sent = False

pygame.init()

pygame.mixer.music.load("tetrisb.mid")

litir = [
    (0, 0, 0),
    (255, 85, 85),
    (100, 200, 115),
    (120, 108, 245),
    (255, 140, 50),
    (50, 120, 52),
    (146, 202, 73),
    (150, 161, 218),
    (35, 35, 35)  # Litur fyrir background grid
]

# Skilgreinir formin a "kubbunum"
tetris_form = [
    [[1, 1, 1],  #***
     [0, 1, 0]], # *

    [[0, 2, 2],  #  **
     [2, 2, 0]], # **

    [[3, 3, 0],  # **
     [0, 3, 3]], #  **

    [[4, 0, 0],  # *
     [4, 4, 4]], # ***

    [[0, 0, 5],  #   *
     [5, 5, 5]], # ***

    [[6, 6, 6, 6]], # ****

    [[7, 7], # **
     [7, 7]] # **
]



def snua_rettsaelis(form):
    return [[form[y][x]
             for y in xrange(len(form))]
            for x in xrange(len(form[0]) - 1, -1, -1)]


def check_collision(spilavollur, form, offset):
    off_x, off_y = offset
    for cy, row in enumerate(form):
        for cx, cell in enumerate(row):
            try:
                if cell and spilavollur[cy + off_y][cx + off_x]:
                    return True
            except IndexError:
                return True
    return False


def remove_dis_row(spilavollur, row):
    del spilavollur[row]
    return [[0 for i in xrange(dalkar)]] + spilavollur


def join_matrixes(mat1, mat2, mat2_off):
    off_x, off_y = mat2_off
    for cy, row in enumerate(mat2):
        for cx, val in enumerate(row):                  # hjalp af netinu ;)
            mat1[cy + off_y - 1][cx + off_x] += val
    return mat1


def nyr_spilavollur():
    spilavollur = [[0 for x in xrange(dalkar)]
             for y in xrange(radir)]
    spilavollur += [[1 for x in xrange(dalkar)]]
    return spilavollur


class GameOfTetris(object):
    def __init__(self):
        global player_name
        pygame.init()
        player_name = raw_input("What is your name?")  # bidur leikmanninn um nafn
        pygame.key.set_repeat(250, 25)
        self.breidd = cellular_size * (dalkar + 6)
        self.haed = cellular_size * radir
        self.rlim = cellular_size * dalkar
        self.bground_grid = [[8 if x % 2 == y % 2 else 0 for x in xrange(dalkar)] for y in xrange(radir)]

        self.default_font = pygame.font.Font(
            pygame.font.get_default_font(), 12)

        self.screen = pygame.display.set_mode((self.breidd, self.haed))
        pygame.event.set_blocked(pygame.MOUSEMOTION)                    #blockar fyrir musina

        self.next_stone = tetris_form[rand(len(tetris_form))]
        self.init_game()

    def gimme_a_new_stone(self):
        self.stone = self.next_stone[:]
        self.next_stone = tetris_form[rand(len(tetris_form))]
        self.stone_x = int(dalkar / 2 - len(self.stone[0]) / 2)
        self.stone_y = 0

        if check_collision(self.spilavollur,
                           self.stone,
                           (self.stone_x, self.stone_y)):
            self.leik_lokid = True

    def init_game(self):
        global player_name
        pygame.mixer.music.play(5)

        self.spilavollur = nyr_spilavollur()
        self.gimme_a_new_stone()
        self.level = 1
        self.score = 0
        self.lines = 0
        pygame.time.set_timer(pygame.USEREVENT + 1, 1000)
        Sent = False

    def disp_msg(self, msg, topleft):
        x, y = topleft
        for line in msg.splitlines():
            self.screen.blit(
                self.default_font.render(
                    line,
                    False,
                    (255, 255, 255),
                    (0, 0, 0)),
                (x, y))
            y += 14

    def center_msg(self, msg):
        for i, line in enumerate(msg.splitlines()):
            msg_image = self.default_font.render(line, False,
                                                 (255, 255, 255), (0, 0, 0))

            msgim_center_x, msgim_center_y = msg_image.get_size()
            msgim_center_x //= 2
            msgim_center_y //= 2

            self.screen.blit(msg_image, (
                self.breidd // 2 - msgim_center_x,
                self.haed // 2 - msgim_center_y + i * 22))

    def teikna_voll(self, vollur, offset):
        off_x, off_y = offset
        for y, row in enumerate(vollur):
            for x, val in enumerate(row):
                if val:
                    pygame.draw.rect(
                        self.screen,
                        litir[val],
                        pygame.Rect(
                            (off_x + x) *
                            cellular_size,
                            (off_y + y) *
                            cellular_size,
                            cellular_size,
                            cellular_size), 0)

    def add_cl_lines(self, n):
        linescores = [0, 40, 100, 300, 1200]
        self.lines += n
        self.score += linescores[n] * self.level
        if self.lines >= self.level * 6:
            self.level += 1
            newdelay = 1000 - 50 * (self.level - 1)
            newdelay = 100 if newdelay < 100 else newdelay
            pygame.time.set_timer(pygame.USEREVENT + 1, newdelay)

    def move(self, delta_x):
        if not self.leik_lokid and not self.paused:
            new_x = self.stone_x + delta_x
            if new_x < 0:
                new_x = 0
            if new_x > dalkar - len(self.stone[0]):
                new_x = dalkar - len(self.stone[0])
            if not check_collision(self.spilavollur,
                                   self.stone,
                                   (new_x, self.stone_y)):
                self.stone_x = new_x

    def enda_leik(self):
        self.center_msg("Endar leik...")
        pygame.display.update()
        sys.exit()

    def drop(self, manual):
        if not self.leik_lokid and not self.paused:
            self.score += 1 if manual else 0
            self.stone_y += 1
            if check_collision(self.spilavollur,
                               self.stone,
                               (self.stone_x, self.stone_y)):
                self.spilavollur = join_matrixes(
                    self.spilavollur,
                    self.stone,
                    (self.stone_x, self.stone_y))
                self.gimme_a_new_stone()
                hreinsadar_radir = 0
                while True:
                    for i, row in enumerate(self.spilavollur[:-1]):
                        if 0 not in row:
                            self.spilavollur = remove_dis_row(
                                self.spilavollur, i)
                            hreinsadar_radir += 1
                            break
                    else:
                        break
                self.add_cl_lines(hreinsadar_radir)
                return True
        return False

    def insta_drop(self):
        if not self.leik_lokid and not self.paused:
            while (not self.drop(True)):
                pass

    def rotate_stone(self):
        if not self.leik_lokid and not self.paused:
            gimme_a_new_stone = snua_rettsaelis(self.stone)
            if not check_collision(self.spilavollur,
                                   gimme_a_new_stone,
                                   (self.stone_x, self.stone_y)):
                self.stone = gimme_a_new_stone

    def toggle_pause(self):
        self.paused = not self.paused

######### Run the goddamn game already -Mani ;) ###################################
    def start_game(self):
        if self.leik_lokid:
            self.init_game()
            self.leik_lokid = False

    def run(self):
        global player_name, player_score, Sent
        key_actions = {
            'ESCAPE': self.enda_leik,
            'LEFT': lambda: self.move(-1),
            'RIGHT': lambda: self.move(+1),
            'DOWN': lambda: self.drop(True),
            'UP': self.rotate_stone,
            'p': self.toggle_pause,
            'SPACE': self.start_game,
            'RETURN': self.insta_drop # thetta er enter takkinn,
        }

        self.leik_lokid = False
        self.paused = False

        plz_no_lag = pygame.time.Clock()
        while 1:
            self.screen.fill((0, 0, 0))
            if self.leik_lokid:
                self.center_msg("""Leik Lokid!\nStigin thin: %d
Yttu a space til ad halda afram eda\n ESCAPE til ad enda leik""" % self.score)
                if Sent == False:
                    player_score = self.score
                    con.InsertExample(player_name, player_score)
                    Sent = True

            else:
                if self.paused:
                    self.center_msg("""Leikur pasadur
                    Yttu a 'p' til ad halda afram""")
                else:
                    pygame.draw.line(self.screen,
                                     (255, 255, 255),
                                     (self.rlim + 1, 0),
                                     (self.rlim + 1, self.haed - 1))
                    self.disp_msg("Next up:", (self.rlim + cellular_size, 2))
                    self.disp_msg("Stig: %d\n\nBord: %d\
\nLinur: %d" % (self.score, self.level, self.lines),
                                  (self.rlim + cellular_size, cellular_size * 5))
                    self.teikna_voll(self.bground_grid, (0, 0))
                    self.teikna_voll(self.spilavollur, (0, 0))
                    self.teikna_voll(self.stone,
                                     (self.stone_x, self.stone_y))
                    self.teikna_voll(self.next_stone,
                                     (dalkar + 1, 2))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.USEREVENT + 1:
                    self.drop(False)
                elif event.type == pygame.QUIT:
                    self.enda_leik()
                elif event.type == pygame.KEYDOWN:
                    for key in key_actions:
                        if event.key == eval("pygame.K_"
                                                     + key):
                            key_actions[key]()

            plz_no_lag.tick(Manar_a_sek)


if __name__ == '__main__':
    Leikur = GameOfTetris()
    Leikur.run()
