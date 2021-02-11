#!/usr/local/bin/python
# UTF-8

# to do list
# 1. keep track of stats
# 2. keep track of contacts
# 3. make social level from birth place carry over to parents occupation
# 4. randomize names and ages

from random import random, choice, randint

def Athairi_birth_place():
    social_level = 0
    print('Athairi_birth_place():')
    print('Social level is', social_level)
    birth_place = (randint(1, 10))
    print('Birth place random number is ', birth_place)
    if birth_place == 1:
        print(' Bandit Camp. Social Level is Outlaw')
        social_level -= 5
    elif birth_place == 2:
        print(' Haunted Ruin. Social Level is -3')
        social_level -= 3
    elif birth_place == 3:
        print(' Forester\'s Camp. Social Level is -4')
        social_level -= 4
    elif birth_place == 4:
        print(' Pleasant Forest Hovel. Social Level is -2')
        social_level -= 2
    elif birth_place == 5:
        print(' Woodland Village. Social Level is 0')
        social_level += 0
    elif birth_place == 6:
        print(' Woodland Fort. Social Level is 0')
        social_level += 0
    elif birth_place == 7:
        print(' Small Town. Social Level is +1')
        social_level += 1
    elif birth_place == 8:
        print(' Small Woodland Castle. Social Level is +2')
        social_level += 2
    elif birth_place == 9:
        print(' Borderland Castle. Social Level is +3')
        social_level += 3
    elif birth_place == 10:
        print('n Earl\'s Hold. Social Level is +4')
        social_level += 4
    return social_level


def Athairi_parents(social_level):
    print('Social level is', social_level)
    Athairi_mother_occupation(social_level)
    print('Your mother was descended from:')
    Athairi_parent_lineage()
    Athairi_father_occupation(social_level)
    print('Your mother was descended from:')
    Athairi_parent_lineage()
    return


def Athairi_mother_occupation(social_level):
    social_level = (randint(1, 10)) + social_level
    if social_level == 1:
        Athairi_mother_outlaw()
    elif social_level < 4:
        Athairi_mother_forester()
    elif social_level < 7:
        Athairi_mother_commoner()
    elif social_level < 9:
        Athairi_mother_merchant()
    else:
        Athairi_mother_noble()
    return


def Athairi_father_occupation(social_level):
    social_level = (randint(1, 10)) + social_level
    if social_level == 1:
        Athairi_father_outlaw()
    elif social_level < 4:
        Athairi_father_forester()
    elif social_level < 7:
        Athairi_father_commoner()
    elif social_level < 9:
        Athairi_father_merchant()
    else:
        Athairi_father_noble()
    return print


def Athairi_mother_outlaw():
        roll = (randint(1, 10))
        if roll < 4:
            print('Mother is a Bandit.')
        elif roll == 8 or 9:
            print('Mother is a Witch.')
        elif roll == 10:
            Athairi_mother_forester()
        else:
            Athairi_mother_outlaw()
        return


def Athairi_mother_forester():
        roll = (randint(1, 10))
        if roll == 1:
            Athairi_mother_outlaw()
        elif roll == 4:
            print('Mother is a Hermit.')
        elif roll == 5:
            print('Mother is a Hunter.')
        elif roll == 6 or 7 or 8:
            print('Mother is a Laborer.')
        else:
            Athairi_mother_forester()
        return


def Athairi_mother_commoner():
        roll = (randint(1, 10))
        if roll == 1:
            Athairi_mother_forester()
        elif roll == 2:
            print('Mother is a Farmer.')
        elif roll == 3:
            print('Mother is a Fortune Teller.')
        elif roll == 4:
            print('Mother is a House Servant.')
        elif roll == 5:
            print('Mother is an Innkeeper.')
        elif roll == 6:
            print('Mother is a Magician.')
        elif roll == 7:
            print('Mother is a Midwife or Priestess.')
        elif roll == 10:
            Athairi_mother_merchant()
        else:
            Athairi_mother_commoner()
        return


def Athairi_mother_merchant():
        roll = (randint(1, 10))
        if roll == 1:
            Athairi_mother_commoner()
        elif roll == 2:
            print('Mother is an Artisan.')
        elif roll == 4:
            print('Mother is an Entertainer.')
        elif roll == 5:
            print('Mother is a Householder.')
        elif roll == 10:
            Athairi_mother_noble()
        else:
            Athairi_mother_merchant()
        return


def Athairi_mother_noble():
        roll = (randint(1, 10))
        if roll == 1:
            Athairi_mother_merchant()
        elif roll == 6 or 7:
            print('Mother is a Lady.')
        else:
            Athairi_mother_noble()
        return


def Athairi_father_outlaw():
        roll = (randint(1, 10))
        if roll < 4:
            print('Father is a Bandit.')
        elif roll < 6:
            print('Father is a Thief.')
        elif roll < 8:
            print('Father is a Thug.')
        else:
            Athairi_father_forester()
        return


def Athairi_father_forester():
        roll = (randint(1, 10))
        if roll == 1:
            Athairi_father_outlaw()
        elif roll == 2:
            print('Father is a Fisher.')
        elif roll == 3:
            print('Father is a Herder.')
        elif roll == 4:
            print('Father is a Hermit.')
        elif roll == 5:
            print('Father is a Hunter.')
        elif roll < 9:
            print('Father is a Laborer.')
        elif roll == 9:
            print('Father is a Scout.')
        else:
            Athairi_father_commoner()
        return


def Athairi_father_commoner():
        roll = (randint(1, 10))
        if roll == 1:
            Athairi_father_forester()
        elif roll == 2:
            print('Father is a Farmer.')
        elif roll == 3:
            print('Father is a Fortune Teller.')
        elif roll == 4:
            print('Father is a House Servant.')
        elif roll == 5:
            print('Father is an Innkeeper.')
        elif roll == 6:
            print('Father is a Magician.')
        elif roll == 8:
            print('Father is a Trader.')
        elif roll == 9:
            print('Father is a Warrior (Mecenary or Vassal).')
        else:
            Athairi_father_merchant()
        return


def Athairi_father_merchant():
    should_restart = True
    while should_restart == True:
        should_restart = False
        roll = (randint(1, 10))
        if roll == 1:
            Athairi_father_commoner()
        elif roll == 2:
            print('Father is an Artisan.')
        elif roll == 3:
            print('Father is a Bard.')
        elif roll == 4:
            print('Father is an Entertainer.')
        elif roll == 5:
            print('Father is a Householder.')
        elif roll == 6:
            print('Father is a Merchant.')
        elif roll == 7:
            print('Father is a Priest.')
        elif roll == 8:
            print('Father is a Sage.')
        elif roll == 9:
            print('Father is a Scribe or Cartographer.')
        else:
            Athairi_father_noble()
        return


def Athairi_father_noble():
    should_restart = True
    while should_restart == True:
        should_restart = False
        roll = (randint(1, 10))
        if roll == 1:
            Athairi_father_merchant()
        elif roll == 3:
            print('Father is a Guard.')
        elif roll == 3:
            print('Father is a Herald.')
        elif roll == 4 or 5:
            print('Father is a Knight.')
        elif roll == 6 or 7:
            print('Father is a Lady.')
        elif roll < 10:
            print('Father is a Lord.')
        else:
            print('Father is a Seneschal.')
        return


def Athairi_parent_lineage():
    lineage = (randint(1, 20))
    if lineage == 1:
        Maelite_lineage()
    elif lineage < 7:
        Daradjan_lineage()
    elif lineage == 7:
        Aurian_lineage()
    elif lineage < 10:
        Danian_lineage()
    elif lineage < 17:
        Athairi_lineage()
    elif lineage < 20:
        Archaic_lineage()
    else:
        Unusual_lineage()


def Athairi_cultural_items():
    item = (randint(1, 10))
    if item == 1:
        print('Unicorn Horn spear')
    elif item == 2:
        print('Cauldron for brewing potions')
    elif item == 3:
        print('Lynx Stone amulet')
    elif item == 4:
        print('Amber amulet, with fossil')
    elif item == 5:
        print('Moss Agate amulet')
    elif item == 6:
        print('Hyacinth amulet')
    elif item == 7:
        print('Labiran Ward Harm Rune amulet')
    elif item == 8:
        print('Labiran Hex Rune amule')
    elif item == 9:
        print('Folk Charm to Ward a Person from Ghosts')
    else:
        print('A Spring Queen Heirloom', end="")
        item = (randint(1, 9))
        if item == 1:
            print('Unicorn Horn spear', end="")
        elif item == 2:
            print('Cauldron for brewing potions', end="")
        elif item == 3:
            print('Lynx Stone amulet', end="")
        elif item == 4:
            print('Amber amulet, with fossil', end="")
        elif item == 5:
            print('Moss Agate amulet', end="")
        elif item == 6:
            print('Hyacinth amulet', end="")
        elif item == 7:
            print('Labiran Ward Harm Rune amulet', end="")
        elif item == 8:
            print('Labiran Hex Rune amulet', end="")
        else:
            print('Folk Charm to Ward a Person from Ghosts', end="")
        print('(triple normal value)')
    return


def Aurian_birth_place():
    social_level = 0
    birth_place = (randint(1, 10))
    if birth_place == 1:
        print(' City Slum. Social Level is -4')
        social_level -= 4
    elif birth_place == 2:
        print(' Woodland Hovel. Social Level is -3')
        social_level -= 3
    elif birth_place == 3:
        print(' Fishing Village. Social Level is -2')
        social_level -= 2
    elif birth_place == 4:
        print(' Country Village. Social Level is -1')
        social_level -= 1
    elif birth_place == 5:
        print(' Small Town. Social Level is 0')
        social_level += 0
    elif birth_place == 6:
        print(' Small Castle. Social Level is 0')
        social_level += 0
    elif birth_place == 7:
        print(' Free City of Truse. Social Level is +1')
        social_level += 1
    elif birth_place == 8:
        print(' Baronial Castle or City. Social Level is +2')
        social_level += 2
    elif birth_place == 9:
        print(' Ducal Castle or City. Social Level is +3')
        social_level += 3
    elif birth_place == 10:
        print(' Royal Castle or City. Social Level is +4')
        social_level += 4
    return social_level


def Aurian_parents(social_level):
    Aurian_mother_occupation(social_level)
    print('Your mother was descended from:')
    Aurian_parent_lineage()
    Aurian_father_occupation(social_level)
    print('Your father was descended from:')
    Aurian_parent_lineage()
    return


def Aurian_mother_occupation(social_level):
    social_level = (randint(1, 10)) + social_level
    if social_level == 1:
        Aurian_mother_outlaw()
    elif social_level < 4:
        Aurian_mother_serf()
    elif social_level < 7:
        Aurian_mother_commoner()
    elif social_level < 9:
        Aurian_mother_lettered()
    else:
        Aurian_mother_noble()
    return


def Aurian_father_occupation(social_level):
    social_level = (randint(1, 10)) + social_level
    if social_level == 1:
        Aurian_father_outlaw()
    elif social_level < 4:
        Aurian_father_serf()
    elif social_level < 7:
        Aurian_father_commoner()
    elif social_level < 9:
        Aurian_father_lettered()
    else:
        Aurian_father_noble()
    return


def Aurian_mother_outlaw():
        roll = (randint(1, 10))
        if roll < 4:
            print('Mother is a Beggar.')
        elif roll == 9:
            print('Mother is a Witch or Fortune Teller.')
        elif roll == 10:
            Aurian_mother_serf()
        else:
            Aurian_mother_outlaw()
        return


def Aurian_mother_serf():
        roll = (randint(1, 10))
        if roll == 1:
            Aurian_mother_outlaw()
        if roll == 4 or 5:
            print('Mother is a House Servant.')
        elif roll == 10:
            Aurian_mother_commoner()
        else:
            Aurian_mother_serf()
        return


def Aurian_mother_commoner():
        roll = (randint(1, 10))
        if roll == 1:
            Aurian_mother_serf()
        elif roll == 3:
            print('Mother is an Entertainer or Courtesan.')
        elif roll == 4:
            print('Mother is a House Servant.')
        elif roll == 8:
            print('Mother is a Midwife.')
        elif roll == 10:
            Aurian_mother_lettered()
        else:
            Aurian_mother_commoner()
        return


def Aurian_mother_lettered():
        roll = (randint(1, 10))
        if roll == 1:
            Aurian_mother_commoner()
        elif roll == 3:
            print('Mother is an Aristocrat.')
        elif roll == 10:
            Aurian_mother_noble()
        else:
            Aurian_mother_lettered()
        return


def Aurian_mother_noble():
        roll = (randint(1, 10))
        if roll == 1:
            Aurian_mother_lettered()
        if roll == 7 or 8:
            print('Mother is a Lady.')
        else:
            Aurian_mother_noble()
        return


def Aurian_father_outlaw():
        roll = (randint(1, 10))
        if roll < 3:
            print('Father is a Bandit.')
        elif roll == 3:
            print('Father is a Beggar.')
        elif roll == 4:
            print('Father is a Hermit.')
        elif roll < 7:
            print('Father is a Thief.')
        elif roll < 9:
            print('Father is a Thug.')
        elif roll == 9:
            print('Father is a Fortune Teller.')
        elif roll == 10:
            Aurian_father_serf()
        else:
            Aurian_father_outlaw()
        return


def Aurian_father_serf():
        roll = (randint(1, 10))
        if roll == 1:
            Aurian_father_outlaw()
        elif roll < 3:
            print('Father is a Fisher.')
        elif roll == 3:
            print('Father is a Herder.')
        elif roll < 6:
            print('Father is a House Servant.')
        elif roll < 8:
            print('Father is a Laborer.')
        elif roll < 10:
            print('Father is a Tenant Farmer.')
        elif roll == 10:
            Aurian_father_commoner()
        else:
            Aurian_father_serf()
        return


def Aurian_father_commoner():
        roll = (randint(1, 10))
        if roll == 1:
            Aurian_father_serf()
        elif roll < 3:
            print('Father is an Artisan.')
        elif roll == 3:
            print('Father is an Entertainer.')
        elif roll == 4:
            print('Father is a House Servant.')
        elif roll == 5:
            print('Father is a Householder.')
        elif roll == 6:
            print('Father is a Hunter (Noble\'s Huntsman).')
        elif roll == 7:
            print('Father is a Innkeeper.')
        elif roll == 9:
            print('Father is a Trader.')
        elif roll == 10:
            Aurian_father_lettered()
        else:
            Aurian_father_commoner()
        return


def Aurian_father_lettered():
        roll = (randint(1, 10))
        if roll == 1:
            Aurian_father_commoner()
        elif roll < 3:
            print('Father is an Alchemist.')
        elif roll == 3:
            print('Father is an Aristocrat.')
        elif roll == 4:
            print('Father is a Magister.')
        elif roll == 5:
            print('Father is a Merchant.')
        elif roll == 6:
            print('Father is a Physician-Healer.')
        elif roll == 7:
            print('Father is a Priest (Divine King or Inquisitor or Templar.)')
        elif roll == 8:
            print('Father is a Scribe or Cartographer.')
        elif roll == 9:
            print('Father is a Spy or Assassin.')
        elif roll == 10:
            Aurian_father_noble()
        else:
            Aurian_father_lettered()
        return


def Aurian_father_noble():
        roll = (randint(1, 10))
        if roll == 1:
            Aurian_father_lettered()
        elif roll < 4:
            print('Father is a Guard.')
        elif roll == 4:
            print('Father is a Herald .')
        elif roll < 7:
            print('Father is a Knight.')
        elif roll == 7 or 8:
            should_restart = True
        elif roll == 9:
            print('Father is a Lord.')
        else:
            print('Father is a Seneschal.')
        return


def Aurian_parent_lineage():
    lineage = (randint(1, 20))

    if lineage < 3:
        Daradjan_lineage()
    elif lineage < 14:
        Aurian_lineage()
    elif lineage < 18:
        Danian_lineage()
    elif lineage < 20:
        Athairi_lineage()
    else:
        Unusual_lineage()
    return print


def Aurian_cultural_items():
    item = (randint(1, 10))
    if item == 1:
        print('Helmet with Auroch Horns')
    elif item == 2:
        print('Griffin Egg drinking cup')
    elif item == 3:
        print('Crystal amulet')
    elif item == 4:
        print('Garnet amulet')
    elif item == 5:
        print('Ruby amulet')
    elif item == 6:
        print('Coral amulet')
    elif item == 7:
        print('Imperial Strength Rune amulet')
    elif item == 8:
        print('Divine King Cult Charm to Ward a Believer from Danger')
    elif item == 9:
        print('Divine King Cult Charm to Ward a Believer from Magic')
    else:
        print('A Sea Migration Heirloom', end="")
        item = (randint(1, 9))
        if item == 1:
            print('Helmet with Auroch Horns', end="")
        elif item == 2:
            print('Griffin Egg drinking cup', end="")
        elif item == 3:
            print('Crystal amulet', end="")
        elif item == 4:
            print('Garnet amulet', end="")
        elif item == 5:
            print('Ruby amulet', end="")
        elif item == 6:
            print('Coral amulet', end="")
        elif item == 7:
            print('Imperial Strength Rune amulet', end="")
        elif item == 8:
            print('Divine King Cult Charm to Ward a Believer from Danger', end="")
        elif item == 9:
            print('Divine King Cult Charm to Ward a Believer from Magic', end="")
            print('(triple normal value)')
    return


def Danian_birth_place():
    social_level = 0
    birth_place = (randint(1, 10))
    if birth_place == 1:
        print(' Umisi Hill-fort. Social Level is -4')
        social_level -= 4
    elif birth_place == 2:
        print(' Pleasant Country Hovel. Social Level is -3')
        social_level -= 3
    elif birth_place == 3:
        print(' Umati Sea Port. Social Level is -2')
        social_level -= 2
    elif birth_place == 4:
        print(' Riverside Village. Social Level is -1')
        social_level -= 1
    elif birth_place == 5:
        print(' Country Village. Social Level is 0')
        social_level += 0
    elif birth_place == 6:
        print(' Small Town. Social Level is 0')
        social_level += 0
    elif birth_place == 7:
        print(' Small Hold. Social Level is +1')
        social_level += 1
    elif birth_place == 8:
        print(' Free City. Social Level is +2')
        social_level += 2
    elif birth_place == 9:
        print(' Earl\'s Hold. Social Level is +2')
        social_level += 2
    elif birth_place == 10:
        print(' King\'s Hold. Social Level is +3')
        social_level += 3
    return social_level


def Danian_parents(social_level):
    Danian_mother_occupation(social_level)
    print('Your mother was descended from:')
    Danian_parent_lineage()
    Danian_father_occupation(social_level)
    print('Your father was descended from:')
    Danian_parent_lineage()
    return print


def Danian_mother_occupation(social_level):
    social_level = (randint(1, 10)) + social_level
    if social_level == 1:
        Danian_mother_outlaw()
    elif social_level < 5:
        Danian_mother_commoner()
    elif social_level < 7:
        Danian_mother_artisan()
    elif social_level < 9:
        Danian_mother_lettered()
    else:
        Danian_mother_noble()
    return


def Danian_father_occupation(social_level):
    social_level = (randint(1, 10)) + social_level
    if social_level == 1:
        Danian_father_outlaw()
    elif social_level < 5:
        Danian_father_commoner()
    elif social_level < 7:
        Danian_father_artisan()
    elif social_level < 9:
        Danian_father_lettered()
    else:
        Danian_father_noble()
    return


def Danian_mother_outlaw():
        roll = (randint(1, 10))
        if roll == 3:
            print('Mother is a Beggar.')
        elif roll == 4:
            print('Mother is a Hermit.')
        elif roll == 4:
            print('Mother is a Witch.')
        elif roll == 10:
            Danian_mother_commoner()
        else:
            Danian_mother_outlaw()
        return


def Danian_mother_commoner():
        roll = (randint(1, 10))
        if roll == 1:
            Danian_mother_outlaw()
        elif roll == 4:
            print('Mother is a House Servant.')
        elif roll == 8:
            print('Mother is a Tenant Farmer.')
        elif roll == 10:
            Danian_mother_artisan()
        else:
            Danian_mother_commoner()
        return


def Danian_mother_artisan():
        roll = (randint(1, 10))
        if roll == 1:
            Danian_mother_commoner()
        elif roll == 2:
            print('Mother is a Artisan.')
        elif roll == 4:
            print('Mother is an Entertainer or Courtesan.')
        elif roll == 5:
            print('Mother is a Householder.')
        elif roll == 7:
            print('Mother is an Innkeeper .')
        elif roll == 8:
            print('Mother is a Midwife.')
        elif roll == 10:
            Danian_mother_lettered()
        else:
            Danian_mother_artisan()
        return


def Danian_mother_lettered():
        roll = (randint(1, 10))
        if roll == 1:
            Danian_mother_lettered()
        elif roll == 3:
            print('Mother is a Bard .')
        elif roll == 5:
            print('Mother is a Merchant.')
        elif second_roll == 6:
            print('Mother is a Physician-Healer.')
        elif roll == 1:
            Danian_mother_noble()
        else:
            Danian_mother_lettered()
        return


def Danian_mother_noble():
        roll = (randint(1, 10))
        if roll == 1:
            Danian_mother_lettered()
        if roll == 6 or 7:
            print('Mother is a Lady.')
        else:
            Danian_mother_noble()
        return


def Danian_father_outlaw():
        roll = (randint(1, 10))
        if roll < 3:
            print('Father is a Bandit.')
        elif roll == 3:
            print('Father is a Beggar.')
        elif roll == 4:
            print('Father is a Hermit.')
        elif roll < 7:
            print('Father is a Thief.')
        elif roll < 9:
            print('Father is a Thug.')
        elif roll == 10:
            Danian_father_commoner()
        else:
            Danian_father_outlaw()
        return


def Danian_father_commoner():
        roll = (randint(1, 10))
        if roll == 1:
            Danian_father_outlaw()
        elif roll == 2:
            print('Father is a Fisher.')
        elif roll == 3:
            print('Father is a Herder.')
        elif roll == 4:
            print('Father is a House Servant.')
        elif roll == 5:
            print('Father is a Laborer.')
        elif roll == 6:
            print('Father is a Sailor.')
        elif roll == 7:
            print('Father is a Scout.')
        elif roll == 8:
            print('Father is a Tenant Farmer.')
        elif roll == 9:
            print('Father is a Warrior (Mercenary or Vassal).')
        elif roll == 10:
            Danian_father_artisan()
        else:
            Danian_father_commoner()
        return


def Danian_father_artisan():
        roll = (randint(1, 10))
        if roll == 1:
            Danian_father_commoner()
        elif roll == 2:
            print('Father is an Artisan.')
        elif roll == 3:
            print('Father is an Astrologer.')
        elif roll == 4:
            print('Father is an Entertainer.')
        elif roll == 5:
            print('Father is a Householder.')
        elif roll == 6:
            print('Father is a Hunter (Noble\'s Huntsman).')
        elif roll == 7:
            print('Father is an Innkeeper.')
        elif roll == 9:
            print('Father is a Trader.')
        elif roll == 10:
            Danian_father_lettered()
        else:
            Danian_father_artisan()
        return


def Danian_father_lettered():
        roll = (randint(1, 10))
        if roll == 1:
            Danian_father_artisan()
        elif roll == 2:
            print('Father is an Alchemist.')
        elif roll == 3:
            print('Father is a Bard.')
        elif roll == 4:
            print('Father is a Magister.')
        elif roll == 5:
            print('Father is a Merchant.')
        elif roll == 6:
            print('Father is a Physician-Healer.')
        elif roll == 7:
            print('Father is a Priest (Divine King.)')
        elif roll == 8:
            print('Father is a Scribe or Cartographer.')
        elif roll == 9:
            print('Father is a Spy or Assassin.')
        elif roll == 10:
            Danian_father_noble()
        else:
            Danian_father_lettered()
        return


def Danian_father_noble():
        roll = (randint(1, 10))
        if roll == 1:
            Danian_father_lettered()
        elif roll == 2:
            print('Father is a Guard.')
        elif roll == 3:
            print('Father is a Herald.')
        elif roll < 6:
            print('Father is a Knight.')
        elif roll < 8:
            print('Father is a Lady.')
        elif roll < 10:
            print('Father is a Lord.')
        else:
            print('Father is a Seneschal.')
        return


def Danian_parent_lineage():
    lineage = (randint(1, 20))
    if lineage < 3:
        Daradjan_lineage()
    elif lineage < 6:
        Maelite_lineage()
    elif lineage < 9:
        Aurian_lineage()
    elif lineage < 16:
        Danian_lineage()
    elif lineage < 18:
        Athairi_lineage()
    elif lineage < 20:
        Archaic_lineage()
    else:
        Unusual_lineage()


def Danian_cultural_items():
    item = (randint(1, 10))
    if item == 1:
        print('Blood Agate amulet')
    elif item == 2:
        print('Crystal amulet')
    elif item == 3:
        print('Amber amulet, with fossil')
    elif item == 4:
        print('Turquoise amulet')
    elif item == 5:
        print('Silver dagger')
    elif item == 6:
        print('Daedekine Rune of Making amulet')
    elif item == 7:
        print('Hyacinth amulet')
    elif item == 8:
        print('Wyvern Scale target shield')
    elif item == 9:
        print('Folk Charm to Ward a Person from Ghosts')
    else:
        print('An Heirloom of either the War against Githwaine or the Black Day Battle', end="")
        item = (randint(1, 9))
        if item == 1:
            print('Blood Agate amulet', end="")
        elif item == 2:
            print('Crystal amulet', end="")
        elif item == 3:
            print('Amber amulet, with fossil', end="")
        elif item == 4:
            print('Turquoise amulet', end="")
        elif item == 5:
            print('Silver dagger', end="")
        elif item == 6:
            print('Daedekine Rune of Making amulet', end="")
        elif item == 7:
            print('Hyacinth amulet', end="")
        elif item == 8:
            print('Wyvern Scale target shield', end="")
        elif item == 9:
            print('Folk Charm to Ward a Person from Ghosts', end="")
        print('(triple normal value)')
    return


def Watchtower_birth_place():
    social_level = 0
    birth_place = (randint(1, 10))
    if birth_place == 1:
        print(' Seaside Hovel. Social Level is -4')
        social_level -= 4
    elif birth_place == 2:
        print(' Inland Village. Social Level is -3')
        social_level -= 3
    elif birth_place == 3:
        print(' Seaside Village. Social Level is -2')
        social_level -= 2
    elif birth_place == 4:
        print(' Small Town. Social Level is -1')
        social_level -= 1
    elif birth_place == 5:
        print(' Small Keep. Social Level is 0')
        social_level += 0
    elif birth_place == 6:
        print(' Coastal Keep. Social Level is 0')
        social_level += 0
    elif birth_place == 7:
        print(' Wall Keep. Social Level is +1')
        social_level += 1
    elif birth_place == 8:
        print(' Port City. Social Level is +2')
        social_level += 2
    elif birth_place == 9:
        print('n Earl\'s Keep. Social Level is +2')
        social_level += 2
    elif birth_place == 10:
        print(' Royal City of Angora. Social Level is +4')
        social_level += 4
    return social_level


def Watchtower_parents(social_level):
    Watchtower_mother_occupation(social_level)
    print('Your mother was descended from:')
    Watchtower_parent_lineage()
    Watchtower_father_occupation(social_level)
    print('Your father was descended from:')
    Watchtower_parent_lineage()
    return


def Watchtower_mother_occupation(social_level):
    social_level = (randint(1, 10)) + social_level
    if social_level == 1:
        Watchtower_mother_outlaw()
    elif social_level < 5:
        Watchtower_mother_commoner()
    elif social_level < 7:
        Watchtower_mother_freeman()
    elif social_level < 10:
        Watchtower_mother_watchtower()
    else:
        Watchtower_mother_patrician()
    return


def Watchtower_father_occupation(social_level):
    social_level = (randint(1, 10)) + social_level
    if social_level == 1:
        Watchtower_father_outlaw()
    elif social_level < 5:
        Watchtower_father_commoner()
    elif social_level < 7:
        Watchtower_father_freeman()
    elif social_level < 10:
        Watchtower_father_watchtower()
    else:
        Watchtower_father_patrician()
    return


def Watchtower_mother_outlaw():
        roll = (randint(1, 10))
        if roll < 3:
            print('Mother is a Bandit.')
        elif roll == 3:
            print('Mother is a Beggar.')
        elif roll == 4:
            print('Mother is a Hermit.')
        elif roll == 5 or 6:
            print('Mother is a Smuggler.')
        elif roll == 9:
            print('Mother is a Witch.')
        elif roll == 10:
            Watchtower_mother_commoner()
        else:
            Watchtower_mother_outlaw()
        return


def Watchtower_mother_commoner():
        roll = (randint(1, 10))
        if roll == 1:
            Watchtower_mother_outlaw()
        if roll == 3:
            print('Mother is a House Servant.')
        elif roll == 8:
            print('Mother is a Tenant Farmer.')
        elif roll == 10:
            Watchtower_mother_freeman()
        else:
            Watchtower_mother_commoner()
        return


def Watchtower_mother_freeman():
        roll = (randint(1, 10))
        if roll == 1:
            Watchtower_mother_commoner()
        if roll < 4:
            print('Mother is an Artisan.')
        elif roll == 4:
            print('Mother is a Bard.')
        elif roll == 5:
            print('Mother is a Fortune Teller.')
        elif roll == 6:
            print('Mother is an Innkeeper .')
        elif roll == 7:
            print('Mother is a Midwife.')
        elif roll == 10:
            Watchtower_mother_watchtower()
        else:
            Watchtower_mother_freeman()
        return


def Watchtower_mother_watchtower():
        roll = (randint(1, 10))
        if roll == 1:
            Watchtower_mother_freeman()
        if roll == 4:
            print('Mother is a Householder.')
        elif roll == 7:
            print('Mother is a Spy or Assassin.')
        elif roll == 10:
            Watchtower_mother_patrician()
        else:
            Watchtower_mother_watchtower()
        return


def Watchtower_mother_patrician():
        roll = (randint(1, 10))
        if roll == 1:
            Watchtower_mother_watchtower()
        elif roll < 4:
            print('Mother is an Aristocrat.')
        elif roll == 4:
            print('Mother is an Entertainer or Courtesan.')
        elif roll == 5:
            print('Mother is a Lady.')
        else:
            Watchtower_mother_patrician()
        return


def Watchtower_father_outlaw():
        roll = (randint(1, 10))
        if roll < 3:
            print('Father is a Bandit.')
        elif roll == 3:
            print('Father is a Beggar.')
        elif roll == 4:
            print('Father is a Hermit.')
        elif roll < 7:
            print('Father is a Smuggler.')
        elif roll == 7:
            print('Father is a Thief.')
        elif roll == 8:
            print('Father is a Thug.')
        elif roll == 10:
            Watchtower_father_commoner()
        else:
            Watchtower_father_outlaw()
        return


def Watchtower_father_commoner():
        roll = (randint(1, 10))
        if roll == 1:
            Watchtower_father_outlaw()
        elif roll < 3:
            print('Father is a Fisher.')
        elif roll == 3:
            print('Father is a House Servant.')
        elif roll == 4:
            print('Father is a Hunter.')
        elif roll == 5:
            print('Father is a Laborer.')
        elif roll == 6:
            print('Father is a Sailor.')
        elif roll == 7:
            print('Father is a Scout.')
        elif roll == 8:
            print('Father is a Tenant Farmer.')
        elif roll == 9:
            print('Father is a Warrior (Mercenary or Vassal).')
        elif roll == 10:
            Watchtower_father_freeman()
        else:
            Watchtower_father_commoner()
        return


def Watchtower_father_freeman():
        roll = (randint(1, 10))
        if roll == 1:
            Watchtower_father_commoner()
        elif roll < 4:
            print('Father is an Artisan.')
        elif roll == 4:
            print('Father is a Bard.')
        elif roll == 5:
            print('Father is a Fortune Teller.')
        elif roll == 6:
            print('Father is an Innkeeper.')
        elif roll == 8:
            print('Father is a Scribe or Cartographer.')
        elif roll == 9:
            print('Father is a Trader.')
        elif roll == 10:
            Watchtower_father_watchtower()
        else:
            Watchtower_father_freeman()
        return


def Watchtower_father_watchtower():
        roll = (randint(1, 10))
        if roll == 1:
            Watchtower_father_freeman()
        if roll < 3:
            print('Father is a Guard.')
        elif roll == 3:
            print('Father is a Herald.')
        elif roll == 4:
            print('Father is a Householder.')
        elif roll == 5:
            print('Father is a Scout.')
        elif roll == 6:
            print('Father is a Seneschal.')
        elif roll == 7:
            print('Father is a Spy or Assassin .')
        elif roll == 8:
            print('Father is a Warlord.')
        elif roll == 9:
            print('Father is a Warrior (Sworn).')
        elif roll == 10:
            Watchtower_father_patrician()
        else:
            Watchtower_father_watchtower()
        return


def Watchtower_father_patrician():
        roll = (randint(1, 10))
        if roll == 1:
            Watchtower_father_watchtower()
        elif roll < 4:
            print('Father is an Aristocrat .')
        elif roll == 4:
            print('Father is an Entertainer.')
        elif roll == 6:
            print('Father is a Lord.')
        elif roll == 7:
            print('Father is a Merchant.')
        elif roll == 8:
            print('Father is a Physician-Healer.')
        elif roll == 9:
            print('Father is a Priest (Divine King.)')
        else:
            print('Father is a Sage.')
        return


def Watchtower_parent_lineage():
    lineage = (randint(1, 20))
    if lineage < 3:
        Daradjan_lineage()
    elif lineage < 6:
        Aurian_lineage()
    elif lineage < 9:
        Danian_lineage()
    elif lineage < 17:
        Maelite_lineage()
    elif lineage < 19:
        Athairi_lineage()
    elif lineage == 19:
        Archaic_lineage()
    else:
        Unusual_lineage()


def Watchtower_cultural_items():
    item = (randint(1, 10))
    if item == 1:
        print('Helmet with Horsehair plume')
    elif item == 2:
        print('Galactide amulet (empty)')
    elif item == 3:
        print('Amber amulet, with insect fossil')
    elif item == 4:
        print('Hyacinth amulet')
    elif item == 5:
        print('Silver dagger')
    elif item == 6:
        print('Crystal amulet')
    elif item == 7:
        print('Labiran Ward Magic rune amulet')
    elif item == 8:
        print('Labiran Motion rune amulet')
    elif item == 9:
        print('Folk Charm to Ward a Person from Danger')
    else:
        item = (randint(1, 9))
        print('Lost Uthedmael Heirloom', end="")
        if item == 1:
            print('Helmet with Horsehair plume', end="")
        elif item == 2:
            print('Galactide amulet (empty)', end="")
        elif item == 3:
            print('Amber amulet, with insect fossil', end="")
        elif item == 4:
            print('Hyacinth amulet', end="")
        elif item == 5:
            print('Silver dagger', end="")
        elif item == 6:
            print('Crystal amulet', end="")
        elif item == 7:
            print('Labiran Ward Magic rune amulet', end="")
        elif item == 8:
            print('Labiran Motion rune amulet', end="")
        elif item == 9:
            print('Folk Charm to Ward a Person from Danger', end="")
        print('(triple normal value)')
    return


def Daradjan_birth_place():
    social_level = 0
    birth_place = (randint(1, 10))
    if birth_place == 1:
        print(' Brigand Encampment. Social Level is Outlaw')
        social_level -= 3
    elif birth_place == 2:
        print(' Barren Coast Pirate Hold. Social Level is Outlaw')
        social_level -= 3
    elif birth_place == 3:
        print(' Decrepit Country Hovel. Social Level is -2')
        social_level -= 2
    elif birth_place == 4:
        print(' Highland Clan Hold. Social Level is Highlander')
    elif birth_place == 5:
        print(' Fortified Village. Social Level is 0')
        social_level += 0
    elif birth_place == 6:
        print(' Fortified Village. Social Level is 0')
        social_level += 0
    elif birth_place == 7:
        print(' Fortified Hill Town. Social Level is +1')
        social_level += 1
    elif birth_place == 8:
        print(' Tributary Citadel. Social Level is +2')
        social_level += 2
    elif birth_place == 9:
        print('n Independent Citadel. Social Level is +3')
        social_level += 3
    elif birth_place == 10:
        print(' Great Citadel. Social Level is +4')
        social_level += 4
    return social_level


def Daradjan_parents(social_level):
    Daradjan_mother_occupation(social_level)
    print('Your mother was descended from:')
    Daradjan_parent_lineage()
    Daradjan_father_occupation(social_level)
    print('Your father was descended from:')
    Daradjan_parent_lineage()
    return


def Daradjan_mother_occupation(social_level):
    social_level = (randint(1, 10)) + social_level
    if social_level < 3:
        Daradjan_mother_outlaw()
    elif social_level < 5:
        Daradjan_mother_highlander()
    elif social_level < 7:
        Daradjan_mother_freeman()
    elif social_level < 9:
        Daradjan_mother_artisan()
    elif social_level > 8:
        Daradjan_mother_citadel()
    return


def Daradjan_father_occupation(social_level):
    social_level = (randint(1, 10)) + social_level
    if social_level < 3:
        Daradjan_father_outlaw()
    elif social_level < 5:
        Daradjan_father_highlander()
    elif social_level < 7:
        Daradjan_father_freeman()
    elif social_level < 9:
        Daradjan_father_artisan()
    else:
        Daradjan_father_citadel()
    return


def Daradjan_mother_outlaw():
        roll = (randint(1, 10))
        if roll < 4:
            print('Mother is a Brigand, Highland.')
        elif roll < 6:
            print('Mother is a Hermit.')
        elif roll < 8:
            print('Mother is a Pirate.')
        elif roll == 10:
            Daradjan_mother_highlander()
        else:
            Daradjan_mother_outlaw()
        return


def Daradjan_mother_highlander():
        roll = (randint(1, 10))
        if roll == 1:
            Daradjan_mother_outlaw()
        elif roll < 3:
            print('Mother is a Chieftess or War Chieftess.')
        elif roll < 5:
            print('Mother is a Hunter.')
        elif roll == 5:
            print('Mother is a Scout.')
        elif roll == 7:
            print('Mother is a Soldier (foot) (Free Company).')
        elif roll == 8 or 9:
            print('Mother is a Warrior (Clan).')
        elif roll == 10:
            Daradjan_mother_freeman()
        else:
            Daradjan_mother_highlander()
        return


def Daradjan_mother_freeman():
        roll = (randint(1, 10))
        if roll == 1:
            Daradjan_mother_highlander()
        elif roll == 5:
            print('Mother is a House Servant.')
        elif roll == 7:
            print('Mother is a Priestess (Mystery Cult: Hathhalla).')
        elif roll == 8:
            print('Mother is a Priestess (Yheran).')
        elif roll == 9:
            print('Mother is a Trader.')
        elif roll == 10:
            Daradjan_mother_artisan()
        else:
            Daradjan_mother_freeman()
        return


def Daradjan_mother_artisan():
        roll = (randint(1, 10))
        if roll == 1:
            Daradjan_mother_freeman()
        elif roll < 3:
            print('Mother is an Artisan.')
        elif roll == 3:
            print('Mother is a Bard.')
        elif roll == 4:
            print('Mother is a Courtesan.')
        elif roll == 5:
            print('Mother is an Entertainer.')
        elif roll == 6:
            print('Mother is a Fortune Teller.')
        elif roll == 7:
            print('Mother is a Householder.')
        elif roll == 8:
            print('Mother is a Midwife.')
        elif roll == 9:
            print('Mother is a Magician.')
        elif roll == 10:
            Daradjan_mother_citadel()
        else:
            Daradjan_mother_artisan()
        return


def Daradjan_mother_citadel():
        roll = (randint(1, 10))
        if roll == 1:
            Daradjan_mother_artisan()
        elif roll == 2:
            print('Mother is a Bannermwoan (War Chieftess).')
        elif roll == 4 or 5:
            print('Mother is a Guard.')
        elif roll == 7:
            print('Mother is a Legionare (Dara Dess only).')
        elif roll == 8:
            print('Mother is a Noble.')
        elif roll == 9 or 10:
            print('Mother is a Warrior (Citadel).')
        else:
            Daradjan_mother_citadel()
        return


def Daradjan_father_outlaw():
        roll = (randint(1, 10))
        if roll < 4:
            print('Father is a Brigand, Highland.')
        elif roll < 6:
            print('Father is a Hermit.')
        elif roll < 8:
            print('Father is a Pirate .')
        elif roll < 10:
            print('Father is a Thug.')
        elif roll == 10:
            Daradjan_father_highlander()
        else:
            Daradjan_father_outlaw()
        return


def Daradjan_father_highlander():
        roll = (randint(1, 10))
        if roll == 1:
            Daradjan_father_outlaw()
        elif roll == 2:
            print('Father is a Chieftain or War Chief.')
        elif roll < 5:
            print('Father is a Hunter.')
        elif roll == 5:
            print('Father is a Scout.')
        elif roll == 6:
            print('Father is a Shaman.')
        elif roll == 7:
            print('Father is a Soldier (foot) (Free Company).')
        elif roll < 10:
            print('Father is a Warrior (Clan).')
        elif roll == 10:
            Daradjan_father_freeman()
        else:
            Daradjan_father_highlander()
        return


def Daradjan_father_freeman():
        roll = (randint(1, 10))
        if roll == 1:
            Daradjan_father_highlander()
        elif roll < 3:
            print('Father is a Farmer.')
        elif roll == 3:
            print('Father is a Fisher.')
        elif roll == 4:
            print('Father is a Herder.')
        elif roll == 5:
            print('Father is a House Servant.')
        elif roll == 6:
            print('Father is a Laborer.')
        elif roll == 9:
            print('Father is a Trader.')
        elif roll == 10:
            Daradjan_father_artisan()
        else:
            Daradjan_father_freeman()
        return


def Daradjan_father_artisan():
        roll = (randint(1, 10))
        if roll == 1:
            Daradjan_father_freeman()
        elif roll < 3:
            print('Father is an Artisan.')
        elif roll == 3:
            print('Father is a Bard.')
        elif roll == 5:
            print('Father is an Entertainer.')
        elif roll == 6:
            print('Father is a Fortune Teller.')
        elif roll == 7:
            print('Father is a Householder.')
        elif roll == 9:
            print('Father is a Magician.')
        elif roll == 10:
            Daradjan_father_citadel()
        else:
            Daradjan_father_artisan()
        return


def Daradjan_father_citadel():
        roll = (randint(1, 10))
        if roll == 1:
            Daradjan_father_artisan()
        elif roll < 3:
            print('Father is a Bannerman (War Chief).')
        elif roll == 3:
            print('Father is a Bannerman (Warlord).')
        elif roll == 4 or 5:
            print('Father is a Guard.')
        elif roll == 6:
            print('Father is a Herald.')
        elif roll == 7:
            print('Father is a Legionare (Dara Dess only).')
        elif roll == 8:
            print('Father is a Noble.')
        else:
            print('Father is a Warrior (Citadel).')
        return


def Daradjan_parent_lineage():
    lineage = (randint(1, 20))
    if lineage < 4:
        Maelite_lineage()
    elif lineage < 6:
        Danian_lineage()
    elif lineage == 6:
        Aurian_lineage()
    elif lineage < 17:
        Daradjan_lineage()
    elif lineage == 17:
        Athairi_lineage()
    elif lineage < 20:
        Archaic_lineage()
    else:
        Unusual_lineage()
    return


def Daradjan_cultural_items():
    item = (randint(1, 10))
    if item == 1:
        print('Helmet with Horsehair plume')
    elif item == 2:
        print('Galactide amulet (empty)')
    elif item == 3:
        print('Amber amulet, with insect fossil')
    elif item == 4:
        print('Hyacinth amulet')
    elif item == 5:
        print('Silver dagger')
    elif item == 6:
        print('Crystal amulet')
    elif item == 7:
        print('Labiran Ward Magic rune amulet')
    elif item == 8:
        print('Labiran Motion rune amulet')
    elif item == 9:
        print('Folk Charm to Ward a Person from Danger')
    else:
        item = (randint(1, 10))
        print('Golden Age Heirloom', end="")
        if item == 1:
            print('Helmet with Horsehair plume', end="")
        elif item == 2:
            print('Galactide amulet (empty)', end="")
        elif item == 3:
            print('Amber amulet, with insect fossil', end="")
        elif item == 4:
            print('Hyacinth amulet', end="")
        elif item == 5:
            print('Silver dagger', end="")
        elif item == 6:
            print('Crystal amulet', end="")
        elif item == 7:
            print('Labiran Ward Magic rune amulet', end="")
        elif item == 8:
            print('Labiran Motion rune amulet', end="")
        elif item == 9:
            print('Folk Charm to Ward a Person from Danger', end="")
        print('(triple normal value)')
    return


def Maelite_lineage():
    initial_roll = (randint(1, 10))
    second_roll = (randint(1, 10))
    if initial_roll < 6:
        print('Maelite Common Lineage. The original inhabitants of the Dain Eduins and large portions of Western (Uthed) Dania. +1 COUR, -1 EMP, +1 WIS. Descended of Geniche.')
    elif initial_roll < 9:
        if second_roll == 1:
            print('Maelfess. An old name for Nymarga the Tyrant, the wickedest man in history, whose blood can still be found amongst the Maelites. +1 APP, +1 STR, +1 TECH, +1 WILL, +1 IMAG, +1 PRE, -1 CONV, -1 EMP, Forked Tongue 3, Cruelty 2 Binding, Vanity 2 Binding. Unknown lineage.')
        elif second_roll == 2:
            print('Maelfir. Ancient King of the Djar Mael, who led the destruction of the Kingdom of the Valley. +1 TECH, +1 IMAG, +1 PRE, +1 COUR, -1 EMP, +1 WIS. Son of Yhera.')
        elif second_roll == 3:
            print('Gaebrila. Ancient Queen of the Djar Mael, one of the destroyers of the Kingdom of the Valley. +1 IMAG, +1 PRE, +1 COUR, -1 EMP, +1 WIS. Daughter of Djara.')
        elif second_roll == 4:
            print('Salach. Ancient King of the Djar Mael, one of the destroyers of the Kingdom of the Valley. +1 APP, +1 STR, +1 MEM, +1 CONV, +1 COUR, +1 WIS, -1 EMP, Enlightened Tongue 2. Son of a Ghazarab.')
        elif second_roll == 5:
            print('Dagukil. First King of the Great Citadel of Ardeal, built with the help of Queen Druxada of Daradja. +1 STR, +1 COUR, -1 EMP, +1 WIS. Of common Maelite Lineage.')
        elif second_roll == 6:
            print('Duras. King of Liadaine and a Defender of Urune Dure during its Fall; a lover to Hannath Hammergreia. +1 APP, +1 STR, +1 COUR, +1 PRE, +1 WIS. Descended of Dagukil.')
        elif second_roll == 7:
            print('Dhankila. A King of Bragagh and a Defender of Urune Dure during its Fall; a lover to Hannath Hammergreia and rival to Duras. +1 DEX, +1 PER, +1 COUR, -1 EMP, +1 WIS, Jealousy 1 Binding (towards any Lover). Of common Maelite Lineage.')
        elif second_roll == 8:
            print('Pale Meffire. Age of Legends Magician from Liss Dyved, who ruled the Vale of Barrows for a time from her own grave. +1 WILL, +1 COUR, -1 EMP, +1 WIS, Ghost Mask 2, Otherworldly Visage 1, Second Sight 2. Of common Maelite Lineage.')
        elif second_roll == 9:
            print('Cirrisa. Famous Priestess of the Great Temple of Yhera on the Fal Shara, called The Blessed for her generosity to those in need. +1 REAS, +1 COUR, +1 EMP, +1 WIS. Of common Maelite Lineage.')
        elif second_roll == 10:
            print('Taran. Age of Legends King of Eoras, called the King of the Dead; killed by Dauban Hess. +1 TECH, +1 MEM, +1 COUR, -1 EMP, +1 WIS, Ghost Mask 1. Of common Maelite Lineage.')
    elif initial_roll == 9:
        if second_roll == 1:
            print('Morghita. A warrior-priestess in the service of Githwaine; called the Blood Lady of Mageva after defending the city against Fortias. +1 WILL, +1 COUR, -1 EMP, +1 WIS, Terrifying Mask 1. Of common Maelite Lineage.')
        elif second_roll == 2:
            print('Malkheb. Greatest Warlord in the service of Githwaine, who killed over 100 Danian Knights. +1 APP, +1 WILL, +1 PRE, +1 CONV, +1 COUR, -1 EMP, +1 WIS, Dreadful Visage 2. Son of a Gamezhiel.')
        elif second_roll == 3:
            print('Maloza. Magician-King of Cimria who created an army of ghosts to rule all of the Dain Eduins for a time. +1 APP, -1 STAM, + 2 DEX, +1 PER, +1 PRE, +1 COUR, +1 WIS, -1 EMP, Otherworldly Visage 1, Ghost Mask 2, Second Sight 1. Son of a Faerie Spirit.')
        elif second_roll == 4:
            print('Gedeb. King of Cacak who allowed the Isliklidae into the Cora Gara and was first to enter their service. +1 STAM, +1 COUR, -1 EMP, +1 WIS. Of common Maelite Lineage.')
        elif second_roll == 5:
            print('Gebet. Los Famed rebel Chieftain who fought the Isliklidae for two decades, often from the Red Wastes. +1 WILL, +1 IMAG, +1 COUR, -1 EMP, +1 WIS. Of common Maelite Lineage')
        elif second_roll == 6:
            print('Dragace. Rebel Warlord that betrayed Gebet Los to the Isliklidae. +1 STR, +1 REAS, +1 COUR, -1 EMP, +1 WIS, Shame 2 Binding. Of common Maelite Lineage.')
        elif second_roll == 7:
            print('Helfyr. Hor War Chief who killed Gwyrfyr Brightstar at the siege of Cir At\'tor; sometimes called The Star Killer. +1 STR, +1 WILL, +1COUR, -1 EMP, +1 WIS. Of common Maelite Lineage.')
        elif second_roll == 8:
            print('Illigdir. Holl War Chief who raided as far as Dara Dess. +1 STR, +1 DEX, +1 COUR, -1 EMP, +1 WIS. Of common Maelite Lineage.')
        elif second_roll == 9:
            print('Carghita. Brigand-Queen of Angharad and agent of the Isliklidae, who knew secret ways across the Djar Eduins. +1 STR, +1 PER, +1 WILL, +1 COUR, -1 EMP, +1 WIS, Terrifying Mask 1. Descended of Morghita.')
        elif second_roll == 10:
            print('Madog. Brigand Warlock who knew how to get over the Great Wall to terrorize the Danias. +1 STR, +1 PER, +1 COUR, -1 EMP, +1 WIS, Second Sight 1. Of common Maelite Lineage.')
    else:
        if second_roll == 1:
            print('Ulywn. A Hero of the war against Githwaine and later the First King of Maece. +1 STR, +1 COUR, +1 WIS. Of common Maelite Lineage.')
        elif second_roll == 2:
            print('Bragas Ley. A Hero of the war against Githwaine and the First Watchtower King of Warwark. +1 DEX, +1 PRE, +1 COUR, -1 EMP, +1 WIS. Of common Maelite Lineage.')
        elif second_roll == 3:
            print('Pallan. A Hero of the war against Githwaine and chief architect of the Great Wall, and a powerful Sorcerer and Alchemist. +1 WILL, +1 IMAG, +1 REAS, +1 COUR, -1 EMP, +1 WIS, Second Sight 1. Of common Maelite Lineage.')
        elif second_roll == 4:
            print('Bier. Fisher-Warrior who killed a sea monster and fed his village for a year on its remains. +1 APP, +1 PRE, +1 COUR, -1 EMP, +1 WIS, Fool\'s Luck 1. Of common Maelite Lineage.')
        elif second_roll == 5:
            print('Dyllam. A Hero of the Black Day Battle, who saved the High King Darwain the Fumbler but could not find Gladringer. +1 DEX, +1 PER, +1 COUR, -1 EMP, +1 WIS Of common Maelite Lineage.')
        elif second_roll == 6:
            print('Pallan of Mizer. A Hero of the Crusade against the Isliklidae, who briefly ruled the New Kingdom of Maellos from the Citadel of Ferabis. +1 STR, +1 WILL, +1 COUR, -1 EMP, +1 WIS, Vanity 1 Binding. Of common Maelite Lineage.')
        elif second_roll == 7:
            print('Gwyrfyr of Warwark. King of Maece who brokered a peace between the Kings of Dain and Erid Dania, averting civil war. +1 WILL, +1 IMAG, +1 REAS, +1 CONV, +1 COUR, +1 EMP, +1 WIS, Second Sight 1. Descended of Pallan.')
        elif second_roll == 8:
            print('Lewyr. Magician and alchemist, the first man to return from Lost Liss Dyved; suspected as a possible Throne Thief. +1 MEM, +1 IMAG, +1 REAS, +1 COUR, -1 EMP, +1 WIS, Second Sight 1. Of common Maelite Lineage.')
        elif second_roll == 9:
            print('Gal Fayre. A Hero of the Wars of the Throne Thief, who saved the city of Nomath by her quick thinking. +1 TECH, +1 IMAG, +1 REAS, +1 COUR, -1 EMP, +1 WIS. Of common Maelite Lineage.')
        elif second_roll == 10:
            print('Angiss. Watchtower King loyal to the High Kings during the Wars of the Throne Thief and so made the First King of Angowrie. +1 APP, +1 PER, +1 CONV, +1 COUR, -1 EMP, +1 WIS. Of common Maelite Lineage.')
    return


def Daradjan_lineage():
    initial_roll = (randint(1, 10))
    second_roll = (randint(1, 10))
    if initial_roll < 6:
        print('Daradjan Common Lineage. The original inhabitants of the Harath Eduin Mountains. +1 STR, +1 PER, -1 WILL. Descended of Yhera.')
    elif initial_roll == 6:
        if second_roll == 1:
            print('Dara. First Queen of the Harath Eduins, builder of Dara Dess, Binder of Yeolf and a Binder of the Black Hunter; slain by Thula. +1 APP, +1 TECH, +1 WILL, +1 IMAG, +1 PRE, +1 CONV, +1 WIS. Daughter of Yhera.')
        elif second_roll == 2:
            print('Druxada. Second Queen of the Harath Eduins, she drove Thula and then the Maelites out of Daradja. +1 APP, +1 TECH, +1 WILL, +1 IMAG, +1 PRE, +1 CONV, +1 WIS, Imperious Tongue 1. Daughter of Dara, daughter of Yhera.')
        elif second_roll == 3:
            print('Yeolf. Mountain-Spirit of the Harath Eduins who shakes the earth. -1 APP, +1 STR, +1 STAM, +1 PER, -1 IMAG. Son of Gigantes.')
        elif second_roll == 4:
            print('Cy Fair. Murderer, companion of the Wild Hunter, and founder of the Cy Faira Mal brigand band. +1 APP, +1 STR, +1 DEX, +1 CONV, -3 EMP, -1 WIS, Aura of Fury 1, Berserkir Ekstasis 2, Hate Life 5 Binding. Son of a Sharab Deceal.')
        elif second_roll == 5:
            print('Sion Gorta. Mountain Man-Spirit who flattened the Erin Gara and ruled it from his Vale. -1 APP, +1 STR, +1 STAM, +1 PER, -1 WILL, -1 IMAG. Son of Gigantes.')
        elif second_roll == 6:
            print('Lanys. A Queen of Dara Dess and mother of Arathea, she let Durean refugees stay in Daradja. +1 APP, +1 TECH, +1 WILL, +1 IMAG, +1 PRE, +1 CONV, +1 EMP, +1 WIS, Imperious Tongue 1. Descended of Druxada, daughter of Dara, daughter of Yhera.')
        elif second_roll == 7:
            print('Damara. By Highland legend daughter of Arathea and Islik the Divine King; a Queen of Dara Dess, she was slain by her sister Goatis. +1 APP, +1 STR, +1 TECH, +1 WILL, +1 IMAG, +1 PRE, +1 CONV, +1 EMP, +1 WIS, Imperious Tongue 1. Descended of Lanys, descendant of Druxada, daughter of Dara, daughter of Yhera.')
        elif second_roll == 8:
            print('Goatis. By Highland legend daughter of Arathea and Agall; first Queen of Athark, she killed her sister Damara and then drowned herself. +1 APP, +1 STR, +1 STAM, +1 TECH, +1 WILL, +1 IMAG, -1 REAS, +1 PRE, +1 CONV, -1 EMP, +1 WIS, Imperious Tongue 1, Rage 3 Binding, Envy 3 Binding (towards family members). Descended of Lanys, descendant of Druxada, daughter of Dara, daughter of Yhera.')
        elif second_roll == 9:
            print('Hetha Basi. By Highland legend daughter of Arathea and Jala; first Queen of Heth Moll. +1 APP, +1 TECH, +1 WILL, +1 IMAG, +1 PRE, +1 CONV, +1 EMP, +1 WIS, Imperious Tongue 1, Serene Aura 1. Descended of Lanys, descendant of Druxada, daughter of Dara, daughter of Yhera.')
        elif second_roll == 10:
            print('Leda. By Highland legend daughter of Arathea and Coromat; first Queen of Finleth. +1 APP, +1 DEX, +1 TECH, +1 WILL, +1 IMAG, +1 PRE, +1 CONV, +1 EMP, +1 WIS, Imperious Tongue 1. Descended of Lanys, descendant of Druxada, daughter of Dara, daughter of Yhera.')
    elif initial_roll < 9:
        if second_roll == 1:
            print('Dyfyr. Durean Hero sworn to the service of Hetha Basi, who fought back the cursed Men of Athark. +1 STR, +1 WILL, +1 CONV, -1 WIS. Of common Galean Lineage.')
        elif second_roll == 2:
            print('Dyved. Seneschal of Damara who became the First King of Dara Dess in the Age of Legends. +1 STR, +1 WILL, +1 IMAG, +1 CONV, -1 WIS. Son of Dyfyr.')
        elif second_roll == 3:
            print('Ara Basi. Queen of Heth Moll who became a Spring Queen of An-Athair, and called the most beautiful Queen the Highlands has ever seen. +1 APP, +1 TECH, +1 WILL, +1 IMAG, +1 PRE, +1 CONV, +1 EMP, +1 WIS, Imperious Tongue 1, Serene Aura 1, Spellbinding Form 3. Descended of Hetha Basi, descendant of Lanys, descendant of Druxada, daughter of Dara, daughter of Yhera.')
        elif second_roll == 4:
            print('Chulwain. King of Athark who became a Golden Knight of An-Athair to lift the curse of Goatis. +1 APP, +1 STR, +1 STAM, +1 TECH, +1 WILL, +1 IMAG, +1 PRE, +1 CONV, +1 WIS. Descended of Goatis, descendant of Lanys, descendant of Druxada, daughter of Dara, daughter of Yhera.')
        elif second_roll == 5:
            print('Cynlas. Brigand King who refused to become a Golden Knight; founded the Bloody Hundred brigand band. +1 APP, +1 STR, +1 PER, +1 WILL, +1 REAS, +1 PRE. Of common Daradjan Lineage.')
        elif second_roll == 6:
            print('Galyease. Builder of a chain of warning signal fires, Warlord of the forces that drove the Empire out of Daradja. +1 STR, +1 PER, +1 MEM, +1 IMAG, +1 PRE, -1 WILL. Of common Daradjan Lineage.')
        elif second_roll == 7:
            print('Mergaile. The Worm Eater, a King of Dara Dess and single-handed slayer of three Worm Kings. +1 STR, +1 PER, +1 IMAG, +1 PRE, Enchanted Aura 2. Of common Daradjan Lineage.')
        elif second_roll == 8:
            print('Gavir. The Runner Lord of Heth Moll, staunch ally of Fortias the Brave who once ran the length of the Vale of Barrows. +1 APP, +1 DEX, +1 TECH, +1 WILL, +1 IMAG, +1 PRE, +1 CONV, +1 EMP, +1 WIS, Imperious Tongue 1, Serene Aura 1, Spellbinding Form 3. Descended of Ara Basi, descendant of Hetha Basi, descendant of Lanys, descendant of Druxada, etc.')
        elif second_roll == 9:
            print('Daurus Tull. Knight-Captain of the Company of Stars, a group of Vanimorian and Thessid Heroes that aided Erlwulf. +1 STR, +1 STAM, -1 TECH, +1 PER, +1 COUR. Of common Vanimorian Lineage.')
        elif second_roll == 10:
            print('Cynan. King of Dara Dess and Hero of the Black Day Battle, last Great King of the Daradjan Citadels. +1 STR, +1 PER, +1 IMAG, +1 PRE, +1 COUR, Enchanted Aura 2. Descended of Mergaile.')
    elif initial_roll == 9:
        if second_roll == 1:
            print('Ruad. First Daradjan to renounce Queen Lanys\' offer to Durean refugees; founder of the Av-Ruad clan. +1 STR, +1 STAM, +1 PER, +1 COUR, Hate non-Daradjans 2 Binding. Of common Daradjan Lineage.')
        elif second_roll == 2:
            print('Faelen. Ruad\'s "steady hand"; founder of the Av-Faelen clan. +1 STR, +1 PER, -1 WILL, +1 PRE, +1 COUR. Of common Daradjan Lineage.')
        elif second_roll == 3:
            print('Tenved. Ruad\'s "hot head"; founder of the Av-Tenved clan. +1 APP, +1 STR, -1 STAM, +1 DEX, +1 PER, -1 WILL, +1 PRE, +1 WIS. Son of a Faerie Spirit.')
        elif second_roll == 4:
            print('Sil Amain. Early Pirate-King of Sharptooth Bay and Mal Irama; founder of the Av-Amain clan. +1 STR, +1 PER, -1 WILL, +1 EMP, +1 WIS. Of common Daradjan Lineage.')
        elif second_roll == 5:
            print('Fallas. King of Hus Gara driven into the mountains; founder of the Fallas Av-Invis and Fallas Av-Tane clans. +1 STR, +1 PER, -1 WILL, +1 REAS. Of common Daradjan Lineage.')
        elif second_roll == 6:
            print('Gal Ari. The Queen of Claws, and famed foe of the Danians of Umat; founder of the Av-Ari clan. +1 APP, +1 STR, +1 PER, +1 PRE, -1 WILL. Of common Daradjan Lineage.')
        elif second_roll == 7:
            print('Gal Dare. Famed ghost-hunter of the Vale of Barrows; a Chieftain and Shaman of the Av-Dare clan. +1 STR, +1 DEX, +1 PER, -1 WILL, +1 COUR, Ghost Mask 1, Second Sight 1. Of common Daradjan Lineage.')
        elif second_roll == 8:
            print('Enora Tane. Bronze Age Pirate Queen who conquered Mal Irama; a Chieftain of the Fallas Av-Tane clan. +1 STR, +1 TECH, +1 PER, -1 WILL, +1 WIS. Of common Daradjan Lineage.')
        elif second_roll == 9:
            print('Bavar Dair. Bronze Age Bard-King of the Eastern Eduins; a Chieftain of the Ban Bres clan. +1 APP, +1 STR, +1 PER,  -1 WILL, +1 IMAG, +1 PRE. Of common Daradjan Lineage.')
        elif second_roll == 10:
            print('Gevris. The Head-Taker, cruel outlaw who used to hunt men for sport; a Chieftain of the Bodmall clan. +1 STR, +1 PER, +1 CONV, Cruelty 1 Binding. Of common Daradjan Lineage.')
    else:
        if second_roll == 1:
            print('Angharab. Golden Age Enchantress-Queen of the Tel Eduins and counsel to Druxada. +1 STR, +1 PER, +1 REAS, +1 WIS, Second Sight 1. Of common Daradjan Lineage.')
        elif second_roll == 2:
            print('Fer Enid. Enchantress-counsel to Damara, who by legend hid away Damara\'s children to save them from Goatis. +1 STR, +1 TECH, +1 PER, +1 IMAG, -1 WILL, Second Sight 1. Of common Daradjan Lineage.')
        elif second_roll == 3:
            print('Rabija. Witch who confronted Dauban Hess and by legend told him to go find the Dawn. +1 STR, +1 PER, +1 WILL, +1 WIS, Forked Tongue 3, Second Sight 1. Of common Daradjan Lineage.')
        elif second_roll == 4:
            print('Gobelin. Bodmall clan blacksmith, forger of the sword Gladringer for Fortias. +1 STR, +1 TECH, +1 PER, -1 WILL, +1 WIS, Second Sight 1. Of common Daradjan Lineage.')
        elif second_roll == 5:
            print('Agaire. Witch who became an early Iron Age Queen of Heth Moll by force, ending the line of the Basi Queens. +1 STR, +1 PER, +1 WILL, +1 CONV, Second Sight 1. Of common Daradjan Lineage.')
        elif second_roll == 6:
            print('Sarash. Early Iron Age Shaman of the Cill Nas Emrys clan who killed all the flowers in the Vale of Flowers. +1 STR, +1 DEX, +1 PER, +1 CONV, Otherworldly Visage 1, Second Sight 1, Shame 1 Binding. Of common Daradjan Lineage.')
        elif second_roll == 7:
            print('Juras Bell. Early Iron Age Enchanter to King Gileas of Finleth; by legend he summoned the Wild Hunt. +1 STR, +1 PER, +1 MEM, +1 WILL, +1 WIS, Second Sight 1. Of common Daradjan Lineage.')
        elif second_roll == 8:
            print('Lugdallas. Early Iron Age Magician-King of Dara Dess who burnt Myr Uras to the ground for ignoring him. +1 STR, +1 PER, +1 WILL, +1 COUR, Second Sight 1, Cruelty 1 Binding. Of common Daradjan Lineage.')
        elif second_roll == 9:
            print('Lugdair. Magician-King of Dara Dess who aided King Fergus\' Highland hunts in the Wars of the Throne Thief. +1 APP, +1 STR, +1 PER, +1 WILL, +1 COUR, Second Sight 1, Cruelty 1 Binding. Descended of Lugdallas.')
        elif second_roll == 10:
            print('Gevred. Warlock of Myr Uras who killed King Lugdair; sometimes spoken of as a possible Throne Thief. +1 STR, +1 DEX, +1 PER, +1 WILL, +1 IMAG, Evil Eye 1, Second Sight 1. Of common Daradjan Lineage.')
    return


def Aurian_lineage():
    initial_roll = (randint(1, 10))
    second_roll = (randint(1, 10))
    if initial_roll < 7:
        print('Aurian Common Lineage. Peoples of the Far North who migrated into the Middle Kingdoms during the Age of Legends. +1 STR, +1 STAM, -1 EMP, Cursed at Sea 2 Binding (which manifests as a penalty to all Tests when on the open water). Descended of Heth.')
    elif initial_roll < 9:
        if second_roll == 1:
            print('Orfeydda. War Leader of the Aurians that invaded the Middle Kingdoms, and first Aurian King of Therapoli. +1 STR, +1 STAM, +1 WILL, +1 COUR, -1 EMP, Mask of Command 1, Cursed at Sea 2 Binding. A son of Heth.')
        elif second_roll == 2:
            print('Odyr. First Aurian Lord of Ogruth and a Golden Knight of An-Athair. +1 APP, +1 STR, +1 STAM, +1 PRE, Love\'s Grace 1, Cursed at Sea 2 Binding. Of common Aurian Lineage')
        elif second_roll == 3:
            print('Helggar. First Aurian Lord of Andria and a Golden Knight of An-Athair. +1 APP, +1 STR, +1 STAM, +1 PER, +1 PRE, Love\'s Grace 1, Cursed at Sea 2 Binding. Of common Aurian Lineage.')
        elif second_roll == 4:
            print('Ballir. Warrior-poet of Edain who codified the early Auric Eddera, about their journey to Danias. +1 STR, +1 STAM, +1 MEM, +1 IMAG, -1 EMP, Cursed at Sea 2 Binding. Of common Aurian Lineage.')
        elif second_roll == 5:
            print('Boros. the Old Warrior born in the Far North who lived long enough to become a Golden Knight of An-Athair. +1 APP, +1 STR, +1 STAM, +1 PRE, -1 EMP, Otherworldly Visage 2, Cursed at Sea 2 Binding. Of common Aurian Lineage.')
        elif second_roll == 6:
            print('Phallas-Theyr. Founder of Aurian Kingdom of Dainphalia, and a sacker of the Green Temple. +1 APP, +1 STR, +1 STAM, +1 PRE, -1 CONV, -1 EMP, Vanity 3 Binding, Cursed at Sea 2 Binding. A son of Heth.')
        elif second_roll == 7:
            print('Ferga. King of Edain during the Aurian War against the Spring Queens of An-Athair. +1 STR, +1 STAM, +1 TECH, +1 WIS, Cursed at Sea 2 Binding. A son of Heth.')
        elif second_roll == 8:
            print('Orfewain. Aurian King of Therapoli who sought peace between Aurians, Athairis, and Danians after the fall of An-Athair. +1 STR, +1 STAM, +1 REAS, +1 COUR, +1 WIS, Mask of Command 1. Son of Orfeydda, son of Heth.')
        elif second_roll == 9:
            print('Gunhilne. Queen of Edain after the death of the Dragon King Petraeus, briefly renouncing the Divine King. +1 APP, +1 STR, +1 STAM, +1 IMAG, +1 PRE, -1 EMP, Cursed at Sea 2 Binding. Of common Aurian Lineage.')
        elif second_roll == 10:
            print('Fortias. the Brave The Great Hero of the wars against the Last Worm King; killer of Githwaine and first High King of Therapoli and the Four Kingdoms. +1 STR, +1 STAM, +1 PER, +1 COUR, -1 EMP, Unveil 2, Cursed at Sea 2 Binding. Of common Aurian Lineage.')
    else:
        if second_roll == 1:
            print('Theodras. Bronze Age Hero who briefly conquered Mal Irama. +1 STR, +1 STAM, +1 COUR, -1 EMP, Cursed at Sea 2 Binding. Of common Aurian Lineage.')
        elif second_roll == 2:
            print('Aelfric. Bronze Age Hero, the first Aurian to return by ship to the Far North. +1 APP, +1 STR, +1 STAM, +1 DEX +1 IMAG, +1 PRE, -1 EMP. Son of a Mermaid.')
        elif second_roll == 3:
            print('Aethelias. Bronze Age Umisi Hero who bound ten Wyverns to his service. +1 APP, +1 STR,  -1 STAM, + 1 DEX, +1 PER, +1 PRE, +1 WIS, Otherworldly Visage 1, Cursed at Sea 2 Binding. Son of a Faerie Spirit.')
        elif second_roll == 4:
            print('Ashketil. Greatest Aurian Hero of the Black Day Battle against the Empire. +1 STR, +1 STAM, +1 PRE, +1 COUR, -1 EMP, Resolute Aura 1, Cursed at Sea 2 Binding. Of common Aurian Lineage.')
        elif second_roll == 5:
            print('Ceolsig. Early Iron Age Umisi rebel War Chief, who had his own Kingdom of Ceol for a while. +1 STR, +1 STAM, +1 PER, -1 EMP, Cursed at Sea 2 Binding. Of common Aurian Lineage.')
        elif second_roll == 6:
            print('Eadric. Early Iron Age bandit-hunter, famed for hunting centaurs. +1 STR, +1 STAM, +1 COUR, -1 EMP, Cursed at Sea 2 Binding. Of common Aurian Lineage.')
        elif second_roll == 7:
            print('Thored. Iron Age artisan and alchemist, famed for silver and pewter works. +1 STR, +1 STAM, +1 TECH, Cursed at Sea 2 Binding Of common Aurian Lineage.')
        elif second_roll == 8:
            print('Forwain. the Wise High King of Therapoli who ended the Wars of the Throne Thief and restored peace to the land. +1 STR, +1 STAM, +1 PER, +1 COUR, +1 WIS, Unveil 2, Cursed at Sea 2 Binding. Descended of Fortias.')
        elif second_roll == 9:
            print('Alefric. Recent artisan, sage, and Magister of the University of Therapoli, who briefly allowed the Gray Dream Cult into the University. +1 STR, +1 STAM, +1 TECH, +1 IMAG, Madness 1 Binding, Cursed at Sea 2 Binding. Descended of Thored.')
        elif second_roll == 10:
            print('Hurias. Recent scholar of the University of Truse, author of On the last Worm, a definitive history of Githwaine. +1 STR, +1 STAM, +1 MEM, +1 REAS, -1 EMP, Cursed at Sea 2 Binding. Of common Aurian Lineage.')
    return


def Danian_lineage():
    initial_roll = (randint(1, 10))
    second_roll = (randint(1, 10))
    if initial_roll < 7:
        print('Danian Common Lineage. The original inhabitants of the Danian Peninsula. -1 STAM, +1 PRE, +1 WIS. Descended of Geniche.')
    elif initial_roll == 7:
        if second_roll == 1:
            print('Ledwyr. of Old Danian Hero-Hunter who rode with the Black Hunter before barring him from Liadaine. -1 STAM, +1 WILL, +1 PRE, +1 WIS. Of common Danian Lineage.')
        elif second_roll == 2:
            print('Culainn. Founder of the City of Therapoli and a Binder of the Black Hunter, considered the First Danian King. -1 STAM, +1 TECH, +1 PRE, +1 WIS. Of common Danian Lineage.')
        elif second_roll == 3:
            print('Bridea. Ancient Queen of Na Caila and the Western Danias, and a Binder of the Black Hunter. -1 STAM, +1 REAS, +1 PRE, +1 WIS. Of common Danian Lineage.')
        elif second_roll == 4:
            print('Erginus. A King of Therapoli and founder of the first Great School of Therapoli (later to become its University). -1 STAM, +1 IMAG, +1 REAS, +1 PRE, +1 WIS. Of common Danian Lineage.')
        elif second_roll == 5:
            print('Myrad. Lunatic King of Therapoli and builder of fabulous dungeons, who imprisoned the Kings in Exile. -1 STAM, +1 TECH, +1 IMAG, +1 PRE, +1 WIS, Vanity 1 Binding, Madness 1 Binding. Son of Erginus.')
        elif second_roll == 6:
            print('Eriador. One of the Hundred Sons of Myrad, who aided the Kings in Exile and was thrown in his father\'s dungeons for his betrayal. -1 STAM, +1 TECH, +1 IMAG, +1 PRE, +1 CONV, +1 WIS, Vanity 1 Binding, Madness 1 Binding. Son of Myrad, son of Erginus.')
        elif second_roll == 7:
            print('Ergist. One of the Hundred Sons of Myrad, who freed his brother Eriador and the other prisoners of their father\'s dungeons. -1 STAM, +1 TECH, +1 PER, +1 IMAG, +1 PRE, +1 WIS, Vanity 1 Binding, Madness 1 Binding. Son of Myrad, son of Erginus.')
        elif second_roll == 8:
            print('Maderyd. One of the Hundred Sons of Myrad, who imprisoned his father in his own dungeons through trickery and guile. -1 STAM, +1 TECH, +1 DEX, +1 IMAG, +1 PRE, +1 WIS, Forked Tongue 2, Vanity 1 Binding, Madness 1 Binding. Son of Myrad, son of Erginus.')
        elif second_roll == 9:
            print('Eldyr. One of the Hundred Sons of Myrad, a Magician who destroyed and sealed his father\'s dungeons, dooming his father to a slow death. -1 STAM, +1 TECH, +1 PER, +1 IMAG, +1 PRE, +1 CONV, +1 WIS, See the Path 3, Second Sight 1, Madness 2 Binding. Son of Myrad, son of Erginus.')
        elif second_roll == 10:
            print('Myrius. the Sane One of the Hundred Sons of Myrad, who was selected by his brothers as the next King of Therapoli after the death of their father. -1 STAM, +1 TECH, +1 IMAG, +1 PRE, +1 WIS, Vanity 2 Binding. Son of Myrad, son of Erginus.')
    elif initial_roll < 10:
        if second_roll == 1:
            print('Ymaire of Therapoli. Magician and Sorceress who counseled her brother King Myriad to accept the presence of the Golden Realm. -1 STAM, +1 TECH, +1 IMAG, +1 REAS, +1 PRE, +1 CONV, +1 WIS, See the Path 3, Second Sight 2. Daughter of Eldyr, son of Myrad, son of Erginus.')
        elif second_roll == 2:
            print('Tara. The first Danian Spring Queen, and the famed Queen of the Tiria Wold, the Lady of Gold and Silver. +1 APP, +1 PRE, +1 COUR, +1 WIS, Spellbinding Form 3. Of common Danian Lineage.')
        elif second_roll == 3:
            print('Hyrval. King of Erid More famed for his hospitality, and companion of the Athairi Hero Gyrfryd. +1 STR, -1 STAM, +1 PRE, +1 WIS, +1 EMP. Of common Danian Lineage.')
        elif second_roll == 4:
            print('The Wyvern. King Brutal ruler of the Manon Mole, King of the Talon Knights. +1 STR, +1 DEX, +1 PER, +1 IMAG, +1 PRE, Iron Body 1, Warlike Visage 1, Cruelty 1 Binding. Son of a Wyvern.')
        elif second_roll == 5:
            print('Gable. Hero-Magician of Mageva who briefly served the Wyvern King; sister to Gawer. -1 STAM, +1 WILL, +1 IMAG, +1 PRE, +1 WIS. Of common Danian Lineage.')
        elif second_roll == 6:
            print('Gawer. Hero-Knight of Mageva who briefly served the Wyvern King; brother to Gable. -1 STAM, +1 PRE, +1 COUR, +1 WIS. Of common Danian Lineage.')
        elif second_roll == 7:
            print('Rhyd-Narys. King of Aprenna, famed for his battle skills, and ruler of the Western Danians. +1 STR, +1 STAM, +1 PRE, +1 WIS. Of common Danian Lineage.')
        elif second_roll == 8:
            print('Efraine. The Lady of Av Luin, who built its stone piers and port, and who tread the Lost Halls of the Red Wastes. -1 STAM, +1 PER, +1 PRE, +1 WIS. Of common Danian Lineage.')
        elif second_roll == 9:
            print('Peredock. A Danian Golden Knight of AnAthair, and lover of Efraine. +1 APP, -1 STAM, +1 PRE, +1 CONV, +1 WIS, Love\'s Grace 1. Of common Danian Lineage.')
        elif second_roll == 10:
            print('Gareint. A Danian Golden Knight of AnAthair, and fast companion of Peredock. +1 APP, +1 STR, -1 STAM, +1 PRE, +1 WIS, Love\'s Grace 1. Of common Danian Lineage.')
    else:
        if second_roll == 1:
            print('Bremen. A Danian Warlord sworn to Dauban Hess, and the Successor King of Dania. +1 STR, -1 STAM, +1 PRE, +1 WIS. Of common Danian Lineage.')
        elif second_roll == 2:
            print('Petraeus. One of the first Danian Dragon Kings, who took up arms against the Emperor\'s Court. +1 STR, -1 STAM, +1 PER, +1 WILL, +1 PRE, +1 WIS, Heroic Aura 1. Son of Bremen.')
        elif second_roll == 3:
            print('Fallair Far-Seer. A Warlord of Umat who sailed with Audra the Voyager against the pirates of the Barren Coast, and then into the Far North. -1 STAM, +1 PER, +1 IMAG, +1 PRE, +1 WIS. Of common Danian Lineage.')
        elif second_roll == 4:
            print('Gwyrfyr the First. King of Dania during the War of the Last Worm, and companion to Fortias the Brave. -1 STAM, +1 DEX, +1 IMAG, +1 PRE, +1 WIS. Of common Danian Lineage.')
        elif second_roll == 5:
            print('Cadr. First Hero to return alive from the ruins of Lost Liss Dyved to report no sign of a burial place for Githwaine. +1 STR, -1 STAM, +1 PRE, +1 COUR, +1 WIS, Otherworldly Visage 2. Of common Danian Lineage.')
        elif second_roll == 6:
            print('Usker. Bard and composer of the epic song cycle, the Adura Draconum Fini ("Last of the Dragon Kings\'"). -1 STAM, +1 IMAG, +1 PRE, +1 WIS. Of common Danian Lineage.')
        elif second_roll == 7:
            print('Perein. Sure-handed Knight of Tamatra who became the King of Dania. -1 STAM, +1 DEX, +1 PRE, +1 WIS. Of common Danian Lineage.')
        elif second_roll == 8:
            print('Cilad. King of Dania, hero of the Black Day Battle, and founder of the University of Newgate. -1 STAM, +1 DEX, +1 REAS, +1 PRE, +1 COUR, +1 WIS. Son of Perein.')
        elif second_roll == 9:
            print('Gargos. Huntsman of the Umisi hills who feuded with the High King Fergus of Therapoli over hunting rights; aided Golgosyn during the Wars of the Throne Thief. -1 STAM, +1 STR, +1 DEX, +1 PRE, +1 WIS. Of common Danian Lineage.')
        elif second_roll == 10:
            print('Golgosyn the Stone. The Stone King of Umis during the Wars of the Throne Thief who was pardoned for his role in the deaths of three High Kings of Therapoli, one by his own hand, but still widely suspected as a possible Throne Thief.+1 STR, +1 IMAG, +1 PRE, +1 COUR, +1 WIS, Implacable Mask 2. Of common Danian Lineage.')
    return


def Athairi_lineage():
    initial_roll = (randint(1, 10))
    second_roll = (randint(1, 10))
    if initial_roll < 7:
        print('An Athairi Common Lineage. The "Children of the Wood", the early inhabitants of the Erid Wold and central Dania. +1 APP, -1 STR, +1 WIS. Descended of Geniche.')
    elif initial_roll < 9:
        if second_roll == 1:
            print('Gyrfyrd. A Golden Knight of An-Athair that single-handedly defended the castle of Hyrval. +1 APP, +1 STAM, +1 WILL, +1 PRE, +1 WIS, Love\'s Grace 1. Of common Athairi Lineage.')
        elif second_roll == 2:
            print('Penwyrd. A Golden Knight of An-Athair, rescuer of Queen Tara of the Tiria Wold from the Wyvern King. +1 APP, -1 STR, +1 DEX, +1 PRE, +1 EMP, +1 WIS, Love\'s Grace 1. Of common Athairi Lineage.')
        elif second_roll == 3:
            print('Dyrk. A Golden Knight of An-Athair; he captured the Wyvern King. +1 APP, +1 DEX, +1 PRE, +1 COUR, +1 WIS, Love\'s Grace 1. Of common Athairi Lineage.')
        elif second_roll == 4:
            print('Benreuth. A Golden Knight of An-Athair famed for dueling with Ferne over the still-beating heart of the Maiden of Abeuth. +1 APP, +1 STR, +1 STAM, +1 PRE, +1 WIS, Love\'s Grace 1, Jealousy 3 Binding (towards any Lover). Of common Athairi Lineage.')
        elif second_roll == 5:
            print('Ferne. A Golden Knight of An-Athair famed for dueling with Benreuth over the still-beating heart of the Maiden of Abeuth +1 APP, +1 STR, +1 STAM, +1 PRE, +1 WIS, Love\'s Grace 1, Jealousy 3 Binding (towards any Lover). Of common Athairi Lineage.')
        elif second_roll == 6:
            print('Penwyn. A Golden Knight of An-Athair famed for outpacing the Wild Hunt through the Eduins. +1 APP, -1 STR, +1 DEX, +1 PRE, +1 WIS, Love\'s Grace 1. Of common Athairi Lineage.')
        elif second_roll == 7:
            print('Terwaine. A Golden Knight of An-Athair; first Erl of Westmark, he defeated King Rhyd-Narys in single combat. +1 APP, +1 STR, +1 IMAG, +1 PRE, +1 WIS, Love\'s Grace 1. Of common Athairi Lineage.')
        elif second_roll == 8:
            print('Urien. A Golden Knight of An-Athair and first Erl of Uthmark. +1 APP, -1 STR, +1 TECH, +1 PRE, +1 WIS, Love\'s Grace 1. Of common Athairi Lineage.')
        elif second_roll == 9:
            print('Mendred. A Golden Knight of An-Athair; he saved Ara Basi from the brigands of Cyr Faira Mal. +1 APP, +1 STR, +1 WILL, +1 PRE, +1 WIS, Love\'s Grace 1. Of common Athairi Lineage.')
        elif second_roll == 10:
            print('Sherwaine. A Golden Knight of An-Athair; he defeated the Dentyn Dragon. +1 APP, +1 STR, +1 DEX, +1 PER, +1 PRE, +1 COUR, +1 WIS, Heroic Aura 1, Love\'s Grace 1. Of common Athairi Lineage.')
    else:
        if second_roll == 1:
            print('Dun Tibra. The first Spring Queen of An-Athair of note, who opened the Green Temple to the World. +1 APP, -1 STR, +1 IMAG, +1 REAS, +1 PRE, +1 WIS, Spellbinding Form 3. Of common Athairi Lineage.')
        elif second_roll == 2:
            print('Beverra. A Spring Queen of An-Athair, whose voice made hearts break. +1 APP, -1 STR, +1 PRE, +1 WIS, Glorious Voice 3, Haunting Voice 3, Spellbinding Form 3. Of common Athairi Lineage.')
        elif second_roll == 3:
            print('Sylill. A Spring Queen of An-Athair, who foretold the Golden Realm\'s end. +1 APP, -1 STR, +1 PER, +1 PRE, +1 WIS, Oracular Dream 2, Spellbinding Form 3, Madness 1 Binding. Of common Athairi Lineage.')
        elif second_roll == 4:
            print('Ymaire of An-Athair. A Spring Queen of An-Athair; she soothed the captured Wyvern King and defanged him. +1 APP, -1 STR, +1 DEX, +1 PRE, +1 WIS, Serene Voice 2, Spellbinding Form 3. Of common Athairi Lineage.')
        elif second_roll == 5:
            print('Iala. A Spring Queen of An-Athair; she founded the University of Truse. +1 APP, -1 STR, +1 IMAG, +1 PRE, +1 CONV, +1 WIS, Spellbinding Form 3. Of common Athairi Lineage.')
        elif second_roll == 6:
            print('Maera. A Spring Queen of An-Athair; she charmed the first Aurian Lords and knighted them with Gold. +1 APP, -1 STR, +1 PRE, +1 EMP, +1 WIS, Spellbinding Form 3. Of common Athairi Lineage.')
        elif second_roll == 7:
            print('Megara. A Spring Queen of An-Athair; she buried enchantments along the borders to keep the Aurians out. +1 APP, +1 STR, +1 REAS, +1 PRE, +1 CONV, +1 WIS, Spellbinding Form 3. Of common Athairi Lineage.')
        elif second_roll == 8:
            print('Morfane. A Spring Queen of An-Athair and reputed the greatest Magician of the Golden Realm. +1 APP, +1 STR, +1 TECH, +1 WILL, +1 IMAG, +1 PRE, +1 CONV, +1 EMP, +1 WIS, Imperious Tongue 1, Second Sight 1, Spellbinding Form 3. By rumor daughter of a Faerie Spirit.')
        elif second_roll == 9:
            print('Urfante. Winter Century Witch that aided the hunters of Githwaine and led Gobelin to the Green Temple. +1 APP, +1 STR, +1 TECH, +1 PER, +1 WILL, +1 IMAG, +1 PRE, +1 CONV, +1 EMP, +1 WIS, Imperious Tongue 1, Second Sight 2, Spellbinding Form 3. Descended of Morfane.')
        elif second_roll == 10:
            print('Arfane. Early Iron Age Witch called The Queen of Ghosts, who dwelt in the Witch\'s Cairns and is considered a possible Throne Thief. +1 APP, +1 STR, +1 TECH, +1 PER, +1 WILL, +1 IMAG, +1 PRE, +1 CONV, +1 EMP, +1 WIS, Imperious Tongue 1, Otherworldly Visage 2, Second Sight 2, Spellbinding Form 3. Descended of Urfante, descendant of Morfane.')
    return


def Archaic_lineage():
    initial_roll = (randint(1, 10))
    second_roll = (randint(1, 10))
    if initial_roll < 7:
        if second_roll < 4:
            print('Numean Common Lineage. One of the three Tribes of the Moon that founded Urune Dure. -1 STAM, +1 PRE, +1 EMP. Descended of Urige, daughter of Yhera.')
        elif second_roll < 8:
            print('Galean Common Lineage. One of the three Tribes of the Moon that founded Urune Dure. +1 STR, +1 CONV, -1 WIS. Descended of the Gorgonae.')
        else:
            print('Amean Common Lineage. One of the three Tribes of the Moon that founded Urune Dure. -1 STR, +1 IMAG, +1 WIS. Descended of Geniche (adopted by Adjia).')
    elif initial_roll == 7:
        if second_roll == 1:
            print('Urige. The Ancestress-Mother of the Numeans. +1 TECH, +1 IMAG, +1 PRE, +1 EMP, +1 WIS. Daughter of Yhera.')
        elif second_roll == 2:
            print('Heleana. The founder of the city of Mercria and a Binder of the Black Hunter. +1 APP, -1 STAM, +1 TECH, +1 PRE, +1 EMP. Of common Numean Lineage.')
        elif second_roll == 3:
            print('Adameia. The founder of the city of Amora and a Binder of the Black Hunter. +1 TECH, +1 IMAG, +1 PRE, +1 CONV, +1 COUR, +1 EMP, +1 WIS. Descended of Urige, daughter of Yhera.')
        elif second_roll == 4:
            print('Pherusa. The founder of the city of Euchale and a Binder of the Black Hunter. +1 STR, +1 TECH, +1 CONV, -1 WIS. Of common Galean Lineage.')
        elif second_roll == 5:
            print('Babi. The leader of the Durean colonists of Dania and a Binder of the Black Hunter. +1 STR, +1 TECH, +1 REAS, +1 CONV, -1 WIS. Of common Galean Lineage.')
        elif second_roll == 6:
            print('Golo. Early Magician-Queen who had Daedekamani as a lover. -1 STAM, +1 WILL, +1 IMAG, +1 REAS, +1 PRE, +1 EMP, +1 WIS, Otherworldly Visage 2, Second Sight 1. Daughter of Djara.')
        elif second_roll == 7:
            print('Lagaris. The founder of the city of Lagapoli and a Binder of the Black Hunter. +1 APP, +1 STR, +1 TECH, +1 PRE, +1 CONV, -1 WIS. Of common Galean Lineage.')
        elif second_roll == 8:
            print('Arraca. Greatest silver and goldsmith of ancient Durea, whose work is still unparalleled today. -1 STR, +1 TECH, +1 IMAG, +1 EMP, +1 WIS. Of common Amean Lineage.')
        elif second_roll == 9:
            print('Illare. The founder of the city of Illagos and a Binder of the Black Hunter. +1 APP, +1 STR, +1 TECH, +1PRE, +1 CONV, -1 WIS. Of common Galean Lineage.')
        elif second_roll == 10:
            print('Sara Hammergreia. The first Carrion Queen of the Rethet Thesa. +1 STR, +1 WILL, +1 CONV, +1 COUR, -1 WIS, Terrifying Mask 1. Of common Galean Lineage.')
    else:
        if second_roll == 1:
            print('Amandrea. The fastest Durean of legend, who outran the Wild Hunt to warn her sisters. -1 STR, +1 STAM, +1 DEX, +1 IMAG, +1 WIS. Of common Amean Lineage.')
        elif second_roll == 2:
            print('Arkida. A trickster who secretly aided Thula in her Raid on Urune Dure, but later was redeemed by her love for another. +1 STR, +1 DEX, +1 WILL, +1 IMAG, +1 CONV, Love\'s Grace 1, Second Sight 1. Of common Galean Lineage.')
        elif second_roll == 3:
            print('Gorgo. A Carrion Queen of the Rethet Thesa who captured Agall, and sacker of Asark. +1 STR, +1 STAM, +1 CONV, +1 COUR, -1 WIS Of common Galean Lineage.')
        elif second_roll == 4:
            print('Russela. A Carrion Queen of the Rethet Thesa who captured Agall, and later seduced Coromat. +1 APP, -1 STR, +1 IMAG, +1 PRE, +1 WIS. Of common Amean Lineage.')
        elif second_roll == 5:
            print('Evaka. A Carrion Queen of the Rethet Thesa who captured Agall. -1 STAM, +1 PER, +1 PRE, +1 EMP. Of common Numean Lineage.')
        elif second_roll == 6:
            print('Nicea. A daughter of Illiki the Bull, who rebuilt the Gates of Urune Dure. +1 APP, +1 STR, +1 STAM, +1 TECH, +1 PRE, +1 EMP. Of common Numean Lineage.')
        elif second_roll == 7:
            print('Hestra. A great magician of the Dureans, and the first to bind ghosts and spirits into Runes. -1 STAM, +1 IMAG, +1 PRE, +1 EMP, Otherworldly Visage 1, Second Sight 2. Of common Numean Lineage.')
        elif second_roll == 8:
            print('Hannath Hammergreia. The last of the Rethet Thesa; she had Nine Lives, and was the last Binder of the Black Hunter. +1 APP, +1 STR, +1 DEX, +1 WILL, +1 CONV, +1 COUR, +1 WIS, Terrifying Mask 1, Courageous Aura 2, Heroic Aura 2. Descended of Sara Hammergreia.')
        elif second_roll == 9:
            print('Hectale. One of the last Defenders of Urune Dure, called the Killer of Giants. +1 STR, +1 DEX, +1 IMAG, +1 COUR, +1 WIS. Of common Amean Lineage.')
        elif second_roll == 10:
            print('Ferise. The last warrior to leave Urune Dure, bearing the Cult Statue of Djara now in the city of Labira. +1 STR,  +1 STAM, +1 WILL, +1 CONV, -1 WIS, Unearthly Mask 3. Of common Galean Lineage.')
    return


def Unusual_lineage():
    print('Generating unusual lineage')
    initial_roll = (randint(1, 10))
    second_roll = (randint(1, 10))
    if initial_roll < 4:
        if second_roll == 1:
            print('A Mermaid. Half-human sea folk, often found along calm coasts. +1 APP, +1 STR, +1 STAM, +1 DEX +1 PRE, -1 EMP. Descended of Agave and Ammon Agdah.')
        elif second_roll == 2:
            print('A Siren. Half-human sea folk found in the deeper oceans and rougher coasts, hostile to Men; guardians of Lost Urune Dure.+1 APP, +1 STR, +1 DEX, +1 PRE, +1 CONV, -1 EMP. Haunting Voice 3. Descended of Agave and Irre.')
        elif second_roll == 3:
            print('A Centaur. Half-human, half-horse, found in isolated woods. +1 STR, +1 STAM, +1 DEX, -1 WILL, -1 WIS. Descended of Ammon Agdah.')
        elif second_roll == 4:
            print('A Satyr. Half-human, half-goat, found in isolated woods. +1 APP, +1 STR, +1 STAM, +1 DEX, +1 PRE, -1 WILL, -1 EMP, -1 WIS, Lust 3 Binding. Descended of Ammon Agdah or Cyrus.')
        elif second_roll == 5:
            print('A Dragon. A great magical beast of The Known World, now rare. +2 STR, +2 STAM, +1 PER, +1 MEM, +1 PRE, +1 COUR, Iron Body 3. Children of Geteema.')
        elif second_roll == 6:
            print('A Wyrm. A lesser form of Earth-Dragon, still found in dark places. +2 STR, +1 STAM, +1 PER, +1 PRE, Iron Body 2. Children of Geteema.')
        elif second_roll == 7:
            print('A Wyvern. A winged but armless kind of Dragon, often found in high mountains. +1 STR, +1 PER, +1 PRE, Iron Body 1 Descended of Dragons, the children of Geteema.')
        elif second_roll == 8:
            print('A Giant. A great malformed semi-human; virtually extinct after the Fall of Urune Dure. -2 APP, +2 STR, +2 STAM, -1 IMAG Children of Geteema.')
        elif second_roll == 9:
            print('A Griffin. A half-eagle, half-lion, common to the Pallithanes of Palatia but capable of being found anywhere. +1 DEX, +1 PER, +1 COUR, +1 WIS, -1 EMP Descended of Ammon Agdah.')
        elif second_roll == 10:
            print('A Faerie Spirit. An Otherworld Spirit of the woods, trees, hills, earth, or stone. +1 APP, -1 STAM, + 1 DEX, +1 PER, +1 PRE, +1 WIS, Otherworldly Visage 1. Descended of Geniche.')
    elif initial_roll < 7:
        if second_roll == 1:
            print('An Archai. Celestial messengers for the Queen of Heaven. +1 APP, +1 DEX, +1 REAS, +1 PRE, +1 CONV, Silver Tongue 2. Children of the Stars of Heaven.')
        elif second_roll == 2:
            print('An Ashaliel. Celestial Guardians of Adjia\'s Virtue. +1 APP, +1 PER, +1 WILL, +1 CONV, -1 EMP, Unearthly Mask 2. Children of Yhera.')
        elif second_roll == 3:
            print('A Kheribeal. Celestial Guardians of the Sacred Tree of Yhera. +1 APP, +1 STR, +1 PER, +1 CONV, -1 EMP, Unearthly Mask 2. Children of Djara.')
        elif second_roll == 4:
            print('An Ariel. Guardian banshees of the Throne of Yhera. +1 APP, +1 MEM, +1 PRE, +1 CONV, Imperious Tongue 2. Children of Yhera.')
        elif second_roll == 5 or 6:
            print('An Urfanim. Mountain spirits, guardians of natural sacred spaces. +1 APP, +1 STAM, +1 PRE, +1 CONV, Charismatic Mask 2. Children of Yhera.')
        elif second_roll == 7:
            print('A Seraphi. Singing banshee guardians. +1 APP, +1 PER, +1 PRE, +1 CONV, Honeyed Tongue 2. Children of Geniche.')
        else:
            print('An Aereffim. Guardian faerie spirits of wood and water. +1 APP, +1 IMAG, +1 PRE, +1 CONV, Spellbinding Form 2. Children of Ami and Dieva.')
    elif initial_roll < 11:
        if second_roll == 1:
            print('A Dhureleal. Spirit Guides in the Otherworld and Underworld. +1 APP, +1 MEM, +1 PRE, +1 CONV, -1 EMP, Clear Mind 2. Children of Ami and Agdah.')
        elif second_roll == 2:
            print('A Ghazarab Spirit Guides for Magicians and Warlocks. +1 APP, +1 MEM, +1 WIS, +1 CONV, -1 EMP, Enlightened Tongue 2. Children of Dieva and Daedekamani.')
        elif second_roll == 3:
            print('A Golodriel. Angels of Justice, servants to both Hathhalla and Seedre in the Underworld. +1 APP, +1 MEM, +1 PER, +1 CONV, -1 EMP, Sense Guilt 2. Children of Dieva and Seedre.')
        elif second_roll == 4:
            print('A Sharab Deceal. Furies, servants to Hathhalla. +1 APP, +1 STR, +1 MEM, +1 CONV, -1 EMP, -1 WIS, Terrifying Mask 2. Children of Geniche and Irre.')
        elif second_roll == 5:
            print('A Bharab Dzerek. Berserker Spirits of Rage. +1 APP, +1 STR, +1 WILL, +1 CONV, -1 EMP, -1 WIS, Voice of Fury 2. Children of Geteema and Irre.')
        elif second_roll == 6:
            print('A Nephilim. "Sphinx" Spirits; questioners and spirits of doubt. +1 APP, +1 IMAG, +1 PRE, +1 CONV, -1 EMP, Forked Tongue 2. Children of Ligrid.')
        else:
            print('A Gamezhiel. Tempter spirits, succubae and incubi. +1 APP, +1 WILL, +1 PRE, +1 CONV, -1 EMP, Dreadful Visage 2. Children of Ligrid and Irre.')
    return


def parent_attitude():
    attitude = (randint(1, 10))
    if attitude == 1:
        print(' is a Family Enemy. They hate your guts, or you hate them, or both. ')  # why oh why roll
        why_oh_why = (randint(1, 10))
        if why_oh_why == 1:
            print(
                'One of you caused the death of a loved one.  Either by accident or on purpose, one of you was in some '
                'way responsible for the death of someone the other person loved.  If you caused a death, gain a '
                'Guilt 1 Binding; otherwise gain a Grief 3 Binding and a Hate 2 Binding aimed at the other person')
        elif why_oh_why == 2:
            print('One of you made a false accusation against the other.  One of you got the other in a lot of trouble '
                  'with your family, your community, your employers, or the law.  The falsely accused party gains a '
                  'Fury 1 Binding against the one who made the false accusations.')
        elif why_oh_why == 3:
            print('One of you caused a loss of standing or reputation.  Whether by gossip or direct action, one of you '
                  'blackened the reputation of the other and caused a loss of social standing.  One of you loses '
                  '2 Social Levels, and the other gains a Guilt 1 Binding.')
        elif why_oh_why == 4:
            print('One of you caused a major humiliation.  One of you must accept a Shame 1 Binding, caused by the '
                  'actions of the other.')
        elif why_oh_why == 5:
            print(
                'One of you caused a physical disability.  One of you must accept the loss of one point of a Physical '
                'Characteristic, caused by the actions of the other, who gains a Guilt 1 Binding.')
        elif why_oh_why == 6:
            print('One of you deserted or betrayed the other.  One of you left the other in the lurch, and gains a '
                  'Shame 1 Binding.')
        elif why_oh_why == 7:
            print('One of you caused the exile of the other.  One of you caused the other to be exiled from your home '
                  'and region, and gains a Guilt 1 Binding.')
        elif why_oh_why == 8:
            print(
                'One of you foiled the other\'s plans.  One of you interfered with the romantic, business, or military '
                'plans of the other, either for just cause, for sport, or by accident.  The injured party gains a '
                'Hate 1 Binding towards the other. ')
        elif why_oh_why == 9:
            print('One of you just plain rubbed the other the wrong way.  You have opposite personalities and one or '
                  'both of you thinks the other is a complete jerk.  You might have a Hate 1 Binding towards the '
                  'other person, or you might not feel bothered enough to react: your choice.')
        elif why_oh_why == 10:
            print('One of you hasn\'t a clue.  You\'ve got no idea why you have become foes.  You might have a Hate 1 '
                  'Binding towards the other person, or be a befuddled victim of someone else\'s irrational hatred: '
                  'your choice.')

    elif attitude == 2:
        print(
            ' is a Family Rival. They constantly compete with you and may be quite envious of your success, or vice versa. ')
    elif attitude == 3:
        print(
            ' is a Family Skeptic. They distrust you for some reason, though they will not actively seek to undermine you.')
    elif attitude == 4 or 5:
        print(
            ' is a Family Compatriot. They are cordial in their dealings with you, but have no special affection for you')
    elif attitude == 6 or 7:
        print(' is a Family Friend. They like you and you get along well.')
    elif attitude == 8 or 9:
        print(' is a Family Ally. You\'re very close and they will almost always take your side in family arguments.')
    elif attitude == 7:
        print(' is a Family Agent. They think you\'re great and will do just about anything you ask, and will sometimes '
              'actively seek to help you out even when you don\'t ask')
    return

def ordinal(value):
    ordval = str(value)
    if value % 100//10 != 1:
        if value % 10 == 1:
            ordval += 'st'
        elif value % 10 == 2:
            ordval += 'nd'
        elif value % 10 == 3:
            ordval += 'rd'
        else:
            ordval += 'th'
    else:
        ordval += 'th'

    return ordval

def siblings():
    siblings = (randint(1, 10))
    if siblings < 8:
        print('You have ' + str(siblings) + ' sibling(s).')
        for i in range(siblings):
            gender = (randint(1, 10))
            # roll d10 for each sibling
            # odd is male and even is female
            if gender % 2 == 0:
                print('One sibling is female.')
                print('This sibling', end="")
                parent_attitude()
            else:
                print('One sibling is male.')
                print('This sibling', end="")
                parent_attitude()
        place = (randint(1, 10))
        if place == 1:
            print('You are the youngest.')
        elif place < 9:
            if place > siblings:
                print('You were the ' + ordinal(siblings), 'child.')
            else:
                print('You were the ' + ordinal(place), 'child.')
        else:
            twins = (randint(1, 10))
            if twins == 1 and siblings == 1:
                print('You have a twin.')
            elif twins == 1 and siblings > 1:
                print('You have a twin. You are both the youngest in the family and have ' + str(
                    siblings - 1) + ' other sibling(s).')
            elif twins < 9:
                print('You have a twin. You were the ' + ordinal(twins) + ' and have ' + str(
                    siblings - 1) + ' other sibling(s).')
            if twins == 9 or 10 and siblings >= 2:
                triplets = (randint(1, 10))
                if triplets == 1:
                    print('You are part of a triplet and have ' + str(
                        siblings - 2) + ' sibling(s). You and the other triplets are the youngest.')
                elif triplets == 9 or 10 and siblings >= 3:
                    quadruplets = (randint(1, 10))
                    if quadruplets == 1:
                        print('You are part of a quadruplet and have ' + str(
                            siblings - 3) + ' sibling(s). You and the other quadruplets are the youngest.')
                    elif quadruplets == 9 or 10 and siblings >= 4:
                        quintuplets = (randint(1, 10))
                        if quintuplets == 1:
                            print('You are part of a quintuplet and have ' + str(
                                siblings - 4) + 'sibling(s). You and the other quintuplets are the youngest.')
                        elif quintuplets == 9 or 10 and siblings >= 5:
                            sextuplets = (randint(1, 10))
                            if sextuplets == 1:
                                print('You are part of a sextuplet and have an older sibling')
                            elif sextuplets == 9 or 10 and siblings >= 6:
                                print('You are part of a septuplet.')
                            else:
                                print('You are part of a sextuplet and have an younger sibling')
                        else:
                            print('You are part of a quintuplet and have ' + str(
                                siblings - 4) + ' sibling(s). You and the other quintuplets are the oldest.')
                    else:
                        print('You are part of a quadruplet and have ' + str(
                            siblings - 3) + ' sibling(s). You and the other quadruplets are the oldest.')
                else:
                    print('You are part of a triplet and have ' + str(
                        siblings - 2) + ' sibling(s). You and the other triplets are the oldest.')
    else:
        print('You are an only child.')
    return


def unusual_circumstances():
    circumstances = (randint(1, 10))

    if circumstances == 10:
        print('Your birth was unusual!')
        unusual_circumstances = (randint(1, 10))
        if unusual_circumstances == 1:
            print('You were abandoned and raised as a foundling.  You lose a point of EMP*.')
        elif unusual_circumstances == 2:
            print(
                'You were separated from your parent(s) at a young age by war or disaster and don\'t know where - or even \n'
                'possibly who - they are*.')
        elif unusual_circumstances == 3:
            print(
                'Your parent(s) are in exile, banished by your local ruler.  You gain a Hate 1 Binding aimed at the \n'
                'person who exiled your parent(s)*.')
        elif unusual_circumstances == 4:
            print('Your parent(s) are involved in a conspiracy or plot.  Gain 3 Training Points in the Intrigue Skill.')
        elif unusual_circumstances == 5:
            print(
                'Your parent(s) are involved in a longstanding feud.  Gain an Enemy family or clan.6Your parent(s) sent \n'
                'you to live with relatives, and while you know where they are, you haven\'t seen them since. You lose a \n'
                'point of EMP.')
        elif unusual_circumstances == 6:
            print(
                'Your parent(s) went missing in the local forest or wilderlands.  You gain a Fear 1 Binding of the place \n'
                'that took your parents.')
        elif unusual_circumstances == 7:
            print(
                'Your parent(s) were actually spies or agents of an Adversary to the rulers of your home.  Choose their \n'
                'patron in consultation with your Guide, and you can secretly take Spy as your starting Occupation.')
        elif unusual_circumstances == 8:
            print(
                'Your parent(s) fled from another region or Culture and live in the Culture you rolled either secretly \n'
                'or under the protection of the local ruler.  Gain an Enemy (from your true home) and an Ally (here)*.')
        elif unusual_circumstances == 9:
            print(
                'Your parent(s) were secretly involved in a Gray Dream Mystery Cult.  Gain Cult Lore (Gray Dream Mystery \n'
                'Cult) as an Everyman Skill and you may secretly take Priest (Gray Dream Mystery Cult) as your starting Occupation.')
    else:
        print('It was a normal birth. (No unusual circumstances)')
    return


def birth_sign():
    print('Generating your Birth Sign')
    birth_sign = (randint(1, 12))
    influence = (randint(1, 10))

    if influence < 7:
        print('Mild Influence')
        if birth_sign == 1:
            print('Birth Sign is the Ram: +1 Stam, -1 Will')
        elif birth_sign == 2:
            print('Birth Sign is the Sun Bull: +1 Str, -1 Reas')
        elif birth_sign == 3:
            print('Birth Sign is the Sky Twins: +1 Emp, -1 Stam')
        elif birth_sign == 4:
            print('Birth Sign is the Scarab: +1 Tech, -1 Imag')
        elif birth_sign == 5:
            print('Birth Sign is Sun Lion: +1 Cour, -1 Wis')
        elif birth_sign == 6:
            print('Birth Sign is the Maiden: +1 App, -1 Conv')
        elif birth_sign == 7:
            print('Birth Sign is the Scales: +1 Men, -1 Pre')
        elif birth_sign == 8:
            print('Birth Sign is the Sphinx: +1 Per, -1 Emp')
        elif birth_sign == 9:
            print('Birth Sign is the Archer: +1 Dex, - 1 Emp')
        elif birth_sign == 10:
            print('Birth Sign is the Dragon: +1 Pre, -1 App')
        elif birth_sign == 11:
            print('Birth Sign is the Star-Child: +1 Wis, -1 Str')
        elif birth_sign == 12:
            print('Birth Sign is the Serpent: +1 Imag, -1 Tech')
    elif influence < 10:
        print('Moderate Influence')
        if birth_sign == 1:
            print('Birth Sign is the Ram: +1 Stam, +1 Str, -1 Will')
        elif birth_sign == 2:
            print('Birth Sign is the Sun Bull: +1 Str, +1 Pre, -1 Reas')
        elif birth_sign == 3:
            print('Birth Sign is the Sky Twins: +1 Emp, +1 Conv, -1 Stam')
        elif birth_sign == 4:
            print('Birth Sign is the Scarab: +1 Tech, +1 Reas, -1 Imag')
        elif birth_sign == 5:
            print('Birth Sign is Sun Lion: +1 Cour, +1 Mem, -1 Wis')
        elif birth_sign == 6:
            print('Birth Sign is the Maiden: +1 App, +1 Reas, -1 Conv')
        elif birth_sign == 7:
            print('Birth Sign is the Scales: +1 Men, +1 Reas, -1 Pre')
        elif birth_sign == 8:
            print('Birth Sign is the Sphinx: +1 Per, +1 Will, -1 Emp')
        elif birth_sign == 9:
            print('Birth Sign is the Archer: +1 Dex, +1 Per, - 1 Emp')
        elif birth_sign == 10:
            print('Birth Sign is the Dragon: +1 Pre, +1 Will, -1 App')
        elif birth_sign == 11:
            print('Birth Sign is the Star-Child: +1 Wis, +1 Conv, -1 Str')
        elif birth_sign == 12:
            print('Birth Sign is the Serpent: +1 Imag, +1 Wis, -1 Tech')
    else:
        print('Strong Influence!')
        if birth_sign == 1:
            print('Birth Sign is the Ram: +2 Stam, +1 Str, -1 Per, -1 Will')
        elif birth_sign == 2:
            print('Birth Sign is the Sun Bull: +2 Str, +1 Pre, -1 Reas, -1 Dex')
        elif birth_sign == 3:
            print('Birth Sign is the Sky Twins: +2 Emp, +1 Conv, -1 Stam, -1 Cour')
        elif birth_sign == 4:
            print('Birth Sign is the Scarab: +2 Tech, +1 Reas, -1 Imag, -1 Dex')
        elif birth_sign == 5:
            print('Birth Sign is Sun Lion: +2 Cour, +1 Mem, -1 Wis, -1 Tech')
        elif birth_sign == 6:
            print('Birth Sign is the Maiden: +2 App, +1 Reas, -1 Conv, -1 Per')
        elif birth_sign == 7:
            print('Birth Sign is the Scales: +2 Men, +1 Reas, -1 Pre, -1 App')
        elif birth_sign == 8:
            print('Birth Sign is the Sphinx: +2 Per, +1 Will, -1 Emp, -1 Imag')
        elif birth_sign == 9:
            print('Birth Sign is the Archer: +2 Dex, +1 Per, - 1 Emp, -1 Conv')
        elif birth_sign == 10:
            print('Birth Sign is the Dragon: +2 Pre, +1 Will, -1 App, -1 Conv')
        elif birth_sign == 11:
            print('Birth Sign is the Star-Child: +2 Wis, +1 Conv, -1 Str, -1 Cour')
        elif birth_sign == 12:
            print('Birth Sign is the Serpent: +2 Imag, +1 Wis, -1 Tech, -1 Will')
    return


def birth_omen():
    heroic_campaign = input('Is this a Heroic campaign? (y/n): ')
    print('Generating your Birth Omens')
    if heroic_campaign == 'y':
        omen = (randint(1, 20))
        if omen == 1:
            # pick d3+1 on ill omen
            print('Doomed!')
            random_omen = (randint(1, 3))
            for i in range(random_omen):
                ill_omen()
            ill_omen()
        elif omen == 2:
            # randomly pick d3+1 on tricky and ill omen
            print('Tricky Destiny!')
            random_omen = (randint(1, 3))
            omen_list = [ill_omen(), tricky_omen()]
            for i in range(random_omen):
                random.choice(omen_list)
            random.choice(omen_list)
        elif omen == 3 or 4:
            print('Ill Omen.')
            ill_omen()
        elif omen == 5 or 6:
            print('Tricky Omen.')
            tricky_omen()
        elif omen < 17:
            print('A typical birth.')
        elif omen < 19:
            print('Good Omen.')
            good_omen()
        elif omen == 19:
            # great destiny - d3+1 on good or tricky
            print('Great Destiny!')
            random_omen = (randint(1, 3))
            omen_list = [good_omen(), tricky_omen()]
            for i in range(random_omen):
                random.choice(omen_list)
            random.choice(omen_list)
        else:
            # rare - 1 race + reroll w/o rare
            rare_omen()
            reroll_omen = (randint(1, 19))
            # mew if statement list to pick reroll omen
            if omen == 1:
                print('Doomed!')
                random_omen = (randint(1, 3))
                for i in range(random_omen):
                    ill_omen()
                ill_omen()
            elif omen == 2:
                print('Tricky Destiny!')
                random_omen = (randint(1, 3))
                omen_list = [ill_omen(), tricky_omen()]
                for i in range(random_omen):
                    random.choice(omen_list)
                random.choice(omen_list)
            elif omen == 3 or 4:
                print('Ill Omen.')
                ill_omen()
            elif omen == 5 or 6:
                print('Tricky Omen.')
                tricky_omen()
            elif omen < 17:
                print('A typical birth.')
            elif omen < 19:
                print('Good Omen.')
                good_omen()
            else:
                print('Great Destiny!')
                random_omen = (randint(1, 3))
                omen_list = [good_omen(), tricky_omen()]
                for i in range(random_omen):
                    random.choice(omen_list)
                random.choice(omen_list)

    if heroic_campaign == 'n':
        omen = (randint(1, 100))
        if omen < 3:
            # d3 + 1 ill omen
            print('Doomed!')
            random_omen = (randint(1, 3))
            for i in range(random_omen):
                ill_omen()
            ill_omen()
        elif omen < 7:
            # d3+1 on tricky and ill omen
            # randomly pick d3+1 on tricky and ill omen
            print('Tricky Destiny!')
            random_omen = (randint(1, 3))
            omen_list = [ill_omen(), tricky_omen()]
            for i in range(random_omen):
                random.choice(omen_list)
            random.choice(omen_list)
        elif omen < 16:
            print('Ill Omen.')
            ill_omen()
        elif omen < 26:
            print('Tricky Omen.')
            tricky_omen()
        elif omen < 76:
            print('A typical birth')
        elif omen < 96:
            print('Good Omen.')
            good_omen()
        elif omen < 100:
            # great destiny - d3+1 on good or tricky
            print('Great Destiny!')
            random_omen = (randint(1, 3))
            omen_list = [good_omen(), tricky_omen()]
            for i in range(random_omen):
                random.choice(omen_list)
            random.choice(omen_list)
        else:
            # rare - 1 race + reroll w/o rare
            rare_omen()
            reroll_omen = (randint(1, 99))
            # mew if statement list to pick reroll omen
            if omen < 3:
                print('Doomed!')
                random_omen = (randint(1, 3))
                for i in random_omen:
                    ill_omen()
                ill_omen()
            elif omen < 7:
                print('Tricky Destiny!')
                random_omen = (randint(1, 3))
                omen_list = [ill_omen(), tricky_omen()]
                for i in random_omen:
                    random.choice(omen_list)
                random.choice(omen_list)
            elif omen < 16:
                print('Ill Omen.')
                ill_omen()
            elif omen < 26:
                print('Tricky Omen.')
                tricky_omen()
            elif omen < 76:
                print('A typical birth.')
            elif omen < 96:
                print('Good Omen.')
                good_omen()
            else:
                print('Great Destiny!')
                random_omen = (randint(1, 3))
                omen_list = [good_omen(), tricky_omen()]
                for i in random_omen:
                    random.choice(omen_list)
                random.choice(omen_list)


def good_omen():
    goodOmen = (randint(1, 10))
    if goodOmen == 1:
        print('The Great Star is seen in the night sky. You are meant for great things: +1 WILL, +1 PRE.')
    elif goodOmen == 2:
        print(
            'The Herald Star is seen in the night sky. You will be greeted with courtesy wherever you go: +1 PRE, +1 IMAG.')
    elif goodOmen == 3:
        print('The Morning Star is seen in the night sky. You will be fortunate in love: +1 EMP, +1 APP.')
    elif goodOmen == 4:
        print('An auroch or great bull is seen nearby. You will lead a life of vigor: +1 STAM, +1 WILL.')
    elif goodOmen == 5:
        print('A white stag is seen nearby. You will lead a noble life:  +1 CONV, +1 PRE.')
    elif goodOmen == 6:
        print('A rainbow is seen overhead. Yours will be a life of joy and plenty: +1 PRE, +1 TECH.')
    elif goodOmen == 7:
        print('A lion is seen nearby. You will be strong and valorous: +1 STR, +1 COUR.')
    elif goodOmen == 8:
        print('Flowers bloom nearby, even in winter. You will lead a life blessed by the Earth: +1 STAM, +1 WIS.')
    elif goodOmen == 9:
        print('A dove alights nearby. You will bring harmony to those around you: +1 EMP, +1 WIS.')
    elif goodOmen == 10:
        print('An eagle is seen overhead. You will grow up to be sharp-eyed and swift: +1 DEX, +1 PER.')
    return


def ill_omen():
    illOmen = (randint(1, 10))
    if illOmen == 1:
        print('The Red Veil falls upon the Moon.Bloodshed is in your future: +1 STR, +1 COUR, -1 EMP.')
    elif illOmen == 2:
        print(
            'The Eye of Ishraha is seen in the night sky. You will be treacherous and troublesome: +1 WILL, +1 PRE, -1 CONV.')
    elif illOmen == 3:
        print('The War Herald is seen in the night sky. Your life will be marked by war: +1 STR, +1 WILL, -1 EMP.')
    elif illOmen == 4:
        print('A great storm accompanies your birth. Your future will be unsettled: +1 IMAG, -1 COUR, -1 WILL.')
    elif illOmen == 5:
        print('Crops are spoiled nearby. You are cursed, and will grow up to be sickly: +1 PRE, -1 APP, -1 STAM.')
    elif illOmen == 6:
        print(
            'Dead animals, birds, or fish are found nearby. You are cursed to hard times and misery: +1 PRE, -1 APP, -1 EMP')
    elif illOmen == 7:
        print(
            'Wolves and carrion birds are seen nearby. Your life will be filled with violence: +1 DEX, +1 COUR, -1 EMP.')
    elif illOmen == 8:
        print('A vulture witnesses your birth. You will not be a stranger to death: +1 STAM, +1 COUR, -1 EMP.')
    elif illOmen == 9:
        print('A black stag is seen nearby. You will lead a cursed and cowardly life: +1 PRE, -1 COUR.')
    elif illOmen == 10:
        print('A ghost is seen nearby. You are touched by the Underworld: +1 WIS, -1 STR, -1 STAM, Ghost Mask1.')
    return


def tricky_omen():
    trickyOmen = (randint(1, 10))
    if trickyOmen == 1:
        print(
            'An owl watches your birth. You will be blessed with insights no one else will have: +1 WIS, +1 PER, -1 MEM.')
    elif trickyOmen == 2:
        print(
            'The Evening Star is seen in the night sky. You will lead a life filled with beauty and sensual pleasures: +1 APP, +1 PRE, -1 WILL.')
    elif trickyOmen == 3:
        print('A satyr is seen nearby. Your life will be filled with trickery: +1 IMAG, +1 PRE, -1 WILL.')
    elif trickyOmen == 4:
        print('The Conqueror Star is seen in the night sky. You will become a leader of men: +1 PRE, +1 WILL, -1 EMP.')
    elif trickyOmen == 5:
        print(
            'Archai (Star Messengers) are seen in the sky. The Heavens have taken note of your birth: +1 PRE, +1 APP, -1 EMP.')
    elif trickyOmen == 6:
        print('A red stag is seen nearby. You will lead a life of danger: +1 STAM, +1 COUR, -1 WIS.')
    elif trickyOmen == 7:
        print(
            'The Midnight Star is seen in the night sky. You\'re born lucky: 10 Fool Arcana Points to spend as you wish.')
    elif trickyOmen == 8:
        print('A wild boar is seen nearby. You will be headstrong and brash: +1 WILL, +1 COUR, -1 WIS.')
    elif trickyOmen == 9:
        print('A griffin is seen nearby. You will lead a life of invention and change: +1 TECH, +1 IMAG, -1 WILL.')
    elif trickyOmen == 10:
        print(
            'A Star Dragon is seen in the sky. Your life will be marked by mystery: +1 IMAG, +1 WIS, -1 REAS, Cryptic Mask 1.')
    return


def rare_omen():
    rareOmen = (randint(1, 10))
    if rareOmen == 1:
        print(
            'A Spirit visits your birth. You are touched by the Otherworld: +1 PER, +1 WIS, -1 STR, -1 STAM, Second Sight 2.')
    elif rareOmen == 2:
        print(
            'Hathhalla\'s Veil descends over the Sun. Your birth is an act of revenge: +1 STR, +1 PRE, -1 EMP, See Guilt 2')
    elif rareOmen == 3:
        print(
            'The Wild Hunt rages nearby. You will cause tumult and chaos wherever you go: +1 STR, +1 IMAG, -1 WILL, Voice of Fury 2.')
    elif rareOmen == 4:
        print(
            'The Sun Eater tries to consume the Sun. You will lead a life of great misfortune: +1 PRE, -1 STAM, Doubt 2 Binding.')
    elif rareOmen == 5:
        print(
            'A flood or earthquake occurs nearby. You will be surrounded by great disaster: +1 PRE, -1 STAM, -1 DEX, Evil Eye 2.')
    elif rareOmen == 6:
        print(
            'A Dragon is seen moving in the Earth nearby. Great powers will manifest in your life: +1 PRE, +1 COUR. Heroic Aura 2.')
    elif rareOmen == 7:
        print(
            'A monster is spotted nearby. Your life will be filled with insensibility: +1 STR, -1 REAS, -1 WILL, Fury 2 Binding.')
    elif rareOmen == 8:
        print('You are born with a caul. You will be a magician: +1 WIS, +1 WILL, +1 IMAG, -1 APP, Second Sight 2.')
    elif rareOmen == 9:
        print(
            'A wyrm or wyvern is seen nearby. You are destined to be a treasure-seeker: +1 PER, -1 WILL, Greed 2 Binding.')
    elif rareOmen == 10:
        print(
            'The Great Shadow falls upon the Moon. Your life will be darkened by confusion and doubt: +1 IMAG, -1 PER, -1 CONV, -1 WILL, Chaotic Aura 2.')
    return


def childhood():
    childhood_event = (randint(1, 10))
    if childhood_event < 5:
        childhood_illfortune()
    elif childhood_event < 9:
        childhood_goodfortune()
    else:
        childhood_illfortune()
        childhood_goodfortune()
    return


def childhood_illfortune():
    parent = 'none'
    sibling = 'none'
    illfortune = (randint(1, 10))
    if illfortune == 1:
        print(
            'Accident.  You lose one point of a Physical Characteristic of your choice after a terrible childhood accident.')
    elif illfortune == 2:
        print(
            'Maltreatment.  You were mistreated in the hands of a parent or family member; you lose a point of EMP, \n'
            'and gain a Fury 1 Binding and a Hate your malefactor1 Binding.')
    elif illfortune == 3:
        print('Disease.  You survived a brush with the Fever, Plague, or Rot, but lose a point of STAM.')
    elif illfortune == 4:
        print('Dropped.  You were dropped on your head while an infant, and lose a point of REAS.')
    elif illfortune == 5:
        parental_loss = (randint(1, 10))
        if parental_loss < 5:
            parent = 'Your father'
        elif parental_loss < 9:
            parent = 'Your mother'
        else:
            parent = 'Both parents'
        print(
            'Parental Loss.' + parent + ' died during your childhood. You gain a (now Dormant) Grief Binding equal to \n'
                                        'half your EMP score. You can choose whether the cause was natural or man-made; \n'
                                        'if a human hand was involved, you gain an Enemy and a Hate the responsible \n'
                                        'party 2 Binding.')
    elif illfortune == 6:
        sibling_loss = (randint(1, 6))
        print('Family Loss.' + str(
            sibling_loss) + ' siblings died during your childhood. You must gain a (now Dormant) Grief Binding \n'
                            'equal to half your EMP score. You can choose whether the cause was natural or \n'
                            'man-made; if a human hand was involved, you gain an Enemy and a Hate the responsible party 2 Binding.')
    elif illfortune == 7:
        print(
            'Torment.  You were tormented by the mockery of other children who liked making fun of you.  You lose a \n'
            'point of EMP and you gain an Ambition 2 Binding')
    elif illfortune == 8:
        print(
            'Homeless.  Your childhood home was destroyed either by natural disaster or by the hand of man.*  You may \n'
            'not receive an inheritance or heirlooms during the LifePath or in the game.')
    elif illfortune == 9:
        print(
            'Ghost.  You had an encounter with a ghost or angry Spirit.  You gain Second Sight 1 and gain a Fear Ghosts \n'
            '(or Spirits, as appropriate) 1 Binding.')
    else:
        print('Prying Eyes.  You saw something you shouldn\'t have, lose a point of COUR, and gain a Shame 1 Binding.')
    return


def childhood_goodfortune():
    goodfortune = (randint(1, 10))
    if goodfortune == 1:
        print('Dreamer. You were a precocious, creative, and inquisitive child. +1 IMAG and +1 COUR.')
    elif goodfortune == 2:
        print(
            'Childhood Patron.  You attracted the attention of strong forces and patrons in your Culture, and may begin \n'
            'Step Four of your LifePath with any Occupation from the next higher Social Class.')
    elif goodfortune == 3:
        print(
            'Active Youth.  You were an active, physical young person and may add one point to any two Physical Characteristics')
    elif goodfortune == 4:
        print(
            'Apt Pupil.  You were an attentive and responsive student.  +1 REAS and begin Step Four of the LifePath \n'
            'with 10 additional Training Points to spend.')
    elif goodfortune == 5:
        print('Save a Life.  Your quick actions and thinking saved someone\'s life.  Gain a Friend, and +1 COUR')
    elif goodfortune == 6:
        print(
            'First Love.  You found love early.  Gain a Lover, and you may add one point to EMP.  You may take a Love \n'
            'your childhood sweetheart Binding up to your EMP in Level if you\'d like.')
    elif goodfortune == 7:
        print(
            'Childhood Friend.  You had a childhood best friend with whom you are still close.  Gain a Friend, and +1 EMP')
    elif goodfortune == 8:
        # roll cultural item
        print('Heirloom.  A parent or relative has bequeathed to you an item of note, enchanted at +2. ')
        if culture == 'Athairi':
            Athairi_cultural_items()
        elif culture == 'Aurian':
            Aurian_cultural_items()
        elif culture == 'Danian':
            Danian_cultural_items()
        elif culture == 'Watchtower':
            Watchtower_cultural_items()
        elif culture == 'Daradjan':
            Daradjan_cultural_items()

    elif goodfortune == 9:
        print(
            'Spirit Blessing.  You had a wondrous encounter with a faerie or earth Spirit of some sort.  You gain Otherworldly Visage 1 and +1 WIS.')
    else:
        if culture == 'Daradjan':
            print(' During your youth you are chosen to be a member of Adjia\'s Companions, the chaste entourage that \n'
                  'accompanies  the  goddess  Adjia  in  her  hunts  and  journeys  in the  wilds. You  gain Glorious Voice  1, \n'
                  'Unearthly  Mask  1,  and +1 APP, +1 STR, +1 DEX, +1 STAM, and +1 CONV, but also gain a Fury at Men 1 Binding.')
        else:
            print(
                'Temple Assistant.  You were chosen to assist the priests or priestesses of a local Temple (dedicated \n'
                'to a God appropriate to your Culture and religion).  You gain 3 Training Points in Cult Lore \n'
                '(for your God), and +1 CONV.  You may take the Priest or Priestess Occupation as your starting Occupation if you choose.')
    return


def life_path():
    lifePath = (randint(1, 10))
    if lifePath == 1:
        print('Nothing Happened')
    elif lifePath == 2:
        Life_Path_Major_Ill_Fortune()
    elif lifePath == 3 - 4:
        Life_Path_Minor_Ill_Fortune()
    elif lifePath == 5 - 6:
        Life_Path_Minor_Good_Fortune()
    elif lifePath == 7:
        Life_Path_Major_Good_Fortune()
    elif lifePath == 8 - 9:
        Life_Path_Romance()
    else:
        Life_Path_Great_Adventure()


def Life_Path_Major_Ill_Fortune():
    LPMajorIllFortune = (randint(1, 10))

    if LPMajorIllFortune == 1:
        print('Financial Disaster.  You lost a lot of money (' + str(
            (randint(10)) * 25) + '), either through a bad business investment, \n'
                                  'gambling, or carelessness.  Roll d10 x 25 to determine how much you lost in g.  If you don\'t have enough g at the moment from previous \n'
                                  'earnings to cover the loss, then you are in debt until the loss is covered.  Gain a Shame 2 Binding.')
    elif LPMajorIllFortune == 2:
        print(
            'Blacklisted.  You somehow screwed up in your Occupation and are barred from practicing it ever again.  \n'
            'You must take a new Occupation next year from the next lower Social Class.  Gain a Shame 2 Binding.')
    elif LPMajorIllFortune == 3:
        print(
            'Addiction.  You struggle with an addiction to a drug or substance.  You lose a point of STAM and gain no \n'
            'Earnings this year, and gain both an Addiction to a Culturally appropriate Drug 1 Binding and a Shame 1 Binding.')
    elif LPMajorIllFortune == 4:
        print(
            'Public Failure.  A large and very public project of yours goes sour.  Halve your income for this year and \n'
            'every following year, and you gain a Shame 2 Binding.')
    elif LPMajorIllFortune == 5:
        print('Imprisonment.  You are (falsely?) convicted of a crime, and must spend ' + str(
            (randint(1, 6)) + (randint(1, 6))) + ' \n'
                                                 'moons imprisoned this year.  You lose your income for the year and gain no Skill Points, but you may earn Arcana Points \n'
                                                 'in the Hermit Arcana.  Next year you must succeed at a PRE Test DR 12 to remain in your chosen Occupation; if you fail, \n'
                                                 'you must select a new Occupation from the next lower Social Class.  Gain a Shame 2 Binding.')
    elif LPMajorIllFortune == 6:
        print(
            'Lose a Friend to the Enemy.  A Lover, Friend, Compatriot, or Ally is killed at the hands of one of your Enemies.  \n'
            'Gain an Enemy if you don\'t have one already, gain a Grief 2 Binding and a Hate 2 Binding against the Enemy responsible.')
    elif LPMajorIllFortune == 7:
        print(
            'Family Loss to the Enemy.  A member of your family is killed at the hands of one of your Enemies.  Gain an Enemy \n'
            'if you don\'t have one already, and gain a Grief2 Binding and a Hate 2 Binding against the Enemy responsible.')
    elif LPMajorIllFortune == 8:
        print(
            'Accident.  You cause an accident that injures or kills someone else.  Gain an Enemy (the victim or a surviving relative) and a Guilt 2 Binding.')
    elif LPMajorIllFortune == 9:
        print(
            'Rat.  You betray someone close to you, either accidentally or on purpose.  A Friend or Ally becomes an Enemy (your Guide chooses which Friend or Ally), \n'
            'and you gain a Guilt 2 Binding.')
    elif LPMajorIllFortune == 10:
        print(
            'Betrayal.  You are betrayed by the actions of someone close to you; a Friend or Ally becomes an Enemy (your Guide chooses which Friend or Ally), \n'
            'and you gain a Fury 2 Binding towards them.')
    return


def Life_Path_Minor_Ill_Fortune():
    LPMinorIllFortune = (randint(1, 10))
    if LPMinorIllFortune == 1:
        print('Financial Loss.  You lost a small amount of money (' + str(
            (randint(1, 10)) * 10) + '), either through a bad business \n'
                                     'investment, gambling, or carelessness. If you don\'t have enough g at the moment from previous earnings to cover the loss, \n'
                                     'then you are in debt until the loss is covered.  Gain a Shame 1 Binding.')
    elif LPMinorIllFortune == 2:
        print(
            'Crime Victim.  You are waylaid and robbed by a bandit, brigand, thief, or trickster.  Lose all your current starting \n'
            'cash and earnings (not including this year\'s earnings).  Gain a Shame 1 Binding.')
    elif LPMinorIllFortune == 3:
        print('Illness.  You are overcome by the Fever for part of this year.  -1 STAM.')
    elif LPMinorIllFortune == 4:
        print('Disfigurement.  You were injured or wounded in a particularly nasty way.  -1 APP.')
    elif LPMinorIllFortune == 5:
        print(
            'Gossip.  You are (falsely?) accused of something: bad behavior, a crime, responsibility for an accident, etc.  Gain a Shame 1 Binding.')
    elif LPMinorIllFortune == 6:
        print('Lose a Friend.  A Lover, Friend, Compatriot, or Ally dies of natural causes.  Gain a Grief 1 Binding.*')
    elif LPMinorIllFortune == 7:
        print('Family Loss.  A member of your family dies of natural causes. Gain a Grief 1 Binding.*')
    elif LPMinorIllFortune == 8:
        print(
            'Accident.  You are in an accident at home and are badly hurt.  Lose a point of a Physical Characteristic (your choice).')
    elif LPMinorIllFortune == 9:
        print(
            'Wounded.  You are injured in a fight or hurt at work.  Lose a point of a Physical Characteristic (your choice).')
    else:
        print('Faux Pas!  You commit a social blunder and lose a Contact, who now becomes a Skeptic.')
    return


def Life_Path_Minor_Good_Fortune():
    LPMinorGoodFortune = (randint(1, 10))
    if LPMinorGoodFortune == 1:
        print(
            'Small Treasure (cash).  You find or receive (perhaps as a reward or gift) a small amount of money.  Roll d10 x PRE to determine how much you found.')
    elif LPMinorGoodFortune == 2:
        print('Small Treasure.  You find or receive (perhaps as a reward or gift) an object of note enchanted at +1.')
        if culture == 'Athairi':
            Athairi_cultural_items()
        elif culture == 'Aurian':
            Aurian_cultural_items()
        elif culture == 'Danian':
            Danian_cultural_items()
        elif culture == 'Watchtower':
            Watchtower_cultural_items()
        elif culture == 'Daradjan':
            Daradjan_cultural_items()
    elif LPMinorGoodFortune == 3:
        print(
            'Merchant Contact.  Make a Contact among your Culture\'s Merchants or Traders, who can usually get you a 10% discount \n'
            'on all items available to your Culture, and a 5% discount on items imported from outside your Culture.')
    elif LPMinorGoodFortune == 4:
        print(
            'Outlaw Contact.  A local bandit or gang of thieves takes a liking to you.  Gain 3 Training Points in Streetwise and \n'
            'an Outlaw Contact you can call on for illicit favors.')
    elif LPMinorGoodFortune == 5:
        print(
            'Teacher.  You find a teacher who is willing to put up with you.  Gain a Contact, and you gain 3 Training Points \n'
            'for any one Trade, Martial, or Lore Skill (even if not normally on any of your available lists).')
    elif LPMinorGoodFortune == 6:
        print(
            'A Favor.  A highborn member of your Culture (from your Culture\'s Social Level 5) owes you a Favor.  You gain them \n'
            'as a Contact, and one time only they may be treated as an Ally.')
    elif LPMinorGoodFortune == 7:
        print(
            'Group Contact.  You gain the attention of a powerful group in your Culture - a guild, Temple, Order, fraternity, \n'
            'merchant House, etc.  You may treat any member of that group as a Contact.')
    elif LPMinorGoodFortune == 8:
        print(
            'Temple Assistant.   You are selected to become a temple assistant at a local Temple.  In addition to your regular \n'
            'Skills and Arcana Points for this year, you gain 3 Training Points in a Cult Lore Skill appropriate for your God, \n'
            '3 Arcana Points in the Great Priestess Arcana, and you gain a Priest or Priestess as a Contact.  You may attempt to \n'
            'take the Priest or Priestess Occupation as your Occupation next year with a +4 bonus to your roll, even if it is of a higher Social Class.')
    elif LPMinorGoodFortune == 9:
        print(
            'Visitor.  You meet a visitor or traveler from another Culture or region.  Gain a Contact from another Culture.')
    else:
        print('Reunion.  An old Lover (someone from the Romance Table) reappears in your life as a Friend.')
    return


def Life_Path_Major_Good_Fortune():
    LPMajorGoodFortune = (randint(1, 10))
    if LPMajorGoodFortune == 1:
        print('Great Treasure (cash).  You find or receive (perhaps as a reward or gift) a considerable sum of money.  '
              'Roll d10 x PRE x 10 to determine how many gc you get.')
    if LPMajorGoodFortune == 2:
        print('Great Treasure.  You find or receive (perhaps as a reward or gift) an object of note enchanted at +2.')
        if culture == 'Athairi':
            Athairi_cultural_items()
        elif culture == 'Aurian':
            Aurian_cultural_items()
        elif culture == 'Danian':
            Danian_cultural_items()
        elif culture == 'Watchtower':
            Watchtower_cultural_items()
        elif culture == 'Daradjan':
            Daradjan_cultural_items()
    if LPMajorGoodFortune == 3:
        print(
            'Musical Friend.  You meet and befriend an entertainer from your Culture - a bard, singer, musician, or \n'
            'perhaps a courtesan - who can help you socially, either by introducing you to the “right people” or perhaps \n'
            'even composing and performing works about you.  Gain a Friend, and as long as he or she is your Friend you \n'
            'may attempt to take an Occupation in the next higher Social Class at a +4 bonus on your roll.')
    if LPMajorGoodFortune == 4:
        print(
            'Outlaw Ally.  A local bandit or gang of thieves has made a blood pact with you.  Gain 3 Training Points in \n'
            'Streetwise and a single Outlaw Ally and d6 Outlaw Compatriots (gang members) that you can call on for illicit favors or muscle.')
    if LPMajorGoodFortune == 5:
        print(
            'Mentor.  You find a mentor and a patron who takes an interest in your future.  Gain an Ally, and you may add \n'
            '3 Training Points to any Trade, Martial, or Lore Skill (even if not normally on your available lists) every year.')
    if LPMajorGoodFortune == 6:
        print(
            'Noble Ally.  A highborn member of your Culture (from your Culture\'s Social Level 9 or higher) has taken an \n'
            'interest in your future.  You gain an Ally, and as long as he or she is your Ally you may attempt to take \n'
            'an Occupation in the next higher Social Class at a +4 bonus on your roll.')
    if LPMajorGoodFortune == 7:
        print(
            'Group Invitation. You are invited to join a powerful group in your Culture - a guild, Temple, Order, fraternity, \n'
            'merchant House, etc.  If you join, you may treat every member of that group as a Compatriot.   As long as you \n'
            'belong to this Group you may attempt to take an Occupation in the next higher Social Class at a +4 bonus on your roll.')
    if LPMajorGoodFortune == 8:
        print(
            'Temple Ally.   You find a patron in a local Temple who takes an interest in your future.  You gain a Priest or \n'
            'Priestess as an Ally.  You may attempt to take the Priest or Priestess Occupation next year.  As long as he or \n'
            'she is your Ally, you may also attempt to take an Occupation in the next higher Social Class with a +4 bonus to your roll.')
    if LPMajorGoodFortune == 9:
        print(
            'Visiting Friend.  You gain the trust of a visitor or traveler from another Culture or region.  Gain a Friend from another Culture.')
    if LPMajorGoodFortune == 10:
        print('Change of Heart.  Thanks to your resolve and good nature, an Enemy (your choice) becomes a Friend.')
    return


def Life_Path_Romance():
    LPRomance = (randint(1, 10))
    if LPRomance == 1:
        print(
            'Busy year.  You are very active socially this year, but your affairs are of little lasting consequence.  Gain d4 Contacts and d4 Skeptics.')
    if LPRomance == 2:
        print(
            'Short affair.  You had a short affair that was enjoyable but didn\'t really go anywhere, and you haven\'t seen '
            'your former Lover since then and have no idea what he or she might think of you.')
    if LPRomance == 3:
        print(
            'Bad Affair.  You had an affair that ended rather badly and in spectacular fashion; you may decide whether it '
            'was your fault or not.  You gain an Enemy regardless.  If it was not your fault, then you gain a Hate 1 Binding '
            'towards your former Lover.  If it was your fault, then you gain a Guilt 1 Binding.')
    if LPRomance == 4:
        print(
            'Fine Affair.  You had a pleasant affair that ended, but ended well, and you are still fairly close to your '
            'former Lover.  Gain a Friend.')
    if LPRomance == 5:
        print(
            'Competition.  You had an affair that seemed to be going well but ended when another suitor stepped in.  Your '
            'former Lover may still be a Friend if you choose (an Opponent if not), and you also gain either a Rival '
            '(if you actively dislike the competition) or a Skeptic (if you don\'t mind one way or the other), your choice.')
    if LPRomance == 6:
        print(
            'Tragic Affair.  You had an affair with someone that you greatly loved, but it ended tragically; either they died, '
            'or somehow you were separated and can never see them again.  Gain a Grief 2 Binding.')
    if LPRomance == 7:
        print(
            'Loved.  You have an affair with someone that genuinely loves you.  You gain a Lover who is willing to take a '
            'Love Binding; you may reciprocate if you want.')
    if LPRomance == 8:
        print(
            'Love a Rival.   You have an intense affair with someone that becomes a competitor.  Gain a Rival, and gain both '
            'a Jealousy 1 and either a Hate 1 or Love 1 Binding towards them (your choice).')
    if LPRomance == 9:
        print(
            'Two-timed.  You gain a Lover but discover them cheating on you with a Friend or Family member.  You choose '
            'whether your Friend or Family member becomes a Rival, Adversary, or Enemy, but you gain a Hate 1 Binding towards '
            'your (former) Friend and a Jealousy 1 Binding towards your Lover (if you end it, they\'re now a Skeptic).')
    else:
        print(
            'Missing.  You had an affair that seemed to be going great, but then your Lover went missing, and their whereabouts '
            'are currently unknown.  Gain a Grief 2 Binding.')
    return


def Life_Path_Great_Adventure():
    LPGreatAdventure = (randint(1, 10))
    if LPGreatAdventure == 1:
        print(
            'Great conflict!  You, your Family, and your Friends are swept up in a military conflict: a war between great powers \n'
            'or perhaps just some petty noblemen\'s feud (see the Recent Events Timeline Table on pages 38-39 to see if there is \n'
            'something appropriate for this year; if not, then it\'s just a small local conflict).  1d3 Friends or Family are killed \n'
            'during the event, and you gain a Grief Binding Level for each person killed.  You may take a military Occupation \n'
            '(appropriate to your Social Class; you may go up or down by one Social Class if there are none in your Social Class \n'
            'category, with an upward move requiring a PRE Test DR 10) for this year, or you may become an Outlaw for this year only.  \n'
            'If you want to remain in a Military Occupation in subsequent years, you must make a PRE Test DR 10.  If you are already \n'
            'in a military or Outlaw Occupation, double your Arcana Points and Earnings for this year.')
    elif LPGreatAdventure == 2:
        print(
            'Traveling!  You get a chance to go off exploring and traveling.  You may take the Trader, Traveler, or Scout Occupation, \n'
            'automatically gain 3 Training Points in Local Expert in each of two regions of your Choice, and gain a Contact and a \n'
            'Friend in those same two regions.  If you are already a Trader. Traveler, or a Scout, then you may double your Arcana \n'
            'Points and Earnings for the year.  After your year of travel, you can keep your new Occupation if you took one this year.')
    elif LPGreatAdventure == 3:
        print(
            'Famine!  Your home region is struck by famine and drought, and tragedy has struck close to you.   You survive, but \n'
            '1d3 Friends or Family die during the drought, either from starvation and malnutrition or as a result of banditry and brigandage.  \n'
            'You gain a Grief 1 Binding for every Friend or Family member that dies during the famine.  You earn no money this year, but \n'
            'gain your CONV in Death Arcana Points in addition to your usual Occupation-related Arcana.  If you choose, you may take an \n'
            'Outlaw Occupation this year, in which case you may gain Annual Earnings as per normal for your Outlaw Occupation.  \n'
            'However, it will take a PRE Test DR 12 to return to a non-Outlaw Occupation the following year.')
    elif LPGreatAdventure == 4:
        print(
            'Learn a Secret!  You learn a secret that has been hidden either by the actions of time and history, or by the desire \n'
            'and will of others.  This secret could be anything you and your Guide find suitable: the secret location of a treasure \n'
            'or hiding place, the true Name or identity of someone who is not who they claim to be, or perhaps a secret of History, \n'
            'such as who really killed the last Baron of Dyn Cail, etc.  The secret should gain you either a Rival (who wants to \n'
            'learn the secret for themselves) or an Enemy or an Adversary (who wants to protect the secret).  You gain double your \n'
            'usual Arcana Points this year no matter what your Occupation is.')
    elif LPGreatAdventure == 5:
        print(
            'Witness!  You witness or get a chance to participate in a major event for your Culture; choose an event for this \n'
            'year from the appropriate column in the Recent Events Timeline Table on pages 38-39, and decide with your Guide \n'
            'whether you observed or participated in the event and how.  Depending on your involvement, your Guide may assign you \n'
            'Contacts, Friends, Allies, or Enemies, and/or Bindings.  Double your Arcana Points and Earnings for this year.')
    elif LPGreatAdventure == 6:
        print(
            'Success!  You have some sort of great achievement, victory, or success that brings you to the attention of great powers.  \n'
            'You receive d10 x PRE x 10 in g in addition to your regular earnings, and gain an Ally at the highest levels of your Culture.  \n'
            'You may take any Occupation from the next highest Social Class this year without rolling.  You must also gain a Vanity 1 Binding.')
    elif LPGreatAdventure == 7:
        print(
            'Plague!  The plague and evil spirits come calling to your home region, and tragedy has struck close to you.  You survive, \n'
            'but 1d3 Friends or Family die during the plague.  You gain a Grief 1 Binding for every Friend or Family member that dies \n'
            'during the plague.  If you so choose, you may take a Culturally-appropriate Occupation related to healing, magic, or religion - \n'
            'such as Healer, Midwife, Witch, Magician, Shaman, Warlock, Sorcerer, Mage, Priest, or Priestess.  You gain your CONV in Death Arcana \n'
            'Points in addition to your usual Occupation-related Arcana.')
    elif LPGreatAdventure == 8:
        print(
            'Bloody Feud!  You, your Friends, and your Family are caught up in a deadly and bloody feud with a neighbor, rival family, \n'
            'or local ruler.  You survive, but 1d3 of your Friends and Family are killed at the hands of your Enemies.  You gain an Enemy \n'
            '(or Enemies, more accurately) if you do not have one already, and you also gain a Grief 1 Binding and a Hate your Enemy 1 Binding \n'
            'for every Relation that died.  You may take a military Occupation of your Social Class or lower (not from a higher Social Class) \n'
            'or you may become an Outlaw this year.')
    elif LPGreatAdventure == 9:
        print(
            'Persecutions!  You get caught up in some sort of mob violence that sweeps your region, either witch burnings or Gray Dream \n'
            'Mystery Cult or Forbidden Cult persecutions.  You may choose whether you and your family are the victims or are part of the mob.  \n'
            'If you are a victim of the mob, then you survive, but 1d3 Friends or Family die during the mass hysteria.  You gain a Hate your \n'
            'Tormentors 1 and a Grief 1 Binding for every Friend or Family member that dies during the persecutions.  You gain double your \n'
            'Arcana Points this year.  You lose your current Occupation and must take an Occupation from the next lower Social Class; if this \n'
            'makes you an Outlaw, then you have been driven into exile.  If you are part of the mob, you gain 1d3 Levels in a Guilt Binding, \n'
            'but you also double your Earnings this year.')
    else:
        print(
            'Brigandage!  Your home region is plagued by widespread banditry and brigandage, as heavily armed thugs wander the area looting \n'
            'and pillaging.  You may aid the bandits, hinder the bandits, fight the bandits, or join the bandits.  If you aid the bandits, \n'
            'you may double your Earnings for the year and gain an Outlaw Contact but also gain a Shame 1 Binding.  If you hinder the bandits, \n'
            'you lose your Earnings for the year but gain an Ally amongst the local rulership or law enforcement hierarchy.  If you fight the \n'
            'bandits, you may take a military Occupation of your Social Class or lower (not from a higher Social Class) if you haven\'t got one \n'
            'already.  You gain Outlaw Enemies and you also gain Compatriots amongst the local rulership or law enforcement hierarchy.  If you \n'
            'join the bandits, you take an Outlaw Occupation and may not return to your previous Occupation.  You gain 10 times your Earnings \n'
            'for this year and 2d6 Outlaw Compatriots, but you also gain an Enemy amongst the local rulership or law enforcement hierarchy and \n'
            'may well have a lot of explaining to do with Friends and Family.')
    return


answer = ''
while answer != 'n':
    print('Generating culture')
    culture = (randint(1, 10))
    if culture == 1:
        culture = 'Athairi'
        print('You were born an Athairi in a', end="")
        social_level = Athairi_birth_place()
        Athairi_parents(social_level)
    elif culture == 1 < 5:
        culture = 'Aurian'
        print('You were born an Aurian in a', end="")
        social_level = Aurian_birth_place()
        Aurian_parents(social_level)
    elif culture == 4 < 8:
        culture = 'Danian'
        print('You were born a Danian in a', end="")
        social_level = Danian_birth_place()
        Danian_parents(social_level)
    elif culture == 8:
        culture = 'Watchtower'
        print('You were born a Watchtower King in a', end="")
        social_level = Watchtower_birth_place()
        Watchtower_parents(social_level)
    else:
        culture = 'Daradjan'
        print('You were born a Daradjan in a', end="")
        social_level = Daradjan_birth_place()
        Daradjan_parents(social_level)

    unusual_circumstances()
    birth_sign()
    birth_omen()
    childhood()
    siblings()
    print('Your mother', end="")
    parent_attitude()
    print('Your father', end="")
    parent_attitude()
    print('Generating Life Path')
    print('Year 1: ')
    life_path()
    print('Year 2: ')
    life_path()
    print('Year 3: ')
    life_path()
    print('Year 4: ')
    life_path()
    print('Year 5: ')
    life_path()
    print('Character creation complete.')
    answer = input('Would you like to create a new character? (y/n): ')
    if answer == 'n':
        print('Goodbye!')

raw_input()
