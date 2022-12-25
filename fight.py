# check how much damage attacks do
# make fight screen
# make challenge and plead stages (can do this with variable that increments by 1 for each stage and then random dialogue of that stage)
# make spare stages with same thing


import pygame, random, sys
pygame.init()

FPS = pygame.time.Clock()
SCREEN_WIDTH = 1253
SCREEN_HEIGHT = 990
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
events = pygame.event.get()
WHITE = (255, 255, 255)

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
    def __init__(self, current_health, maximum_health):
        super().__init__()
        self.image = pygame.image.load('assets\\images\\red_soul.webp')
        self.rect = self.image.get_rect()
        self.current_health = current_health
        self.maximum_health = maximum_health
        self.health_bar_length = 200    
        self.health_ratio = self.maximum_health / self.health_bar_length
        
    def update(self):
        self.healthbar()
    
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
    
    def healthbar(self):
        pygame.draw.rect(screen, (255, 0, 0), (480, 565, self.health_bar_length, 40))
        pygame.draw.rect(screen, (255, 255, 64), (480, 565, self.current_health / self.health_ratio, 40))
    
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
                    
                    elif item_btn.active:
                        default = False
                        iteming = True
                        
                    elif mercy_btn.active:
                        default = False
                        mercying = True

def fightbuttonupdates():
    global default, fighting, last_keypress, fight_selected, fighting
    undyne_text.update()
    screen.blit(hp_text_undyne, hp_text_undyne_rect)
    undyne_health.healthbar()
    
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
    global default, acting, checked, last_keypress
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

                elif challenge_text.active:
                    pass
            
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
                    pass
                
                if plead_text.active:
                    pass
                    
            if event.key == pygame.K_x:
                last_keypress = 0
                check_text.active = True
                challenge_text.active = False
                plead_text.active = False
                acting = False
                default = True
                
def itembuttonupdates():
    global default, iteming, snowpiece1_text, snowpiece2_text, cinnabun1_text, cinnabun2_text
    global last_keypress, top_item_list, btm_item_list
    global snowpiece_consumed, cinnabun_consumed

    top_x = 150
    for top_item in top_item_list:
        top_item.pos = (top_x, 550)
        top_item.update()
        top_x += 500
        print(top_item_list)
        
    btm_x = 150
    for btm_item in btm_item_list:
        btm_item.pos = (btm_x, 650)
        btm_item.update()
        btm_x += 500
        print(btm_item_list)
    
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
                top_item_list[0].active = True

                iteming = False
                default = True

def mercybuttonupdates():
    global default, mercying
    spare_text.update()
    
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                spare_text.active = True
                mercying = False
                default = True

def attackscreen():
    global events
    
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                # add attack here
                pass

def check():
    global undyne_check1, undyne_check1_rect, undyne_check2, undyne_check2_rect, events, checked, last_keypress, acting
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

def snowpieceitemconsume():
    global snowpiece_item_consume1, snowpiece_item_consume1_rect, snowpiece_item_consume2, snowpiece_item_consume2_rect, events, snowpiece_consumed, last_keypress, iteming
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

def cinnabunitemconsume():
    global cinnabun_item_consume1, cinnabun_item_consume1_rect, cinnabun_item_consume2, cinnabun_item_consume2_rect, events, cinnabun_consumed, last_keypress, iteming
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

def boss_fight():
    pygame.display.set_caption('Fight!')
    global events
    global player, undyne_health
    player = Heart(76, 76)
    undyne_health = UndyneHealth(1500, 1500)
    
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
    
    global fight_btn, act_btn, item_btn, mercy_btn
    fight_btn = Button(fight_img, active_fight_img, (30, 876), True)
    act_btn = Button(act_img, active_act_img, (363, 876), False)
    item_btn = Button(item_img, active_item_img, (683, 876), False)
    mercy_btn = Button(mercy_img, active_mercy_img, (1003, 876), False)
    
    char_font = pygame.font.Font("assets\\fonts\\Determination Mono.otf", 40)
    
    chara_text = char_font.render("Chara", False, WHITE)
    chara_text_rect = chara_text.get_rect(topleft = (30, 816))
    
    lvl_text = char_font.render("LV 15", False, WHITE)
    lvl_text_rect = lvl_text.get_rect(topleft = (280, 816))
    
    hp_text = char_font.render("HP", False, WHITE)
    hp_text_rect = hp_text.get_rect(topleft = (500, 816))
    
    kr_text = char_font.render("KR", False, WHITE)
    kr_text_rect = kr_text.get_rect(topleft = (800, 816))
    
    global text_font
    text_font = pygame.font.Font("assets\\fonts\\Determination Sans.otf", 50)
    
    global hp_text_undyne, hp_text_undyne_rect
    hp_text_undyne = text_font.render("HP", False, WHITE)
    hp_text_undyne_rect = hp_text.get_rect(topleft = (400, 550))
    
    undyne_attacks = text_font.render("* Undyne Attacks!", False, WHITE)
    undyne_attacks_rect = undyne_attacks.get_rect(topleft = (60, 530))
    
    global snowpiece_item_consume1, snowpiece_item_consume1_rect
    snowpiece_item_consume1 = text_font.render("* You ate the Snowman Piece.", False, WHITE)
    snowpiece_item_consume1_rect = snowpiece_item_consume1.get_rect(topleft = (60, 530))
    
    global snowpiece_item_consume2, snowpiece_item_consume2_rect
    snowpiece_item_consume2 = text_font.render("* You recovered 45 HP!", False, WHITE)
    snowpiece_item_consume2_rect = snowpiece_item_consume2.get_rect(topleft = (60, 630))
    
    global cinnabun_item_consume1, cinnabun_item_consume1_rect
    cinnabun_item_consume1 = text_font.render("* You ate the Cinnamon Bun.", False, WHITE)
    cinnabun_item_consume1_rect = cinnabun_item_consume1.get_rect(topleft = (60, 530))
    
    global cinnabun_item_consume2, cinnabun_item_consume2_rect
    cinnabun_item_consume2 = text_font.render("* You recovered 22 HP!", False, WHITE)
    cinnabun_item_consume2_rect = cinnabun_item_consume2.get_rect(topleft = (60, 630))
    
    global undyne_check1, undyne_check1_rect
    undyne_check1 = text_font.render("* UNDYNE 7 ATK 0 DEF", False, WHITE)
    undyne_check1_rect = undyne_check1.get_rect(topleft = (60, 530))
    
    global undyne_check2, undyne_check2_rect
    undyne_check2 = text_font.render("* The heroine that NEVER gives up.", False, WHITE)
    undyne_check2_rect = undyne_check2.get_rect(topleft = (60, 630))
    
    undyne_image = pygame.image.load('assets\\images\\undyne_battle.gif')
    undyne_image = pygame.transform.scale(undyne_image, (346, 478))
    
    global undyne_text
    undyne_text = TextButton("* Undyne", False, WHITE, (255, 255, 64), (150, 550), True)
    
    global check_text, plead_text, challenge_text
    check_text = TextButton("* Check", False, WHITE, (255, 255, 64), (150, 550), True)
    plead_text = TextButton("* Plead", False, WHITE, (255, 255, 64), (650, 550), False)
    challenge_text = TextButton("* Challenge", False, WHITE, (255, 255, 64), (150, 650), False)
    
    global snowpiece1_text, snowpiece2_text, cinnabun1_text, cinnabun2_text
    snowpiece1_text = TextButton("* SnowPiece", False, WHITE, (255, 255, 64), (150, 550), True)
    snowpiece2_text = TextButton("* SnowPiece", False, WHITE, (255, 255, 64), (650, 550), False)
    cinnabun1_text = TextButton("* CinnaBun", False, WHITE, (255, 255, 64), (150, 650), False)
    cinnabun2_text = TextButton("* CinnaBun", False, WHITE, (255, 255, 64), (650, 650), False)
    global top_item_list, btm_item_list
    top_item_list = [snowpiece1_text, snowpiece2_text]
    btm_item_list = [cinnabun1_text, cinnabun2_text]
    
    global spare_text
    spare_text = TextButton("* Spare", False, WHITE, (255, 255, 64), (150, 550), True)
    
    global fighting, acting, iteming, mercying
    
    global snowpiece_consumed, cinnabun_consumed
    
    while True:
        screen.fill((0, 0, 0))
        screen.blit(chara_text, chara_text_rect)
        screen.blit(lvl_text, lvl_text_rect)
        if default:
            screen.blit(undyne_attacks, undyne_attacks_rect)
        screen.blit(hp_text, hp_text_rect)
        screen.blit(kr_text, kr_text_rect)
        
        health_ratio_text = char_font.render(f"{player.current_health} / {player.maximum_health}", False, WHITE)
        health_ratio_text_rect = health_ratio_text.get_rect(topleft = (875, 816))
        
        screen.blit(health_ratio_text, health_ratio_text_rect)
        screen.blit(undyne_image, (430, 10))
        pygame.draw.rect(screen, WHITE, pygame.Rect(30, 500, 1193, 300), 5)

        buttonupdates()
        if fighting and fight_selected == False:
            fightbuttonupdates()
        if acting and checked == False:
            actbuttonupdates()
        
        if len(top_item_list) <= 0:
            fight_btn.active = True
            item_btn.active = False
        if iteming and (snowpiece_consumed == False and cinnabun_consumed == False) and len(top_item_list):
            itembuttonupdates()
        
        if mercying:
            mercybuttonupdates()
        
        if fight_selected:
            attackscreen()
        if checked:
            check()
        if snowpiece_consumed:
            snowpieceitemconsume()
        if cinnabun_consumed:
            cinnabunitemconsume()
        
        # player.draw(screen)
        player.update()
        
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit(0)
                
        pygame.display.update()
        FPS.tick(60)

boss_fight()