from django.shortcuts import render

# Create your views here.
def show_main(request):
    # Data yang akan dikirimkan ke tampilan HTML
    weapon_data = [
        {
            'name': 'Buster Sword',
            'attack': 91,
            'magic': 91,
            'description': 'A large broadsword that has inherited the hopes of those who fight',
            'ability': '<strong>Focused Thrust</strong> - “Lunge toward an enemy with a piercing strike that hits multiple times. Significantly increases stagger.”',
            'proficiency_bonus': 'None; the Buster Sword ability starts out mastered',
            'location': "Cloud's starting weapon"
        },
        {
            'name': 'Iron Blade',
            'attack': 77,
            'magic': 105,
            'description': 'A greatsword cast from carefully selected iron ore',
            'ability': '<strong>Triple Slash</strong> - “Slash three enemies in quick succession, dealing more damage with each blow.”',
            'proficiency_bonus': 'Strike three or more enemies',
            'location': 'Receive automatically in Chapter 3 after the trip to the Scrap Boulevard'
        },
        {
            'name': 'Nail Bat',
            'attack': 30,
            'magic': 30,
            'description': 'A crudely reinforced baseball bat. Designed to beat the living tar out of anything and everything',
            'ability': '<strong>Disorder</strong> - “Deliver a devastating attack and switch modes in one fluid motion.”',
            'proficiency_bonus': 'Strike with Attack or Strong Attack after switching modes',
            'location': "Reward for 'Kids on Patrol' sidequest (Chapter 8). If missed, this is sold in some shops in later chapters"
        },
        {
            'name': 'Mythril Saber',
            'attack': 46,
            'magic': 138,
            'description': 'An immense sword made from magic-infused mythril ore',
            'ability': '<strong>Blade Burst</strong> - “Unleash a wave of non-elemental mako energy at an enemy in front of you with a slash of your sword.”',
            'proficiency_bonus': 'Finish off an enemy',
            'location': 'Buy at Wall Market weapon shop (Chapter 14)'
        },
        {
            'name': 'Twin Stinger',
            'attack': 73,
            'magic': 73,
            'description': 'A sword forged from two existing blades. Well suited for materia',
            'ability': '<strong>Counterstance</strong> - “Brace for attacks and retaliate with a powerful slash.”',
            'proficiency_bonus': 'Unleash a counterattack.',
            'location': 'Shinra Tower (Chapter 17) -  in The Drum after reuniting with Barret'
        }
    ]

    context = {
        'name': 'Dhemas Wicaksono Nugroho',  
        'class': 'PBP E',
        'weapon_data': weapon_data
    }

    return render(request, "main.html", context)
