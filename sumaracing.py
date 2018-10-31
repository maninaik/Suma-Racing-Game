import pygame, sys, time,random
pygame.init()

# Dimensions of the display
display_width = 800
display_height = 800

# Displaying the display screen with game title
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('SUMA RACING')

# Declaration of colours used
white = (255,255,255)
text_colour = (135,205,29)
block_colour = (67,98,234)
black = (0,0,0)
intro_colour = (72,200,210)
c_colour = (242,214,13)
green = (13,123,27)
bright_green = (65,235,86)
red = (163,5,21)
bright_red = (255,0,0)
blue = (6,36,157)
bright_blue = (18,64,245)
dark_colour = (150,50,152)
bright_colour = (205,109,207)
rule_colour = (22,169,248)

# Decalaration of the clock
clock = pygame.time.Clock()

# Loading the image in the variable
carImg = pygame.image.load('sumacar1.png')

# Function for displaying number of dodged blocks 
def blocks_dodged(count):
        font = pygame.font.SysFont(None,25)
        text = font.render("DODGED : " + str(count),True,black)
        gameDisplay.blit(text,(0,0))

# Function for displaying score 
def game_score(score):
        font = pygame.font.SysFont(None,25)
        text = font.render("SCORE : " + str(score),True,black)
        gameDisplay.blit(text,(200,0))

# Function to load the car image in the background       
def car(x,y):
        gameDisplay.blit(carImg,(x,y))
        
# Function to display the crash message
def crash():
        message_display('YOU CRASHED!',text_colour)

# Function for displaying text of large font size
def message_display(text,m_colour):
        largeText = pygame.font.Font('freesansbold.ttf',100)
        TextSurf , TextRect = text_object(text,largeText,m_colour)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf,TextRect)
        pygame.display.update()
        time.sleep(2)
        game_loop()

# Function for rendering text on the display
def text_object(text,font,t_colour):
        TextSurface = font.render(text,True,t_colour)
        return TextSurface, TextSurface.get_rect()

# Function to draw a block
def block(block_x,block_y,block_w,block_h,colour):
        pygame.draw.rect(gameDisplay,colour,[block_x,block_y,block_w,block_h])

# Function to draw a coin
def coin(coinx,coiny,coinr,c_colour):
        pygame.draw.circle(gameDisplay,c_colour,(coinx,coiny),coinr)

# Function to quit the game
def quit_game():
        pygame.quit()
        quit()

# Funcion to form a button with it's functionalities        
def button(msg,x,y,w,h,ic,ac,action=None):
      mouse = pygame.mouse.get_pos()
      click = pygame.mouse.get_pressed()
      if (x+w)> mouse[0] > x and (y+h) > mouse[1] > y :
             pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
             if click[0] == 1 and action != None:
                   action()
      else:
             pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
             smallText = pygame.font.Font("freesansbold.ttf",25)
             TextSurf , TextRect = text_object(msg,smallText,white)
             TextRect.center = ((x+(w/2)),(y+(h/2)))
             gameDisplay.blit(TextSurf,TextRect)

# Function to display instrutions
def rule_message(message):
             gameDisplay.fill(white)
             largeText = pygame.font.Font('freesansbold.ttf',20)
             TextSurf , TextRect = text_object(message,largeText,rule_colour)
             TextRect.center = ((display_width/2),(display_height/2))
             gameDisplay.blit(TextSurf,TextRect)
             pygame.display.update()
             clock.tick(15)
             time.sleep(3)
                      
# Function for defining the instruction
def rule():
        flag = True
        while flag == True:
             rule_message("INSTRUCTIONS WILL BE DISPLAYED IN THE FORM OF A SLIDE SHOW.")
             rule_message("1. DODGE THE BLUE BLOCKS IN ORDER TO SURVIVE THE GAME.")
             rule_message("2. COLLECT AS MANY YELLOW COINS AS POSSIBLE.")
             rule_message("3. EACH YELLOW COIN WILL EARN YOU 32 POINTS.")
             rule_message("4. IF YOU TOUCH LESS AREA OF COIN YOU WILL EARN LESS POINTS.")
             rule_message("5. YOUR SCORE IS DISPLAYED AT THE TOP LEFT CORNER OF YOUR SCREEN.")
             rule_message("6. NO. OF BLOCKS DODGED IS DISPLAYED AT THE TOP OF YOUR SCREEN.")
             rule_message("7. GOING BEYOND LEFT BORDER OF YOUR SCREEN YOU WILL CRASH YOU.")
             rule_message("8. GOING BEYOND RIGHT BORDER OF YOUR SCREEN WILL CRASH YOU.")
             rule_message("9. IF YOU TOUCH ANY OF THE BLOCK YOU WILL CRASH.")
             rule_message("ALL THE BEST GAMERS!!")
             flag=False
        game_menu()

# Function for displaying the menu page        
def game_menu():
        gexit=False        
        while not gexit:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            gexit = True
                intro = True
                while not intro:
                        for event in pygame.event.get():

                        	if event.type == pygame.QUIT:
                            		pygame.quit()
                            		quit()
                gameDisplay.fill(white)
                largeText = pygame.font.Font('freesansbold.ttf',100)
                TextSurf , TextRect = text_object("SUMA RACING",largeText,intro_colour)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf,TextRect)
               
                button("GO!",150,550,100,50,green,bright_green,game_loop)
                button("QUIT",600,550,100,50,red,bright_red,quit_game)
                button("RULE",370,550,100,50,blue,bright_blue,rule)
                
                pygame.display.update()
                clock.tick(2)

# Function for running the game 
def game_loop():
    car_width = 114
    car_height = 109
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    block_startx = random.randrange(0,display_width)
    block_starty = -200
    block_width = 114
    block_height = 109
    block_speed = 5

    coinx = random.randrange(0,display_width)
    coiny = -200
    coinr = 50
    coin_speed = 5

    score = 0

    x_change = 0
    y_change = 0
    count = 0
 
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_LEFT:
                    x_change = -7
                elif event.key ==  pygame.K_RIGHT:
                    x_change = 7
                
            elif event.type == pygame.KEYUP:
                if event.key ==  pygame.K_LEFT or event.key ==  pygame.K_RIGHT :
                    x_change = 0
                    y_change = 0
        
        x += x_change
        y += y_change
        

        gameDisplay.fill(white)

        block(block_startx,block_starty,block_width,block_height,block_colour)
        block_starty += block_speed

        coin(coinx,coiny,coinr,c_colour)
        coiny += coin_speed
        
        car(x,y)

        blocks_dodged(count)
        game_score(score)

        if x > ((display_width)-(car_width)) or x < 0  or  y > ((display_width)-(car_width)) or y < 0 :
            crash()

        if block_starty > display_height:
            block_starty = 0 - block_starty
            block_startx = random.randrange(0,display_width)
            count += 1
            block_speed += 1

        if coiny > display_height:
            coiny = 0 - coiny
            coinx = random.randrange(0,display_width)
           
           
           
        if y < block_starty + block_height :
            if x > block_startx and x <block_startx + block_width or x + car_width > block_startx and x + car_width < block_startx + block_width:
                crash()

        if y < coiny :
            if x > coinx - coinr and x < coinx + coinr or x + car_width > coinx - coinr and x + car_width < coinx + coinr:
                score += 1

                  
        pygame.display.update()
        clock.tick(80)
 
game_menu()                    
game_loop()
pygame.quit()
quit() 
         
