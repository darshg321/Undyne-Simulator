from random import randint

neutral_list = ["* Undyne flips her spear impatiently.",
"* Undyne points heroically towards the sky.",
"* Undyne flashes a menacing smile.",
"* Undyne draws her finger across her neck.",
"* Undyne bounces impatiently.",
"* Undyne towers threateningly.",
"* Smells like sushi." ]

late_list = ["* Smells like angry fish.",
"* Undyne is hyperventilating.",
"* Undyne is smashing spears on the ground.",
"* Undyne's eye is twitching involuntarily."]

low_hp_list = ["* Water rushes around you.",
"* Flower pollen drifts in front of you.",
"* The wind is howling...",
"* The spears pause for a moment."]

def dialogue_gen(stage):
    if stage == "neutral":
        num_generated = randint(0, 6)
        dialogue_generated = neutral_list[num_generated]
        return dialogue_generated
    
    if stage == "late":
        num_generated = randint(0, 3)
        dialogue_generated = late_list[num_generated]
        return dialogue_generated
    
    if stage == "low hp":
        num_generated = randint(0, 3)
        dialogue_generated = low_hp_list[num_generated]
        return dialogue_generated