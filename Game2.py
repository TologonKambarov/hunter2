import pygame, sys
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((288, 512))  # pygame.SCALED | pygame.FULLSCREEN)
pygame.display.set_caption('ОХОТНИК')
FonA = pygame.image.load('bg.png').convert_alpha()
icon = pygame.image.load('zomb2.png').convert_alpha()
huntingclub = pygame.image.load('huntingclub82.png').convert_alpha()
metka = pygame.image.load('metka48.png').convert_alpha()
sniper1 = pygame.image.load('sniper.png').convert_alpha()
sniper2 = pygame.image.load('zomb1.png').convert_alpha()
pygame.display.set_icon(icon)
myfont = pygame.font.Font('forest.ttf', 25)
text_surface = myfont.render('HUNTER', False, 'lightgreen')
Shoot = pygame.image.load('shoot2.png').convert_alpha()
shoot_rect = Shoot.get_rect(topleft=(120, 455))
Jump = pygame.image.load('jump2.png').convert_alpha()
jump_rect = Jump.get_rect(topleft=(118, 400))
Leftr = pygame.image.load('left2.png').convert_alpha()
left_rect = Leftr.get_rect(topleft=(234, 455))
Rightr = pygame.image.load('right2.png').convert_alpha()
right_rect = Rightr.get_rect(topleft=(5, 455))
walk_left = [
    pygame.image.load('hleft1.png').convert_alpha(),
    pygame.image.load('hleft2.png').convert_alpha(),
    pygame.image.load('hleft3.png').convert_alpha(),
    pygame.image.load('hleft4.png').convert_alpha(),
    pygame.image.load('hleft4.5.png').convert_alpha(),
    pygame.image.load('hleft5.png').convert_alpha(),
    pygame.image.load('hleft6.png').convert_alpha(),
    pygame.image.load('hleft7.png').convert_alpha(),
    pygame.image.load('hleft8.png').convert_alpha(),
    pygame.image.load('hleft9.png').convert_alpha(),
]
walk_right = [
    pygame.image.load('hright1.png').convert_alpha(),
    pygame.image.load('hright2.png').convert_alpha(),
    pygame.image.load('hright3.png').convert_alpha(),
    pygame.image.load('hright4.png').convert_alpha(),
    pygame.image.load('hright4.5.png').convert_alpha(),
    pygame.image.load('hright5.png').convert_alpha(),
    pygame.image.load('hright6.png').convert_alpha(),
    pygame.image.load('hright7.png').convert_alpha(),
    pygame.image.load('hright8.png').convert_alpha(),
    pygame.image.load('hright9.png').convert_alpha(),
]
Ghost = pygame.image.load('ghost2.png').convert_alpha()
ghost_list_in_game = []
player_anim_count = 0
FonB = 0
player_speed = 15
player_x = 10
player_y = 330
is_jump = False
jump_count = 7
Fonsound = pygame.mixer.Sound("forest.mp3")
ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 4000)
label = pygame.font.Font('Broken.ttf', 28)
label2 = pygame.font.Font('Toyz.ttf', 17)
lose_label = label.render('ЖЕНИЛДИН!', False, (20, 0, 200))
restart_label = label2.render('Кайра БАШТА', False, (0, 200, 0))
restart_label_rect = restart_label.get_rect(topleft=(76, 356))
Restart = pygame.image.load('restart3.png').convert_alpha()
Lose = pygame.image.load('lose2.png').convert_alpha()
bullets_left = 100
bullet = pygame.image.load('bullet10 6.png').convert_alpha()
bullets = []
gameplay = True
running = True
Fonsound2 = pygame.mixer.Sound("zaryad.ogg")
gunsound = pygame.mixer.Sound("gun2.mp3")
Fonsound.play(2)
Fonsound2.play()
Fonsound2.play()
Fonsound2.play()
while running:
    screen.blit(FonA, (FonB, 0))
    screen.blit(FonA, (FonB + 288, 0))
    screen.blit(text_surface, (5, 5))
    screen.blit(Shoot, shoot_rect)
    screen.blit(Jump, jump_rect)
    screen.blit(Leftr, left_rect)
    screen.blit(Rightr, right_rect)
    screen.blit(metka, (120, 0))
    screen.blit(sniper2, (220, 0))
    if gameplay:
        player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))
        if ghost_list_in_game:
            for (i, el) in enumerate(ghost_list_in_game):
                screen.blit(Ghost, el)
                el.x -= 10
                if el.x < 0:
                    ghost_list_in_game.pop(i)
                if player_rect.colliderect(el):
                    gameplay = False
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()
        if right_rect.collidepoint(mouse):
            screen.blit(walk_right[player_anim_count], (player_x, player_y))
        else:
            screen.blit(walk_left[player_anim_count], (player_x, player_y))
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()
        if left_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] and player_x > -10 and player_x < 228:
            player_x += player_speed
        elif right_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] and player_x < 250 and player_x > 10:
            player_x -= player_speed
        if not is_jump:
              if jump_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                is_jump = True
        else:
            if jump_count >= -7:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 2
                else:
                    player_y += (jump_count ** 2) / 2
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 7
        if player_anim_count == 9:
            player_anim_count = 0
        else:
            player_anim_count += 1
        FonB -= 2
        if FonB == -288:
            FonB = 0
        if bullets:
            for (i, el) in enumerate(bullets):
                screen.blit(bullet, (el.x, el.y))
                el.x += 30
                if el.x > 388:
                    bullets.pop(i)
                if ghost_list_in_game:
                    for (index, ghost_el) in enumerate(ghost_list_in_game):
                        if el.colliderect(ghost_el) and el.x < 288:
                            ghost_list_in_game.pop(index)
                            bullets.pop(i)
    else:
        screen.fill((20, 220, 90))
        screen.blit(icon, (88, 180))
        screen.blit(Lose, (50, 95))
        screen.blit(lose_label, (66, 128))
        screen.blit(Restart, (56, 321))
        screen.blit(restart_label, restart_label_rect)
        screen.blit(huntingclub, (100, 0))
        screen.blit(sniper1, (100, 440))
        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse):
            gameplay = True
            Fonsound2.play()
            Fonsound2.play()
            Fonsound2.play()
            player_x = 10
            ghost_list_in_game.clear()
            bullets.clear()
            bullets_left = 100
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == ghost_timer:
            ghost_list_in_game.append(Ghost.get_rect(topleft=(player_x+240, player_y-1)))
        if shoot_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] and bullets_left > 0:
            gunsound.play()
            gunsound.play()
            gunsound.play()
            gunsound.play()
            gunsound.play()
            gunsound.play()
            gunsound.play()
            gunsound.play()
            gunsound.play()
            gunsound.play()
            bullets.append(bullet.get_rect(topleft=(player_x + 60, player_y + 16)))
            bullets_left -= 1
    clock.tick(6)