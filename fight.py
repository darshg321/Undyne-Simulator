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
        if self.active == True:
            screen.blit(self.hovering_image, self.pos)
        else:
            screen.blit(self.image, self.pos)

class TextButton():
    def __init__(self, string, antialiasing, color, hover_color, pos, active):
        self.string = string
        self.text_font = pygame.font.Font("assets\\fonts\\Determination Sans.otf", 50, bold=True)
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
        self.image = pygame.image.load('assets\images\\red_soul.webp')
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
        
    def currenthealth(self):
        return self.current_health
    
    def maximumhealth(self):
        return self.maximum_health
    
default = True
fighting = False
acting = False
iteming = False
mercying = False

def buttonupdates():
    global default, fighting, acting, iteming, mercying
    fight_btn.update()
    act_btn.update()
    item_btn.update()
    mercy_btn.update()
    
    if default == True:
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    
                    if fight_btn.active == True:
                        act_btn.active = True
                        fight_btn.active = False
                    
                    elif act_btn.active == True:
                        item_btn.active = True
                        act_btn.active = False
                        
                    elif item_btn.active == True:
                        mercy_btn.active = True
                        item_btn.active = False
                        
                    elif mercy_btn.active == True:
                        fight_btn.active = True
                        mercy_btn.active = False
                
                if event.key == pygame.K_LEFT:
                    
                    if fight_btn.active == True:
                        mercy_btn.active = True
                        fight_btn.active = False
                    
                    elif act_btn.active == True:
                        fight_btn.active = True
                        act_btn.active = False
                        
                    elif item_btn.active == True:
                        act_btn.active = True
                        item_btn.active = False
                        
                    elif mercy_btn.active == True:
                        item_btn.active = True
                        mercy_btn.active = False
                
                if event.key == pygame.K_RETURN or event.key == pygame.K_z:
                    
                    if fight_btn.active == True:
                        default = False
                        fighting = True
                    
                    elif act_btn.active == True:
                        default = False
                        acting = True
                    
                    elif item_btn.active == True:
                        default = False
                        iteming = True
                        
                    elif mercy_btn.active == True:
                        default = False
                        mercying = True

def fightbuttonupdates():
    global default, fighting
    undyne_text.update()
    
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                undyne_text.active = True
                fighting = False
                default = True

def actbuttonupdates():
    global default, acting
    check_text.update()
    plead_text.update()
    challenge_text.update()
    
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:

                if check_text.active == True:
                    plead_text.active = True
                    check_text.active = False
                
                elif plead_text.active == True:
                    check_text.active = True
                    plead_text.active = False

                elif challenge_text.active == True:
                    pass
            
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                
                if check_text.active == True:
                    challenge_text.active = True
                    check_text.active = False
                    
                elif plead_text.active == True:
                    pass
                
                elif challenge_text.active == True:
                    check_text.active = True
                    challenge_text.active = False
                    
            if event.key == pygame.K_x:
                check_text.active = True
                challenge_text.active = False
                plead_text.active = False
                acting = False
                default = True
                
def itembuttonupdates():
    global default, iteming, snowpiece1_text, snowpiece2_text, cinnabun1_text, cinnabun2_text
    snowpiece1_text.update()
    snowpiece2_text.update()
    cinnabun1_text.update()
    cinnabun2_text.update()
    
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:

                if snowpiece1_text.active == True:
                    snowpiece2_text.active = True
                    snowpiece1_text.active = False
                
                elif snowpiece2_text.active == True:
                    snowpiece1_text.active = True
                    snowpiece2_text.active = False

                elif cinnabun1_text.active == True:
                    cinnabun2_text.active = True
                    cinnabun1_text.active = False
                    
                elif cinnabun2_text.active == True:
                    cinnabun1_text.active = True
                    cinnabun2_text.active = False
            
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                
                if snowpiece1_text.active == True:
                    cinnabun1_text.active = True
                    snowpiece1_text.active = False
                
                elif snowpiece2_text.active == True:
                    cinnabun2_text.active = True
                    snowpiece2_text.active = False
                    
                elif cinnabun1_text.active == True:
                    snowpiece1_text.active = True
                    cinnabun1_text.active = False
                    
                elif cinnabun2_text.active == True:
                    snowpiece2_text.active = True
                    cinnabun2_text.active = False
                    
            if event.key == pygame.K_z:
                
                if snowpiece1_text.active or snowpiece2_text.active:
                    player.heal(45)
                    
                if cinnabun1_text.active or cinnabun2_text.active:
                    player.heal(22)
                    
            if event.key == pygame.K_x:
                snowpiece1_text.active = True
                snowpiece2_text.active = False
                cinnabun1_text.active = False
                cinnabun2_text.active = False
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

def boss_fight():
    pygame.display.set_caption('Fight!')
    global events
    global player
    player = Heart(76, 76)
    
    fight_img = pygame.image.load('assets\images\\fight.webp')
    fight_img = pygame.transform.scale(fight_img, (220, 84))
    act_img = pygame.image.load('assets\images\\act.webp')
    act_img = pygame.transform.scale(act_img, (220, 84))
    item_img = pygame.image.load('assets\images\\item.webp')
    item_img = pygame.transform.scale(item_img, (220, 84))
    mercy_img = pygame.image.load('assets\images\\mercy.webp')
    mercy_img = pygame.transform.scale(mercy_img, (220, 84))
    
    active_fight_img = pygame.image.load('assets\images\\active_fight.png')
    active_fight_img = pygame.transform.scale(active_fight_img, (220, 84))
    active_act_img = pygame.image.load('assets\images\\active_act.png')
    active_act_img = pygame.transform.scale(active_act_img, (220, 84))
    active_item_img = pygame.image.load('assets\images\\active_item.png')
    active_item_img = pygame.transform.scale(active_item_img, (220, 84))
    active_mercy_img = pygame.image.load('assets\images\\active_mercy.png')
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
    
    text_font = pygame.font.Font("assets\\fonts\\Determination Sans.otf", 50, bold=True)
    
    undyne_attacks = text_font.render("* Undyne Attacks!", False, WHITE)
    undyne_attacks_rect = undyne_attacks.get_rect(topleft = (60, 530))
    
    undyne_image = pygame.image.load('assets\images\\undyne_battle.gif')
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
    
    global spare_text
    spare_text = TextButton("* Spare", False, WHITE, (255, 255, 64), (150, 550), True)
    
    global fighting, acting, iteming, mercying
    
    while True:
        screen.fill((0, 0, 0))
        screen.blit(chara_text, chara_text_rect)
        screen.blit(lvl_text, lvl_text_rect)
        if default == True:
            screen.blit(undyne_attacks, undyne_attacks_rect)
        screen.blit(hp_text, hp_text_rect)
        screen.blit(kr_text, kr_text_rect)
        
        health_ratio_text = char_font.render(f"{player.current_health} / {player.maximum_health}", False, WHITE)
        health_ratio_text_rect = health_ratio_text.get_rect(topleft = (875, 816))
        
        screen.blit(health_ratio_text, health_ratio_text_rect)
        screen.blit(undyne_image, (430, 10))
        pygame.draw.rect(screen, WHITE, pygame.Rect(30, 500, 1193, 300), 5)

        buttonupdates()
        if fighting:
            fightbuttonupdates()
        if acting:
            actbuttonupdates()
        if iteming:
            itembuttonupdates()
        if mercying:
            mercybuttonupdates()

        # player.draw(screen)
        player.update()
        
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.heal(20)
                if event.key == pygame.K_DOWN:
                    player.damage(20)
                
        pygame.display.update()
        FPS.tick(60)

boss_fight()