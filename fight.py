# check how much damage attacks do
# make fight screen
# make challenge and plead stages (can do this with variable that increments by 1 for each stage and then random dialogue of that stage)
# make spare stages with same thing
# make undynehealth class into just undyne
# make undyne attacks "less extreme" by changing the delay between bullets / bullet speed
# change invincibility to 0 after attacks are done

import pygame
from dialogue import dialogue_gen
from random import randint
from sys import exit
pygame.init()

FPS = pygame.time.Clock()
SCREEN_WIDTH = 1253
SCREEN_HEIGHT = 990
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
events = pygame.event.get()
WHITE = (255, 255, 255)

# assets
fight_img = pygame.image.load('assets\\images\\fight.webp')
fight_img = pygame.transform.scale(fight_img, (220, 84))
act_img = pygame.image.load('assets\\images\\act.webp')
act_img = pygame.transform.scale(act_img, (220, 84))
item_img = pygame.image.load('assets\\images\\item.webp')
item_img = pygame.transform.scale(item_img, (220, 84))
mercy_img = pygame.image.load('assets\\images\\mercy.webp')
mercy_img = pygame.transform.scale(mercy_img, (220, 84))

active_fight_img = pygame.image.load('assets\\images\\active_fight.png')
active_fight_img = pygame.transform.scale(active_fight_img, (220, 84))
active_act_img = pygame.image.load('assets\\images\\active_act.png')
active_act_img = pygame.transform.scale(active_act_img, (220, 84))
active_item_img = pygame.image.load('assets\\images\\active_item.png')
active_item_img = pygame.transform.scale(active_item_img, (220, 84))
active_mercy_img = pygame.image.load('assets\\images\\active_mercy.png')
active_mercy_img = pygame.transform.scale(active_mercy_img, (220, 84))

target_img = pygame.image.load('assets\\images\\target.png')
target_img = pygame.transform.scale(target_img, (1180, 280))

strike1 = pygame.image.load('assets\\images\\strike1.png')
strike1 = pygame.transform.scale(strike1, (10, 15))
strike2 = pygame.image.load('assets\\images\\strike2.png')
strike2 = pygame.transform.scale(strike2, (10, 55))
strike3 = pygame.image.load('assets\\images\\strike3.png')
strike4 = pygame.transform.scale(strike3, (15, 105))
strike4 = pygame.image.load('assets\\images\\strike4.png')
strike4 = pygame.transform.scale(strike4, (20, 160))
strike5 = pygame.image.load('assets\\images\\strike5.png')
strike5 = pygame.transform.scale(strike5, (35, 80))
strike6 = pygame.image.load('assets\\images\\strike6.png')
strike6 = pygame.transform.scale(strike6, (35, 30))

undyne_image = pygame.image.load('assets\\images\\undyne_battle.gif')
undyne_image = pygame.transform.scale(undyne_image, (346, 478))

undyne_image_dark = pygame.image.load('assets\\images\\undyne_battle_dark.png')
undyne_image_dark = pygame.transform.scale(undyne_image_dark, (346, 478))

green_soul = pygame.image.load('assets\\images\\green_soul.webp')
green_soul = pygame.transform.scale(green_soul, (24, 24))

red_soul = pygame.image.load('assets\\images\\green_soul.webp')
red_soul = pygame.transform.scale(red_soul, (24, 24))

bullet_1 = pygame.image.load('assets\\images\\bullet_1.png')
bullet_1 = pygame.transform.scale(bullet_1, (50, 48))
bullet_2 = pygame.image.load('assets\\images\\bullet_2.png')
bullet_2 = pygame.transform.scale(bullet_2, (50, 48))
bullet_3 = pygame.image.load('assets\\images\\bullet_3.png')
bullet_3 = pygame.transform.scale(bullet_3, (50, 48))
bullet_4 = pygame.image.load('assets\\images\\bullet_4.png')
bullet_4 = pygame.transform.scale(bullet_4, (50, 48))
bullet_image_list = [bullet_1, bullet_2, bullet_3, bullet_4]

# text
text_font = pygame.font.Font("assets\\fonts\\Determination Sans.otf", 50)

hp_text_undyne = text_font.render("HP", False, WHITE)
hp_text_undyne_rect = hp_text_undyne.get_rect(topleft = (400, 550))

undyne_attacks = text_font.render("* Undyne Attacks!", False, WHITE)
undyne_attacks_rect = undyne_attacks.get_rect(topleft = (60, 530))

snowpiece_item_consume1 = text_font.render("* You ate the Snowman Piece.", False, WHITE)
snowpiece_item_consume1_rect = snowpiece_item_consume1.get_rect(topleft = (60, 530))

snowpiece_item_consume2 = text_font.render("* You recovered 45 HP!", False, WHITE)
snowpiece_item_consume2_rect = snowpiece_item_consume2.get_rect(topleft = (60, 630))

cinnabun_item_consume1 = text_font.render("* You ate the Cinnamon Bun.", False, WHITE)
cinnabun_item_consume1_rect = cinnabun_item_consume1.get_rect(topleft = (60, 530))

cinnabun_item_consume2 = text_font.render("* You recovered 22 HP!", False, WHITE)
cinnabun_item_consume2_rect = cinnabun_item_consume2.get_rect(topleft = (60, 630))

undyne_check1 = text_font.render("* UNDYNE 7 ATK 0 DEF", False, WHITE)
undyne_check1_rect = undyne_check1.get_rect(topleft = (60, 530))

undyne_check2 = text_font.render("* The heroine that NEVER gives up.", False, WHITE)
undyne_check2_rect = undyne_check2.get_rect(topleft = (60, 630))

mercy_fail_text = text_font.render("* You told Undyne you didn't want to fight.", False, WHITE)
mercy_fail_text_rect = mercy_fail_text.get_rect(topleft = (60, 530))
mercy_fail_text2 = text_font.render("* But nothing happened.", False, WHITE)
mercy_fail_text2_rect = mercy_fail_text2.get_rect(topleft = (60, 630))

mercy_success_text = text_font.render("* You told Undyne you didn't want to fight.", False, WHITE)
mercy_success_text_rect = mercy_success_text.get_rect(topleft = (60, 530))
mercy_success_text2 = text_font.render("* Her attacks slow down.", False, WHITE)
mercy_success_text2_rect = mercy_success_text2.get_rect(topleft = (60, 630))

plead_fail_text = text_font.render("* You told Undyne you didn't want to fight.", False, WHITE)
plead_fail_text_rect = plead_fail_text.get_rect(topleft = (60, 530))
plead_fail_text2 = text_font.render("* But nothing happened.", False, WHITE)
plead_fail_text2_rect = plead_fail_text2.get_rect(topleft = (60, 630))

plead_success_text = text_font.render("* You told Undyne you just want to be friends.", False, WHITE)
plead_success_text_rect = plead_success_text.get_rect(topleft = (60, 530))
plead_success_text2 = text_font.render("* She remembers someone...", False, WHITE)
plead_success_text2_rect = plead_success_text2.get_rect(topleft = (60, 600))
plead_success_text3 = text_font.render("* Her attacks became a little less extreme.", False, WHITE)
plead_success_text3_rect = plead_success_text3.get_rect(topleft = (60, 670))

undyne_challenge_text = text_font.render("* You tell UNDYNE her attacks are too easy.", False, WHITE)
undyne_challenge_text_rect = undyne_challenge_text.get_rect(topleft = (60, 530))

first_challenge_text = text_font.render("* The bullets get faster.", False, WHITE)
first_challenge_text_rect = first_challenge_text.get_rect(topleft = (60, 630))

second_challenge_text = text_font.render("* The bullets get unfair.", False, WHITE)
second_challenge_text_rect = second_challenge_text.get_rect(topleft = (60, 630))

third_challenge_text = text_font.render("* She doesn't care.", False, WHITE)
third_challenge_text_rect = third_challenge_text.get_rect(topleft = (60, 630))

class Button():
    def __init__(self, image, hovering_image, pos, active):
        self.image = image
        self.rect = self.image.get_rect()
        self.pos = pos
        self.hovering_image = hovering_image
        self.active = active
    
    def update(self):
        if self.active:
            screen.blit(self.hovering_image, self.pos)
        else:
            screen.blit(self.image, self.pos)

class TextButton():
    def __init__(self, string, antialiasing, color, hover_color, pos, active):
        self.string = string
        self.text_font = text_font
        self.antialiasing = antialiasing
        self.color = color
        self.pos = pos
        self.text = self.text_font.render(string, antialiasing, color)
        self.text_rect = self.text.get_rect(topleft = (pos))
        self.hovering_text = self.text_font.render(string, antialiasing, hover_color)
        self.hovering_text_rect = self.hovering_text.get_rect(topleft = (pos))
        self.active = active
    
    def update(self):
        if self.active == False:
            screen.blit(self.text, self.pos)
        else:
            screen.blit(self.hovering_text, self.pos)

class Heart(pygame.sprite.Sprite):
    def __init__(self, current_health, maximum_health, heart_color):
        super().__init__()
        self.heart_color = heart_color
        if self.heart_color == "red":
            self.image = red_soul
        elif self.heart_color == "green":
            self.image = green_soul
        self.rect = self.image.get_rect()
        self.current_health = current_health
        self.maximum_health = maximum_health
        self.health_bar_length = 200    
        self.health_ratio = self.maximum_health / self.health_bar_length
        
    def update(self):
        self.healthbar()
        
    def draw(self, pos_x, pos_y):
        self.rect.x = pos_x
        self.rect.y = pos_y
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    def damage(self, amount):
        if self.current_health > 0:
            self.current_health -= amount
        if self.current_health <= 0:
            self.current_health = 0
            
    def heal(self, amount):
        if self.current_health < self.maximum_health:
            self.current_health += amount
        if self.current_health >= self.maximum_health:
            self.current_health = self.maximum_health
    
    def healthbar(self):
        pygame.draw.rect(screen, (255, 0, 0), (575, 816, self.health_bar_length, 40))
        pygame.draw.rect(screen, (255, 255, 64), (575, 816, self.current_health / self.health_ratio, 40))
    
class UndyneHealth():
    def __init__(self, current_health, maximum_health):
        self.current_health = current_health
        self.maximum_health = maximum_health
        self.health_bar_length = 200    
        self.health_ratio = self.maximum_health / self.health_bar_length
    
    def damage(self, amount):
        if self.current_health > 0:
            self.current_health -= amount
        if self.current_health <= 0:
            self.current_health = 0
            
    def heal(self, amount):
        if self.current_health < self.maximum_health:
            self.current_health += amount
        if self.current_health >= self.maximum_health:
            self.current_health = self.maximum_health
    
    def healthbar(self, pos_x, pos_y, height):
        pygame.draw.rect(screen, (255, 0, 0), (pos_x, pos_y, self.health_bar_length, height))
        pygame.draw.rect(screen, (255, 255, 64), (pos_x, pos_y, self.current_health / self.health_ratio, height))
    
class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, direction, speed, speed_multiplier):
        super().__init__()
        global bullet_image_list
        self.direction = direction
        self.image = bullet_image_list[self.direction - 1]
        self.rect = self.image.get_rect(center = (pos_x, pos_y))
        self.speed = speed
        self.speed_multiplier = speed_multiplier
        
    def update(self):
        if self.direction == 2:
            self.rect.y -= round(self.speed * self.speed_multiplier)
        elif self.direction == 1:
            self.rect.y += round(self.speed * self.speed_multiplier)
        elif self.direction == 3:
            self.rect.x += round(self.speed * self.speed_multiplier)
        elif self.direction == 4:
            self.rect.x -= round(self.speed * self.speed_multiplier)
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Shield(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        global up_active, down_active, left_active, right_active
        self.up_active = up_active
        self.down_active = down_active
        self.left_active = left_active
        self.right_active = right_active
        
    def update(self):
        if self.up_active:
            pygame.draw.rect(screen, WHITE, pygame.Rect(575, 475, 100, 5))
            self.rect = pygame.Rect(575, 475, 100, 5)
        elif self.down_active:
            pygame.draw.rect(screen, WHITE, pygame.Rect(575, 575, 100, 5))
            self.rect = pygame.Rect(575, 575, 100, 5)
        elif self.left_active:
            pygame.draw.rect(screen, WHITE, pygame.Rect(575, 475, 5, 100))
            self.rect = pygame.Rect(575, 475, 5, 100)
        elif self.right_active:
            pygame.draw.rect(screen, WHITE, pygame.Rect(675, 475, 5, 100))
            self.rect = pygame.Rect(675, 475, 5, 100)
            
        for event in events:
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_UP:
                    if self.right_active:
                        self.up_active = True
                        self.right_active = False
                    elif self.down_active:
                        self.up_active = True
                        self.down_active = False
                    elif self.left_active:
                        self.up_active = True
                        self.left_active = False
                        
                if event.key == pygame.K_DOWN:
                    if self.right_active:
                        self.down_active = True
                        self.right_active = False
                    elif self.up_active:
                        self.down_active = True
                        self.up_active = False
                    elif self.left_active:
                        self.down_active = True
                        self.left_active = False
                
                if event.key == pygame.K_LEFT:
                    if self.right_active:
                        self.left_active = True
                        self.right_active = False
                    elif self.down_active:
                        self.left_active = True
                        self.down_active = False
                    elif self.up_active:
                        self.left_active = True
                        self.up_active = False
                        
                if event.key == pygame.K_RIGHT:
                    if self.left_active:
                        self.right_active = True
                        self.left_active = False
                    elif self.down_active:
                        self.right_active = True
                        self.down_active = False
                    elif self.up_active:
                        self.right_active = True
                        self.up_active = False

# objects

damage_font = pygame.font.Font("assets\\fonts\\hachicro.ttf", 80)

undyne_text = TextButton("* Undyne", False, WHITE, (255, 255, 64), (150, 550), True)

check_text = TextButton("* Check", False, WHITE, (255, 255, 64), (150, 550), True)
plead_text = TextButton("* Plead", False, WHITE, (255, 255, 64), (650, 550), False)
challenge_text = TextButton("* Challenge", False, WHITE, (255, 255, 64), (150, 650), False)

spare_text = TextButton("* Spare", False, WHITE, (255, 255, 64), (150, 550), True)

snowpiece1_text = TextButton("* SnowPiece", False, WHITE, (255, 255, 64), (150, 550), True)
snowpiece2_text = TextButton("* SnowPiece", False, WHITE, (255, 255, 64), (650, 550), False)
cinnabun1_text = TextButton("* CinnaBun", False, WHITE, (255, 255, 64), (150, 650), False)
cinnabun2_text = TextButton("* CinnaBun", False, WHITE, (255, 255, 64), (650, 650), False)

fight_btn = Button(fight_img, active_fight_img, (30, 876), True)
act_btn = Button(act_img, active_act_img, (363, 876), False)
item_btn = Button(item_img, active_item_img, (683, 876), False)
mercy_btn = Button(mercy_img, active_mercy_img, (1003, 876), False)

bullet_group = pygame.sprite.Group()

def buttonupdates():
    global default, fighting, acting, iteming, mercying
    fight_btn.update()
    act_btn.update()
    item_btn.update()
    mercy_btn.update()
    
    if default:
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    
                    if fight_btn.active:
                        act_btn.active = True
                        fight_btn.active = False
                    
                    elif act_btn.active:
                        item_btn.active = True
                        act_btn.active = False
                        
                    elif item_btn.active:
                        mercy_btn.active = True
                        item_btn.active = False
                        
                    elif mercy_btn.active:
                        fight_btn.active = True
                        mercy_btn.active = False
                
                if event.key == pygame.K_LEFT:
                    
                    if fight_btn.active:
                        mercy_btn.active = True
                        fight_btn.active = False
                    
                    elif act_btn.active:
                        fight_btn.active = True
                        act_btn.active = False
                        
                    elif item_btn.active:
                        act_btn.active = True
                        item_btn.active = False
                        
                    elif mercy_btn.active:
                        item_btn.active = True
                        mercy_btn.active = False
                
                if event.key == pygame.K_RETURN or event.key == pygame.K_z:
                    
                    if fight_btn.active:
                        default = False
                        fighting = True
                        
                    elif act_btn.active:
                        default = False
                        acting = True
                        
                    elif mercy_btn.active:
                        default = False
                        mercying = True
                    
                    elif item_btn.active and len(top_item_list) > 0:
                        default = False
                        iteming = True
                    elif item_btn.active and len(top_item_list) <= 0:
                        default = True
                        fight_btn.active = True
                        item_btn.active = False
                    
def fightbuttonupdates():
    global default, fighting, last_keypress, fight_selected, fighting
    undyne_text.update()
    screen.blit(hp_text_undyne, hp_text_undyne_rect)
    undyne_health.health_bar_length = 200
    undyne_health.healthbar(480, 565, 40)
    undyne_health.health_ratio = undyne_health.maximum_health / undyne_health.health_bar_length
    
    health_ratio_text = text_font.render(f"{undyne_health.current_health} / {undyne_health.maximum_health}", False, WHITE)
    health_ratio_text_rect = health_ratio_text.get_rect(topleft = (700, 550))
    screen.blit(health_ratio_text, health_ratio_text_rect)
    
    last_keypress += 1
    
    for event in events:
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_z and last_keypress >= 20:
                fight_selected = True
                last_keypress = 0
                fight_btn.active = False
                fighting = False
                
            if event.key == pygame.K_x:
                last_keypress = 0
                undyne_text.active = True
                fighting = False
                default = True

def actbuttonupdates():
    global default, acting, checked, last_keypress, challenged, \
            pleaded, challenge_stage, plead_fail, plead_success
    check_text.update()
    plead_text.update()
    challenge_text.update()
    last_keypress += 1
    
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:

                if check_text.active:
                    plead_text.active = True
                    check_text.active = False
                
                elif plead_text.active:
                    check_text.active = True
                    plead_text.active = False
            
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                
                if check_text.active:
                    challenge_text.active = True
                    check_text.active = False
                
                elif challenge_text.active:
                    check_text.active = True
                    challenge_text.active = False
                    
            if event.key == pygame.K_z and last_keypress >= 20:
                
                if check_text.active:
                    checked = True
                    last_keypress = 0
                    act_btn.active = False
                    
                if challenge_text.active:
                    challenged = True
                    last_keypress = 0
                    if challenge_stage <= 3:
                        challenge_stage += 1
                    act_btn.active = False
                
                if plead_text.active:
                    pleaded = True
                    last_keypress = 0
                    if randint(1, 2) == 2:
                        plead_success = True
                    else:
                        plead_fail = True
                    act_btn.active = False
                    
            if event.key == pygame.K_x:
                last_keypress = 0
                check_text.active = True
                challenge_text.active = False
                plead_text.active = False
                acting = False
                default = True
                
def itembuttonupdates():
    global default, iteming, snowpiece1_text, snowpiece2_text, cinnabun1_text, cinnabun2_text, \
            last_keypress, top_item_list, btm_item_list, snowpiece_consumed, cinnabun_consumed

    top_x = 150
    for top_item in top_item_list:
        top_item.pos = (top_x, 550)
        top_item.update()
        top_x += 500
        
    btm_x = 150
    for btm_item in btm_item_list:
        btm_item.pos = (btm_x, 650)
        btm_item.update()
        btm_x += 500
    
    last_keypress += 1
    
    for event in events:
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                
                if len(top_item_list) >= 2:
                    if top_item_list[0].active:
                        top_item_list[1].active = True
                        top_item_list[0].active = False
                
                    elif top_item_list[1].active:
                        top_item_list[0].active = True
                        top_item_list[1].active = False

                if len(btm_item_list) >= 2:
                    if btm_item_list[0].active:
                        btm_item_list[1].active = True
                        btm_item_list[0].active = False
                        
                    elif btm_item_list[1].active:
                        btm_item_list[0].active = True
                        btm_item_list[1].active = False
            
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                
                if len(btm_item_list) >= 1:
                    if top_item_list[0].active:
                        btm_item_list[0].active = True
                        top_item_list[0].active = False
                        
                    elif btm_item_list[0].active:
                        top_item_list[0].active = True
                        btm_item_list[0].active = False
                
                if (len(top_item_list) and len(btm_item_list)) >= 2:
                    if top_item_list[1].active:
                        btm_item_list[1].active = True
                        top_item_list[1].active = False
                    
                    elif btm_item_list[1].active:
                        top_item_list[1].active = True
                        btm_item_list[1].active = False
                    
            if event.key == pygame.K_z and last_keypress >= 20:
                
                if len(top_item_list) >= 1:
                    if top_item_list[0].active:
                        
                        if len(top_item_list) <= 1:
                            top_item_list.pop(0)
                        else:
                            top_item_list[0] = top_item_list[1]
                            
                            if len(btm_item_list) <= 0:
                                top_item_list.pop(1)
                            else:
                                top_item_list[1] = btm_item_list[0]
                                
                                if len(btm_item_list) <= 1:
                                    btm_item_list.pop(0)
                                else:
                                    btm_item_list[0] = btm_item_list[1]
                                    btm_item_list.pop(1)
                        
                        last_keypress = 0
                        player.heal(45)
                        snowpiece_consumed = True
                        item_btn.active = False
                    
                if len(top_item_list) >= 2:
                    if top_item_list[1].active and last_keypress >= 20:
                        if len(top_item_list) >= 2:
                            top_item_list[0] = top_item_list[1]
                            top_item_list.pop(1)
                        else:
                            top_item_list.pop(0)
                        last_keypress = 0
                        player.heal(45)
                        snowpiece_consumed = True
                        item_btn.active = False
                
                if len(btm_item_list) >= 1:
                    if btm_item_list[0].active and last_keypress >= 20:
                        if len(btm_item_list) >= 2:
                            btm_item_list[0] = btm_item_list[1]
                            btm_item_list.pop(1)
                        else:
                            btm_item_list.pop(0)
                        last_keypress = 0
                        player.heal(22)
                        cinnabun_consumed = True
                        item_btn.active = False
                    
                if len(btm_item_list) >= 2:
                    if btm_item_list[1].active and last_keypress >= 20:
                        if len(btm_item_list) >= 2:
                            btm_item_list[0] = btm_item_list[1]
                            btm_item_list.pop(1)
                        else:
                            btm_item_list.pop(0)
                        last_keypress = 0
                        player.heal(22)
                        cinnabun_consumed = True
                        item_btn.active = False
                    
            if event.key == pygame.K_x:
                last_keypress = 0
                snowpiece1_text.active = False
                snowpiece2_text.active = False
                cinnabun1_text.active = False
                cinnabun2_text.active = False
                if len(top_item_list) > 0:
                    top_item_list[0].active = True

                iteming = False
                default = True

def mercybuttonupdates():
    global default, mercying, last_keypress, mercy_success, mercy_fail
    spare_text.update()
    last_keypress += 1
    
    for event in events:
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_z and last_keypress >= 10:
                
                if spare_text.active:
                    last_keypress = 0
                    # 5 is a random number
                    if mercy_stage >= 5:
                        mercy_btn.active = False
                        mercy_success = True
                    else:
                        mercy_btn.active = False
                        mercy_fail = True
                        
            if event.key == pygame.K_x:
                last_keypress = 0
                spare_text.active = True
                mercying = False
                default = True

def fightscreen():
    global events, target_img, bar_x, attack_power, attacked, last_keypress, attack_damage, strike_counter, \
            attack_stage, getting_attacked, fight_selected
    
    screen.blit(target_img, (40, 510))
    if bar_x < 1200:
        pygame.draw.rect(screen, WHITE, pygame.Rect(bar_x, 510, 20, 280))
        
        if attacked == False:
            if bar_x <= 600:
                attack_power += 1
            else:
                attack_power -= 1
    else:
        attack_power = 0
        attacked = True
    
    if attacked == False:
        bar_x += 15
        last_keypress += 1

    if attacked:
        undyne_health.health_bar_length = 400
        undyne_health.healthbar(423, 400, 40)
        pygame.draw.rect(screen, (196, 47, 51), pygame.Rect(570, 270, 250, 90), 0, 3)
        damage_text = damage_font.render(f"{attack_damage}", False, (0, 0, 0))
        damage_text_rect = damage_text.get_rect(topleft = (580, 280))
        screen.blit(damage_text, damage_text_rect)
        undyne_health.health_ratio = undyne_health.maximum_health / undyne_health.health_bar_length
        
        if strike_counter <= 22:
            strike_animation()
        else:
            attack_stage += 1
            getting_attacked = True
            fight_selected = False
            bar_x = 30
            attack_power = 0
            strike_counter = 0
            attacked = False
        
    for event in events:
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_z and last_keypress >= 2:
                
                last_keypress = 0
                attack_damage = attack_power * 5
                undyne_health.damage(attack_damage)
                attacked = True
                
def strike_animation():
    global strike1, strike2, strike3, strike4, strike5, strike6, strike_counter
    strike_counter += 0.25
    if strike_counter >= 2 and strike_counter <= 12:
        screen.blit(strike1, (600, 220))
    if strike_counter >= 4 and strike_counter <= 14:
        screen.blit(strike2, (600, 240))
    if strike_counter >= 6 and strike_counter <= 16:
        screen.blit(strike3, (600, 260))
    if strike_counter >= 8 and strike_counter <= 18:
        screen.blit(strike4, (600, 300))
    if strike_counter >= 10 and strike_counter <= 20:
        screen.blit(strike5, (600, 370))
    if strike_counter >= 12 and strike_counter <= 22:
        screen.blit(strike6, (600, 380))
    
def check():
    global undyne_check1, undyne_check1_rect, undyne_check2, undyne_check2_rect, events, checked, last_keypress, acting, \
            attack_stage, getting_attacked
    screen.blit(undyne_check1, undyne_check1_rect)
    screen.blit(undyne_check2, undyne_check2_rect)
    last_keypress += 1
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z and last_keypress >= 20:
                # actual fight here
                last_keypress = 0
                acting = False
                checked = False
                attack_stage += 1
                getting_attacked = True

def snowpieceitemconsume():
    global snowpiece_item_consume1, snowpiece_item_consume1_rect, snowpiece_item_consume2, \
            snowpiece_item_consume2_rect, events, snowpiece_consumed, last_keypress, iteming, \
            attack_stage, getting_attacked
    
    screen.blit(snowpiece_item_consume1, snowpiece_item_consume1_rect)
    screen.blit(snowpiece_item_consume2, snowpiece_item_consume2_rect)
    last_keypress += 1
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z and last_keypress >= 20:
                # actual fight here
                last_keypress = 0
                iteming = False
                snowpiece_consumed = False
                attack_stage += 1
                getting_attacked = True

def cinnabunitemconsume():
    global cinnabun_item_consume1, cinnabun_item_consume1_rect, cinnabun_item_consume2, \
            cinnabun_item_consume2_rect, events, cinnabun_consumed, last_keypress, iteming, \
            attack_stage, getting_attacked
    
    screen.blit(cinnabun_item_consume1, cinnabun_item_consume1_rect)
    screen.blit(cinnabun_item_consume2, cinnabun_item_consume2_rect)
    last_keypress += 1
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z and last_keypress >= 20:
                # call actual bossfight here
                last_keypress = 0
                iteming = False
                cinnabun_consumed = False
                attack_stage += 1
                getting_attacked = True

def mercyresult():
    global mercy_success, mercy_fail, last_keypress, events, mercy_fail_text, \
            mercy_fail_text_rect, mercy_success_text, mercy_success_text_rect, \
            mercying, mercy_fail_text2, mercy_fail_text2_rect, mercy_success_text2, \
            mercy_success_text2_rect, attack_stage, getting_attacked
            
    if mercy_success:
        # make attacks slower
        screen.blit(mercy_success_text, mercy_success_text_rect)
        screen.blit(mercy_success_text2, mercy_success_text2_rect)
    if mercy_fail:
        screen.blit(mercy_fail_text, mercy_fail_text_rect)
        screen.blit(mercy_fail_text2, mercy_fail_text2_rect)
        
    
    last_keypress += 1
    
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z and last_keypress >= 20:
                # actual fight here
                last_keypress = 0
                mercying = False
                mercy_fail = False
                mercy_success = False
                attack_stage += 1
                getting_attacked = True

def challenge():
    global events, challenged, last_keypress, acting, undyne_challenge_text, undyne_challenge_text_rect, \
            first_challenge_text, first_challenge_text_rect, second_challenge_text, second_challenge_text_rect, \
            third_challenge_text, third_challenge_text_rect, challenge_stage, attack_stage, getting_attacked, \
            speed_multiplier
    
    screen.blit(undyne_challenge_text, undyne_challenge_text_rect)
    if challenge_stage == 1:
        screen.blit(first_challenge_text, first_challenge_text_rect)
    if challenge_stage == 2:
        screen.blit(second_challenge_text, second_challenge_text_rect)
    if challenge_stage == 3:
        screen.blit(third_challenge_text, third_challenge_text_rect)
    
    last_keypress += 1
    
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z and last_keypress >= 20:
                # actual fight here
                last_keypress = 0
                acting = False
                challenged = False
                attack_stage += 1
                getting_attacked = True
                speed_multiplier += 0.4
    
def plead():
    global events, last_keypress, acting, pleaded, plead_success, plead_fail, \
            plead_fail_text, plead_fail_text_rect, plead_success_text, \
            plead_success_text_rect, plead_fail_text2, plead_fail_text2_rect, \
            plead_success_text2, plead_fail_text2_rect, plead_success_text3, \
            plead_success_text3_rect, attack_stage, getting_attacked, speed_multiplier
    
    if plead_success:
        screen.blit(plead_success_text, plead_success_text_rect)
        screen.blit(plead_success_text2, plead_success_text2_rect)
        screen.blit(plead_success_text3, plead_success_text3_rect)
    
    if plead_fail:
        screen.blit(plead_fail_text, plead_fail_text_rect)
        screen.blit(plead_fail_text2, plead_fail_text2_rect)
    
    last_keypress += 1
    
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z and last_keypress >= 20:
                # actual fight here
                if plead_success:
                    speed_multiplier -= 0.2
                last_keypress = 0
                acting = False
                pleaded = False
                plead_fail = False
                plead_success = False
                attack_stage += 1
                getting_attacked = True
    
def undyne_fight():
    global attack_stage, events, player, up_active, down_active, \
        left_active, right_active, bullet_group, invincibility, player_shield, \
        attack_counter, attack_delay, events
            
    player.heart_color = "green"
    pygame.draw.rect(screen, WHITE, pygame.Rect(550, 450, 150, 150), 7)
    player.draw(613, 510)
    pygame.draw.circle(screen, (32, 90, 33), (625, 525), 60, 3)
    player_shield.update()

    invincibility += 1
    
    bullet_group.update()
    
    player_hit = pygame.sprite.spritecollide(player, bullet_group, True)
    pygame.sprite.spritecollide(player_shield, bullet_group, True)

    if player_hit and (invincibility > 4):
        player_hit = None
        player.damage(5)
        invincibility = 0
        
    if len(bullet_group) == 0 and attack_counter > attack_delay:
        attack_finished()
        
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSLASH:
                bullet_group.empty()
                attack_finished()
    
    if attack_stage == 1:
        attack_1()
    elif attack_stage == 2:
        attack_2()

def attack_finished():
    global attack_counter, attack_delay, speed_multiplier, \
    getting_attacked, up_active, down_active, left_active, right_active, \
    invincibility, fight_btn, default, dialogue_generated, dialogue_generated_rect, \
    attack_stage
    
    getting_attacked = False
    up_active = True
    down_active = False
    left_active = False
    right_active = False
    invincibility = 0
    attack_counter = 0
    fight_btn.active = True
    default = True
    
    if player.current_health <= 30:
        dialogue_stage = "low hp"
    elif attack_stage >= 1 and attack_stage <= 5: # 5 is a random number do fix
        dialogue_stage = "neutral"
    elif attack_stage >= 5:
        dialogue_stage = "late"
    
    dialogue_generated = text_font.render(dialogue_gen(dialogue_stage), False, WHITE)
    dialogue_generated_rect = dialogue_generated.get_rect(topleft = (60, 530))
    
def attack_1():
    global bullet_group, attack_counter, attack_delay, speed_multiplier

    attack_counter += 1

    if attack_counter == attack_delay:
        bullet_group.add(Bullet(630, 100, 1, 4, speed_multiplier))
    elif attack_counter == attack_delay * 2:
        bullet_group.add(Bullet(630, 100, 1, 4, speed_multiplier))
    elif attack_counter == attack_delay * 3:
        bullet_group.add(Bullet(630, 100, 1, 4, speed_multiplier))
     
def attack_2():
    global bullet_group, attack_counter, attack_delay, speed_multiplier

    attack_counter += 1
    
    if attack_counter == attack_delay:
        bullet_group.add(Bullet(630, 100, 1, 4, speed_multiplier))
    elif attack_counter == attack_delay * 2:
        bullet_group.add(Bullet(630, 100, 1, 4, speed_multiplier))
    elif attack_counter == attack_delay * 3:
        bullet_group.add(Bullet(100, 520, 3, 4, speed_multiplier))
    elif attack_counter == attack_delay * 4:
        bullet_group.add(Bullet(100, 520, 3, 4, speed_multiplier))
    elif attack_counter == attack_delay * 5:
        bullet_group.add(Bullet(1153, 520, 4, 4, speed_multiplier))
    elif attack_counter == attack_delay * 6:
        bullet_group.add(Bullet(1153, 520, 4, 4, speed_multiplier))
        
def boss_fight():
    pygame.display.set_caption('Choose.')
    global events
    global player, undyne_health
    player = Heart(76, 76, "red")
    undyne_health = UndyneHealth(1500, 1500)
    
    char_font = pygame.font.Font("assets\\fonts\\Determination Mono.otf", 40)
    
    chara_text = char_font.render("Chara", False, WHITE)
    chara_text_rect = chara_text.get_rect(topleft = (30, 816))
    
    lvl_text = char_font.render("LV 15", False, WHITE)
    lvl_text_rect = lvl_text.get_rect(topleft = (280, 816))
    
    hp_text = char_font.render("HP", False, WHITE)
    hp_text_rect = hp_text.get_rect(topleft = (500, 816))
    
    kr_text = char_font.render("KR", False, WHITE)
    kr_text_rect = kr_text.get_rect(topleft = (800, 816))
    
    global top_item_list, btm_item_list
    top_item_list = [snowpiece1_text, snowpiece2_text]
    btm_item_list = [cinnabun1_text, cinnabun2_text]
    
    global fighting, acting, iteming, mercying, undyne_image, text_font, \
            snowpiece_consumed, cinnabun_consumed, default, last_keypress, \
            checked, fight_selected, bar_x, attack_power, attacked, attack_damage, \
            strike_counter, mercy_stage, mercy_success, mercy_fail, challenge_stage, \
            challenged, pleaded, plead_fail, plead_success, attack_stage, getting_attacked, \
            undyne_image_dark, up_active, down_active, left_active, right_active, invincibility, \
            attack_delay, attack_counter, speed_multiplier, dialogue_generated, dialogue_generated_rect, \
            player_shield
    
    default = True
    fighting = False
    acting = False
    iteming = False
    mercying = False
    last_keypress = 0
    snowpiece_consumed = False
    cinnabun_consumed = False
    checked = False
    fight_selected = False
    bar_x = 30
    attack_power = 10
    attacked = False
    attack_damage = 0
    strike_counter = 0
    mercy_stage = 0
    mercy_success = False
    mercy_fail = False
    challenge_stage = 0
    challenged = False
    pleaded = False
    plead_fail = False
    plead_success = False
    attack_stage = 0
    getting_attacked = False
    up_active = True
    down_active = False
    left_active = False
    right_active = False
    invincibility = 0
    attack_delay = 30
    attack_counter = 0
    speed_multiplier = 1
    dialogue_generated = ""
    dialogue_generated_rect = ""
    player_shield = Shield()
    
    while True:
        screen.fill((0, 0, 0))
        screen.blit(chara_text, chara_text_rect)
        screen.blit(lvl_text, lvl_text_rect)
        if default:
            if attack_stage == 0:
                screen.blit(undyne_attacks, undyne_attacks_rect)
            else:
                screen.blit(dialogue_generated, dialogue_generated_rect)
        
        screen.blit(hp_text, hp_text_rect)
        screen.blit(kr_text, kr_text_rect)
        
        health_ratio_text = char_font.render(f"{player.current_health} / {player.maximum_health}", False, WHITE)
        health_ratio_text_rect = health_ratio_text.get_rect(topleft = (875, 816))
        
        screen.blit(health_ratio_text, health_ratio_text_rect)
        if getting_attacked == False:
            pygame.draw.rect(screen, WHITE, pygame.Rect(30, 500, 1193, 300), 5)
            screen.blit(undyne_image, (430, 10))
        else:
            screen.blit(undyne_image_dark, (430, 10))
            undyne_fight()

        buttonupdates()
        if fighting and fight_selected == False:
            fightbuttonupdates()
        if acting and (checked == False and challenged == False and pleaded == False):
            actbuttonupdates()
        
        if iteming and (snowpiece_consumed == False and cinnabun_consumed == False):
            itembuttonupdates()
        
        if mercying and (mercy_success == False and mercy_fail == False):
            mercybuttonupdates()
        
        if fight_selected and not getting_attacked:
            fightscreen()
        if checked:
            check()
        if challenged:
            challenge()
        if pleaded:
            plead()
        if snowpiece_consumed:
            snowpieceitemconsume()
        if cinnabun_consumed:
            cinnabunitemconsume()
        if mercy_success or mercy_fail:
            mercyresult()
        
        player.update()
        
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit(0)
                
        pygame.display.update()
        FPS.tick(60)

boss_fight()