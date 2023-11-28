# The script of the game goes in this file.
#$winCount = 0
#$Enemies = ("Goblin","Orc","Demon","Thief")
#$Enemy_Max_Health = {"Goblin": 5,"Orc":12, "Demon": 10, "Thief": 7}
#$Enemy_Damage = {"Goblin": 2,"Orc":3, "Demon": 2, "Thief": 2}

#$player_max_hp = 10
#$player_hp = player_max_hp
#$player_damage = 2


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Narrator")


# The game starts here.

label start:
    call player_stats
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene dungeon entrance

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    "You come across the entrance to a Dungeon and decide to explore."
    while player_hp>0:
        
        if encounter_type > .25:
            call encounter_stats
            "You have come across a [enemy] and have to fight it!"
            while enemy_hp >0:
                menu:
                    "Attack":
                        $enemy_hp -= player_damage
                        "That looked like it hurt. Enemy has [enemy_hp] health"
                    "Don't Attack":
                        "You don't do anything"
                #Enemy Turn
                $player_hp -= enemy_damage
                "The [enemy] attacks reducing your health to [player_hp]."
            $winCount += 1
            call win_screen
        elif encounter_type <= .25:
            call encounter_stats
            pass

label player_stats:
    $winCount = 0
    
    $player_max_hp = 10
    $player_hp = player_max_hp
    $player_damage = 2

    
label encounter_stats:
    $Enemies = ("Goblin","Orc","Demon","Thief")
    $Enemy_Max_Health = {"Goblin": 5,"Orc":12, "Demon": 10, "Thief": 7}
    $Enemy_Damage = {"Goblin": 2,"Orc":3, "Demon": 2, "Thief": 2}
    #$Enemy_Setting = {"Goblin":}
    
    $enemy = renpy.random.choice(Enemies)
    $enemy_max_hp = Enemy_Max_Health[enemy]
    $enemy_hp = enemy_max_hp
    $enemy_damage =Enemy_Damage[enemy]

    $encounter_type = renpy.random.random()

label win_screen:
    "You won!. You have now won [winCount] battles."
    
