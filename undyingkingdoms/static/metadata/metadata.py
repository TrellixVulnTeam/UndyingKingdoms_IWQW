from undyingkingdoms.models.achievements import Achievement


metadata_races = ['Human', 'Elf', 'Dwarf', 'Goblin']

metadata_backgrounds = ['Warlord', 'Engineer', 'Merchant', 'Rogue']

kingdom_names = ["Faenoth", "Aldoroth", "Ecthalion"]

infiltration_missions = ['scout military', 'pilfer', 'burn crops', 'sow distrust']

rations_terminology = [(0, "None"), (0.25, "Quarter"), (0.5, "Half"), (1, "Normal"), (2, "Double"), (3, "Triple")]

all_buildings = ['house', 'field', 'pasture', 'mill', 'mine', 'fort', 'stables', 'guild', 'bank', 'lair']

all_achievements = {
    'land': Achievement(name="land", category="reach_x_amount_in_one_age", sub_category="land",
                        display_title="From Coast to Coast",
                        description="Have your county reach x amount of land in one playthrough.",
                        tier1=175, tier2=250, tier3=300, tier4=400, tier5=500, maximum_tier=5,
                        points_rewarded=5),
    'population': Achievement(name="population", category="reach_x_amount_in_one_age", sub_category="population",
                              display_title="Like Rabbits...",
                              description="Have your county reach x population in one playthrough.",
                              tier1=750, tier2=1500, tier3=2250, tier4=3000, tier5=4000, maximum_tier=5,
                              points_rewarded=5),
    'gold': Achievement(name="gold", category="reach_x_amount_in_one_age", sub_category="gold",
                        display_title="Midas Touch",
                        description="Have your county reach x gold in one playthrough.",
                        tier1=1000, tier2=2000, tier3=3000, tier4=4000, tier5=5000, maximum_tier=5,
                        points_rewarded=5),
    'wood': Achievement(name="wood", category="reach_x_amount_in_one_age", sub_category="wood",
                        display_title="Where Did the Forests Go?",
                        description="Have your county reach x wood in one playthrough.",
                        tier1=500, tier2=1000, tier3=1500, tier4=2000, tier5=2500, maximum_tier=5,
                        points_rewarded=5),
    'iron': Achievement(name="iron", category="reach_x_amount_in_one_age", sub_category="iron",
                        display_title="Heart of Iron",
                        description="Have your county reach x iron in one playthrough.",
                        tier1=500, tier2=1000, tier3=1500, tier4=2000, tier5=2500, maximum_tier=5,
                        points_rewarded=5),
    'dwarf_class_leader': Achievement(name="dwarf_class_leader", category="class_leader", sub_category="dwarf",
                                      display_title="Lord Under the Mountain!",
                                      description="Become the leader of your kingdom while playing as Dwarves.",
                                      maximum_tier=1,
                                      points_rewarded=15),
    'human_class_leader': Achievement(name="human_class_leader", category="class_leader", sub_category="human",
                                      display_title="Return of the King",
                                      description="Become the leader of your kingdom while playing as Humans.",
                                      maximum_tier=1,
                                      points_rewarded=15),
    'elf_class_leader': Achievement(name="elf_class_leader", category="class_leader", sub_category="elf",
                                    display_title="King of the Forest",
                                    description="Become the leader of your kingdom while playing as Elves.",
                                    maximum_tier=1,
                                    points_rewarded=15)
}

# Racial/Class Modifiers (A modifier of 0 means +0%. A modifier of 1 would mean +100%)
happiness_modifier = {'Goblin': ("Infighting", -2)}
birth_rate_modifier = {'Elf': ("Elders", -0.15), 'Goblin': ("Expendable", 0.10)}
death_rate_modifier = {}
income_modifier = {'Merchant': ("Silver Tongue", 0.15)}
offensive_power_modifier = {'Warlord': ("Relentless", 0.10)}
infiltration_success_modifier = {'Rogue': ("Master of Disguise", 0.10)}
production_per_worker_modifier = {'Dwarf': ("Dwarven Made", 0.15), 'Engineer': ("Craftsman", 0.20)}
defense_per_citizen_modifier = {'Elf': ("Citizen Militia", 1.00)}
food_consumed_modifier = {'Dwarf': ("Ravenous", 0.15)}

all_armies = ["peasant", "archer", "soldier", "elite", "monster"]

game_descriptions = {"attack": "How much power a unit has when attacking another county.",
                     "defence": "How much power a unit has when defending your county.",
                     "health": "Health affects how many of your units die in battle.",
                     "available_workers": "Any citizen not in the military or employed, is available. These workers "
                                          "will add production to your city which can be used to build new buildings. "
                                          "Unused production generates gold.",
                     "upkeep": "Monthly cost of paying your soldiers' salaries.",
                     "upkeep_daily": "Today's expected salary cost."}
