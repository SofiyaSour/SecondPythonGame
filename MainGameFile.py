import pygame

image_path = "/data/data/org.test.somethingstrange/files/app/"
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((618, 359))
pygame.display.set_caption("SomethingStrange")
icon = pygame.image.load(image_path + "for games/something_strange_icon.png").convert_alpha()
pygame.display.set_icon(icon)

bg = pygame.image.load(image_path + "for games/bg.png").convert_alpha()
player = pygame.image.load(image_path + "for games/ImagesPythonGameSS/left_1.png")

walk_left = [
    pygame.image.load(image_path + "for games/ImagesPythonGameSS/left_1.png").convert_alpha(),
    pygame.image.load(image_path + "for games/ImagesPythonGameSS/right4.png").convert_alpha(),
    pygame.image.load(image_path + "for games/ImagesPythonGameSS/left_2.png").convert_alpha(),
    pygame.image.load(image_path + "for games/ImagesPythonGameSS/left_3.png").convert_alpha()
]
walk_right = [
    pygame.image.load(image_path + "for games/ImagesPythonGameSS/right_1.png").convert_alpha(),
    pygame.image.load(image_path + "for games/ImagesPythonGameSS/right_2.png").convert_alpha(),
    pygame.image.load(image_path + "for games/ImagesPythonGameSS/right_3.png").convert_alpha(),
    pygame.image.load(image_path + "for games/ImagesPythonGameSS/right_4.png").convert_alpha(),
]

monstRICK = pygame.image.load(image_path + "monstRICK.png").convert_alpha()
monstRICK_List = []


player_anim_count = 0
bg_x = 0
player_speed = 5
player_x = 150
player_y = 250

is_jump = False
jump_count = 8


#bg_sound = pygame.mixer.xound("soundforss/название звука")
#bg_sound.play()

monstRICK_timer = pygame.USEREVENT + 1
pygame.time.set_timer(monstRICK_timer,  2500)

label = pygame.font.Font(image_path + "for games/DeliciousHandrawn-Regular.ttf", 40)
lose_label = label.render("you lose!", False, (249, 48, 48))
restart_label = label.render("Play again?", False, (29, 233, 104))
restart_label_rect = restart_label.get_rect(topleft=(180, 200))

bullets_left = 5
bullet = pygame.image.load(image_path + "for games/ImagesPythonGameSS/bullet.png").convert_alpha()
bullets = []
gameplay = True
running = True
while running:


    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 618, 0))

    if gameplay:


        player_rect =  walk_left[0].get_rect(topleft=(player_x, player_y))

        if monstRICK_List:
            for (i,el) in enumerate(monstRICK_List):
                screen.blit(monstRICK, el)
                el.x -= 10

                if el.x < - 10:
                    monstRICK_List.pop(i)
                if player_rect.colliderect(el):
                    gameplay =  False


        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))

        else:
            screen.blit(walk_left[player_anim_count], (player_x, player_y))


        if keys[pygame.K_LEFT] and player_x > 50:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 200:
            player_x += player_speed

        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True

        else:
            if jump_count >= -8:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) // 2
                else:
                    player_y += (jump_count ** 2) // 2
                jump_count -= 1

            else:
                is_jump = False
                jump_count = 8



        if player_anim_count == 3:
            player_anim_count = 0
        else:
           player_anim_count += 1

        bg_x -= 2
        if bg_x == -618:
            bg_x = 0



        if bullets:
            for (i, el) in enumerate(bullets):
                screen.blit(bullet, (el.x, el.y))
                el.x += 4

                if el.x > 630:
                    bullets.pop(i)

                if monstRICK_List:
                    for (index, monstRICK_el) in enumerate(monstRICK_List):
                        if el.colliderect(monstRICK_el):
                            monstRICK_List.pop(index)
                            bullets.pop(i)
    else:
        screen.fill((87, 88, 89))
        screen.blit(lose_label, (180, 100))
        screen.blit(restart_label, restart_label_rect)

        mouse =pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 150
            monstRICK_List.clear()
            bullets.clear()
            bullets_left = 5




    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type ==  monstRICK_timer:
            monstRICK_List.append(monstRICK.get_rect(topleft=(620, 250)))

        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_b and bullets_left > 0:
            bullets.append(bullet.get_rect(topleft=(player_x + 30, player_y + 10)))
            bullets_left -= 1



    clock.tick(15)
