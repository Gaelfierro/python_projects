def Story(game):
    print 'You are in the middle of the forest, what do you do?'
    print'Press 1 to look for food, press 2 to look for shelter, or press 3 to look for water.'
    user_input=int(raw_input('...'))
    if user_input==1:
        print 'You found a mushroom and a bush with weird berries, but you dont know if their poisonous or not...'
        print 'Press 1 to eat the mushroom, press 2 to eat the berries, press 3 to skip both'
        user_input=int(raw_input('...'))
        if user_input ==1:
            print'You ate the berries, they tasted weird, it turns that they were indeed poisonous and you died!'
        elif user_input==2:
            print'The mushroom was poisonous, you got diarrhea and you died!'
        else:
            print'Good thing you avoided those, they were both really poisonous.'
    elif user_input==2:
        print 'There is a cave 2 miles away or go to the cabin on top of the mountain.'
        print 'Press 1 to go to the cave, press 2 to go to the cabin, or press 3 to skip'
        user_input= int(raw_input('...'))
        if user_input==1:
            print 'The cave is filled with cannibals and they eat you.'
            print 'You died'
            print 'press 1 to go back to the beginning.'
        elif user_input==2:
            print 'The cabin is on top of the mountain, you go there and it turns it was abandoned. However, there is a town nearby, you go there and they give you shelter. YOU WON!'
        else:
            print 'good choice, they were both dangerous.'
            print 'Press 1 to go back to the beginning.'
    else:
        print 'There is river 4 miles away, go there?'
        print 'Press 1 for YES, press 2 for NNNOOOPPPEEE!!!'
        user_input=int(raw_input('...'))
        if user_input==1:
            print 'After an hour of walking, you finally get to the river, you reach out to drink some water, but a massive fish came out and ate your face, killing you in the process.'
        elif user_input==2:
            print 'Good choice, the fish there are as large as cow (which is odd, because river is rather small, maybe it is deeper then it looks.) and can eat a human in one bite.'
            print 'press 1 to go back to the beginning.'

def The_Room(room):
    print 'You wake up in empty room with two doors, one in the left, one in the right, and on the front a large window.'
    print 'Press one to go to left door, press two to go to the right door, or press three to look into the window'
    user_input=int(raw_input(1, 2, 3,))
    if user_input==1:
        print 'You tried to to open the door, but the darn thing is lock, maybe there is another way to open it...'
    elif user_input==2:
        print 'You open the right door, there is a sink, a toilet, a bathtab, a large hole in the wall, and cabinet with a mirror on top of the sink. A bathroom...'
        print 'You check the toilet, there is a pistol on it (it is a M1911). You reach out for it and checked the chamber, it only has one round.'
        print 'You check the sink. there is a key on it. You open the cabinet, there is 3 magazines with 7 rounds each.'
        print 'Nothing interesting in the bathtab.'
        print 'Press one to go to the other door and shoot the doorknob, or press two to check the window.'
        user_input=int(raw_input(1,2,))
        if user_input==1:
            print 'You went back to the other room and shot the doorknob, now that door is now unlocked, you open the door and see a long hallway right on front of you.'
            print 'The walls of the hallway are filled with paintings of people and places you never seen or been to, however one of them depicts the same room you have previously been to.'
            print 'But as the hallway goes on, you start noticing some paintings depicting strange looking humanoid creatures, then you finally reached the end of the hall.'
            print 'The hallway ends with a large dark green door, but before you could reach the dooknob, you remember that you notice was something strange about one particular painting.'
            print 'So what will you do now? Open the door (press 1) or go back to inspect the painting (press 2).'
        elif user_input==2:
            print 'you look through the window and it seems that you are on a large building. Trying to jump will be suicide, so you leave it alone.'
