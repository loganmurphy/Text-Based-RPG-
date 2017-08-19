# Here is where I have stored all of the character/enemy stats
class Monster:
     def __init__(self, name, hp, ap):
         self.name = name
         self.hp = hp
         self.ap = ap
     def displayMonster(self):
         print "Name : ", self.name,  ", HP: ", self.hp, ", AP: ", self.ap
monster1 = Monster("Goblin", 10, 2)

class Player:
    def __init__(self, name, hp, ap, mp):
        self.name = name
        self.hp = hp
        self.ap = ap
        self.mp = mp
    def displayPlayer(self):
        print "Name : ", self.name,  ", HP: ", self.hp, ", AP: ", self.ap, ", MP: ", self.mp
warrior = Player("Warrior", 10, 5, 0)
archer = Player("Archer", 10, 3, 0)
mage = Player("Mage", 10, 1, 5)

print "You find yourself at the foot of an old abandoned mine. In front of the cavernous entrance stands an old, wizened man."
char_name = raw_input("Old man: Hello, what is your name? ")
#Choices are Dwarf, Elf and Human
while True:
    char_race = raw_input("Old man: What Race are you a member of? ")
    if char_race.lower() not in ('dwarf', 'elf', 'human'):
        print "You may choose a Dwarf, Elf or Human as your character's race."
    else:
        print "Ah, well met noble %s." %(char_race)
        break
while True:
    char_class = raw_input("Old man: What class are you? ")
    if char_class.lower() not in ("warrior", "archer", "mage"):
        print "Hmm, never heard of that before. Around here we just have warriors, archers or mages."
        print "Choose again."
    else:
        print "I thought as much, you have the bearings of a %s." %(char_class)
        break

if (char_race == "dwarf" and char_class == "warrior"):
    warrior = Player("Warrior", 10, 5, 0)
    warrior.ap = warrior.ap + 1
    print "Here are your stats: "
    warrior.displayPlayer()
elif (char_race == "elf" and char_class == "archer"):
    archer = Player("Archer", 10, 3, 0)
    archer.ap = archer.ap + 1
    print "Here are your stats: "
    archer.displayPlayer()
elif (char_race == "human" and char_class == "mage"):
    mage = Player("Mage", 10, 1, 5)
    mage.mp = mage.mp + 1
    print "Here are your stats: "
    mage.displayPlayer()
elif (char_race != "dwarf" and char_class == "warrior"):
    warrior = Player("Warrior", 10, 5, 0)
    print "Here are your stats: "
    warrior.displayPlayer()
elif (char_race != "elf" and char_class == "archer"):
    archer = Player("Archer", 10, 3, 0)
    print "Here are your stats: "
    archer.displayPlayer()
else:
    mage = Player("Mage", 10, 1, 5)
    print "Here are your stats: "
    mage.displayPlayer()
    # print "Here are your stats: "

char_gen = raw_input("Old man: What is your gender? ")

print "Old mn: Hello, brave %s. Tell me, what brings a %s %s to our lands?" % (char_name, char_race, char_class)
reason = raw_input("Old man: Is it adventure that you seek? ")

if (reason.lower() == "no"):
    print "Old man: Oh, how disapointing. A coward. Begone from here, the sight of you sickens me."
    print "You turn and leave, shoulders slumped in defeat. The old man's loud, shrill laughter rings in your ears as you make retreat."
    print ">>>>>>>>>GAME OVER<<<<<<<<<"
else:
    print "Old man: May the Gods look over you on your journey. Here, take this. I no longer need it."
    print "Old man: And you my friend, will need all the help you can get."
    if(char_class == "warrior"):
        print "The old man hands over a sheathed short-sword. It is well-worn, but upon inspection you find it to be deadly-sharp"
        inventory = ["short-sword"]
        print "You look up to thank the old man, only to find he has vanished."
    elif(char_class == "archer"):
        print "The old man hands over a cloth-wrapped short-bow and quiver of arrows. The draw-string is frayed, and the wooden shaft well-worn, but it will do."
        inventory = ["short-bow", "10 arrows"]
        print "You look up to thank the old man, only to find he has vanished."
    else:
        print "The old man hands over a dust-covered scroll. The script is in a familiar language, and you realize this is a fire-spell. With this, you can hurl fire-balls at your enemies"
        magic = ["fire-ball"]
        print "You look up to thank the old man, only to find he has vanished."
    user_choice = raw_input("The mine-shaft lies await, like a demon's maw ready to swallow you. You have come too far to turn around. What do you do? ")
    if user_choice not in ("enter", "go in", "continue"):
        print "Make another choice."
    else:
        print "You take your first steps into the mine, dreaming of the treasures you will find. As you continue down further, you come to a fork in the path. Beyond, the light of the sun no longer reaches."
        user_choice = raw_input("The pathways to the left and right are equally dark and foreboding. No telling what lies in wait down either. Which direction do you go? ")
        if user_choice not in ("left", "right"):
            print "Make another choice."
        else: print "You make your way down the %s-hand path, stepping carefull as you secure your footing. The is much steeper than you expected." % (user_choice)
        if (user_choice == "left"):
            print "As you make your way into the depths of the mine, running your hand along the wall to steady yourself, you start to wish the old man had given you a torch instead."
            print "You stop abrubtly as you hear a faint chattering ahead."
        else:
            print "As you are make your way down the path, you suddenly lose your footing and fall on your back, sliding several-hundred-feet down the tunnel. You come to a stop as you crash head-first into a wall."
            print "You know that the wet feeling spreading over your face is not moisture from the cave wall as you think of the family you left behind to chase fortune and fame. If only you had stayed away from this forsaken place. Everything goes black."
            print ">>>>>>>>>GAME OVER<<<<<<<<<"
# I need a way to reset the game if there is a game over

# I need a way for my characters to do combat with monsters and have their health change as they take damage.
