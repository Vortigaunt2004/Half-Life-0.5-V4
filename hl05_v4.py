import random

# Player class
class Player:
    def __init__(self, health, armor, ammo):
        self.health = health
        self.armor = armor
        self.ammo = ammo
        
    def attack(self):
        self.ammo -= 1
        return random.randint(10, 20)
    
    def defend(self, damage):
        if self.armor >= damage:
            self.armor -= damage
        else:
            remaining_damage = damage - self.armor
            self.armor = 0
            self.health -= remaining_damage
            
    def is_alive(self):
        return self.health > 0

# Enemies list
enemies = [
    {
        'name': 'Combine Soldier',
        'health': 50,
        'damage': 10
    },
    {
        'name': 'Zombie',
        'health': 30,
        'damage': 5
    },
    {
        'name': 'Headcrab',
        'health': 20,
        'damage': 5
    },
    {
        'name': 'Antlion',
        'health': 40,
        'damage': 15
    },
    {
        'name': 'Manhack',
        'health': 15,
        'damage': 5
    },
    {
        'name': 'Strider',
        'health': 100,
        'damage': 20
    },
    {
            'name': 'Shock Trooper',
            'health': 80,
            'damage': 25
    },
    {
            'name': 'Pit Drone',
            'health': 80,
            'damage': 10
    },
    {
            'name': 'Gonarch',
            'health': 600,
            'damage': 35
    },
    {
            'name': 'Alien Grunt',
            'health': 80,
            'damage': 25
    },
    {
            'name': 'Bullsquid',
            'health': 60,
            'damage': 15
    },
    {

        'name': 'Father Grigori',
        'health': 120,
        'damage': 37

    },
    {
        'name': 'Gargantua',
        'health': 200,
        'damage': 25
    },
    {
        'name': 'Ichthyosaur',
        'health': 80,
        'damage': 20
    },
    {
        'name': 'Barnacle',
        'health': 10,
        'damage': 3
    },
    {
        'name': 'Houndeye',
        'health': 30,
        'damage': 10
    },
    {
        'name': 'Vortigaunt',
        'health': 60,
        'damage': 35
    }
]

# Random encounter function
def random_encounter():
    enemy = random.choice(enemies)
    print(f"You've encountered a {enemy['name']} with {enemy['health']} health!\n")
    return enemy

# Character dialogue
eli_dialogue = [
    "Eli: We don't go there anymore.\n",
    "Eli: You're doing great!\n",
    "Eli: We'll make a sharpshooter out of you yet.\n",
    "Eli: Keep it up, Gordon!\n"
]

alyx_dialogue = [
    "Alyx: You know Dr. Kleiner's gonna be mad if you break his record.\n",
    "Alyx: Gordon, why don't you position yourself near the panel over there and wait for my word?\n",
    "Alyx: I'm glad you're on our side.\n",
    "Alyx: Let's get out of here!\n"
]

gman_dialogue = [
    "Gman: Rise and shine, Mr. Freeman. Rise and shine.\n",
    "Gman: I'm afraid we'll be deviating a bit from standard analysis procedures today.\n",
    "Gman: I have recommended your services to my employers.\n",
    "Gman: We'll see each other again, in the flesh.\n"
]

kleiner_dialogue = [
    "Kleiner: Ah, Gordon! The very man I hoped to see.\n",
    "Kleiner: I've made a few modifications, but still, your gravity gun should be able to handle them.\n",
    "Kleiner: Ah, Gordon, there you are!\n",
    "Kleiner: Now, now, there's nothing to be nervous about.\n"
]

barney_dialogue = [
    "Barney: Hey, hey, he's back!\n",
    "Barney: You're heading for the Lambda Complex, aren't you?\n",
    "Barney: Good luck, buddy!\n",
    "Barney: I'm with ya, Doc!\n"
]

# Game loop
player = Player(100, 50, 30)

while True:
    # Random encounter
    enemy = random_encounter()
    
    # Battle loop
    while enemy['health'] > 0 and player.is_alive():
        # Player turn
        print(f"Your health: {player.health} | Your armor: {player.armor} | Your ammo: {player.ammo}\n")
        action = input("What would you like to do? (attack/defend) \n")
        
        if action ==  'attack':
            damage = player.attack()
            enemy['health'] -= damage
            print(f"You dealt {damage} damage to the {enemy['name']}!\n")
        elif action == 'defend':
            enemy_damage = random.randint(5, 15)
            player.defend(enemy_damage)
            print(f"You defended against the {enemy['name']}'s attack, taking {enemy_damage} damage!\n")
            
        # Enemy turn
        if enemy['health'] > 0:
            player_damage = random.randint(5, enemy['damage'])
            player.defend(player_damage)
            print(f"The {enemy['name']} attacked you, dealing {player_damage} damage!\n")
            
    # End of battle
    if player.is_alive():
        print(f"You defeated the {enemy['name']}!\n")
        loot = random.randint(10, 30)
        loot2 = random.randint(0, 30)
        player.ammo += loot
        player.health += loot2
        player.armor += loot2
        print(f"    You found {loot} ammo!\n    You got {loot2} health and armor!")
    else:
        print(f"You were killed by the {enemy['name']}!\n")
        break
        
    # Character dialogue
    character = random.choice([eli_dialogue, alyx_dialogue, gman_dialogue, kleiner_dialogue, barney_dialogue])
    print(f"\n{random.choice(character)}\n")
