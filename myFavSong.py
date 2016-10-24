def myFavSong(song, artist):
    tries = 0
    hints = 0
    song = song.lower()
    while tries < 5:
        guess = input('What is my favorite song?')
        guess = guess.lower()
        if guess != "hint":
            tries += 1 
        if guess == song or guess == song.lower():
            print ('Great Job! It took you {} tries and {} hints to guess my favorite song.'.format(tries,hints))
            break
        elif guess == 'hint':
            hints += 1
            print ( 'The artist of this song is {}'.format(artist))
        elif guess == 'Hint':
            hints += 1
            print ( 'The artist of this song is {}'.format(artist))
        elif guess == 'HINT':
            hints += 1
            print ( 'The artist of this song is {}'.format(artist))
        else:
            print ('Try again!')
    if tries == 5 and guess != song:
        print("You have exceeded the number of tries")
    print('Thanks for playing!')
