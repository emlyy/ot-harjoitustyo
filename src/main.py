from cavegame import CaveGame

def main():
    game = CaveGame()
    game.starting_screen()
    while game.running:
        if game.start == True:
            game.sprites()
            game.start = False
        game.events()
        game.all_sprites.update()
        game.draw()

        

if __name__=="__main__":
    main()

    

    
        