import random

neutral_list = ["Undyne flips her spear impatiently.",
"Undyne points heroically towards the sky.",
"Undyne flashes a menacing smile.",
"Undyne draws her finger across her neck.",
"Undyne bounces impatiently.",
"Undyne suplexes a large boulder, just because she can.",
"Undyne thinks of her friends and pounds the ground with her fists.",
"Undyne holds her fist in front of her and shakes her head.",
"Undyne towers threateningly.",
"Smells like sushi." ]

late_list = ["Smells like angry fish.",
"Undyne is hyperventilating.",
"Undyne is smashing spears on the ground.",
"Undyne's eye is twitching involuntarily.",
"Undyne's eyes dart around to see if this is a prank."]

low_hp_list = ["Water rushes around you.",
"Flower pollen drifts in front of you.",
"The wind is howling...",
"The spears pause for a moment."]

def dialogue_gen(stage):
    if stage == "neutral":
        num_generated = random.randint(1, 10)
        dialogue_generated = neutral_list[num_generated]
        return dialogue_generated
    
    if stage == "late":
        num_generated = random.randint(1, 5)
        dialogue_generated = late_list[num_generated]
        return dialogue_generated
    
    if stage == "failed_plead":
        dialogue_generated = "You told Undyne you didn't want to fight. But nothing happened."
        return dialogue_generated
    
    if stage == "success_plead":
        dialogue_generated = "You told Undyne you just want to be friends. She remembers someone... Her attacks became a little less extreme."
        return dialogue_generated
    
    if stage == "low_hp":
        num_generated = random.randint(1, 4)
        dialogue_generated = low_hp_list[num_generated]
        return dialogue_generated