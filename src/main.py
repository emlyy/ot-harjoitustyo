from cavegame import CaveGame

def main():
    game = CaveGame()
    while game.start_screen is True:
        game.events()
    while game.running:
        if game.start is True:
            game.sprites()
            game.start = False
        game.events()
        game.all_sprites.update()
        game.draw()


if __name__=="__main__":
    main()
  