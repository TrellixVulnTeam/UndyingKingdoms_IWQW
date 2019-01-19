from undyingkingdoms.models.achievements import Achievement
from undyingkingdoms.models.buildings import Building
from undyingkingdoms.models.armies import Army

kingdom_names = ["Faenoth", "Aldoroth"]

all_achievements = {
    'land': Achievement(name="land", category="reach_x_amount_in_one_age", sub_category="land",
                        display_title="From Coast to Coast",
                        description="Have your county reach x amount of land in one playthrough.",
                        tier1=175, tier2=250, tier3=300, tier4=400, tier5=500, maximum_tier=5,
                        points_rewarded=5),
    'population': Achievement(name="population", category="reach_x_amount_in_one_age", sub_category="population",
                              display_title="Like Rabbits...",
                              description="Have your county reach x population in one playthrough.",
                              tier1=550, tier2=750, tier3=1000, tier4=1500, tier5=2000, maximum_tier=5,
                              points_rewarded=5),
    'gold': Achievement(name="gold", category="reach_x_amount_in_one_age", sub_category="gold",
                        display_title="Midas Touch",
                        description="Have your county reach x gold in one playthrough.",
                        tier1=1250, tier2=2000, tier3=None, tier4=None, tier5=None, maximum_tier=2,
                        points_rewarded=5),
    'wood': Achievement(name="wood", category="reach_x_amount_in_one_age", sub_category="wood",
                        display_title="Where Did the Forests Go?",
                        description="Have your county reach x wood in one playthrough.",
                        tier1=100, tier2=200, tier3=None, tier4=None, tier5=None, maximum_tier=2,
                        points_rewarded=5),
    'iron': Achievement(name="iron", category="reach_x_amount_in_one_age", sub_category="iron",
                        display_title="Heart of Iron",
                        description="Have your county reach x iron in one playthrough.",
                        tier1=50, tier2=100, tier3=None, tier4=None, tier5=None, maximum_tier=2,
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
                                      points_rewarded=15)
}
rations_terminology = [(0, "None"), (0.25, "Quarter"), (0.5, "Half"), (1, "Normal"), (2, "Double"), (3, "Triple")]

all_buildings = ['houses', 'fields', 'pastures', 'mills', 'mines', 'forts', 'stables', 'guilds']

dwarf_buildings = {'houses': Building(base_name='houses',
                                      class_name='cottage',
                                      total=25,
                                      production_cost=20,
                                      labour_maintenance=0,
                                      gold=50,
                                      wood=25,
                                      output=1,
                                      description='Each {} adds +{} to your birth rate.'),
                   'fields': Building(base_name='fields',
                                      class_name='grain field',
                                      total=20,
                                      production_cost=20,
                                      labour_maintenance=5,
                                      gold=50,
                                      wood=10,
                                      output=25,
                                      description='Each {} provides enough grain for {} people a day.'),
                   'pastures': Building(base_name='pastures',
                                        class_name='goat farm',
                                        total=5,
                                        production_cost=20,
                                        labour_maintenance=15,
                                        gold=50,
                                        wood=10,
                                        output=30,
                                        description='Each {} can feed {} people a day, but excess milk is lost.'),
                   'mills': Building(base_name='mills',
                                     class_name='lumber mill',
                                     total=3,
                                     production_cost=25,
                                     labour_maintenance=15,
                                     gold=50,
                                     wood=25,
                                     output=3,
                                     description='Each {} produces {} wood a day.'),
                   'mines': Building(base_name='mines',
                                     class_name='iron mine',
                                     total=1,
                                     production_cost=35,
                                     labour_maintenance=15,
                                     gold=75,
                                     wood=15,
                                     output=3,
                                     description='Each {} produces {} iron a day.'),
                   'forts': Building(base_name='forts',
                                     class_name='stronghold',
                                     total=0,
                                     production_cost=50,
                                     labour_maintenance=15,
                                     gold=100,
                                     wood=50,
                                     output=6,
                                     description='Dwarf {}\'s are very effective and add +{}% to your county\'s defence value.'),
                   'stables': Building(base_name='stables',
                                       class_name='Pony Stables',
                                       total=0,
                                       production_cost=25,
                                       labour_maintenance=5,
                                       gold=40,
                                       wood=25,
                                       output=4,
                                       description='Each {} lets your army return from battle {}% faster.'),
                   'guilds': Building(base_name='guilds',
                                      class_name='Thieves\' Guild',
                                      total=0,
                                      production_cost=45,
                                      labour_maintenance=10,
                                      gold=50,
                                      wood=25,
                                      output=5,
                                      description="Each {} improves the accuracy of your thief reports.")
                   }
human_buildings = {'houses': Building(base_name='houses',
                                      class_name='house',
                                      total=25,
                                      production_cost=20,
                                      labour_maintenance=0,
                                      gold=50,
                                      wood=25,
                                      output=1,
                                      description='Each {} adds +{} to your birth rate.'),
                   'fields': Building(base_name='fields',
                                      class_name='wheat field',
                                      total=20,
                                      production_cost=20,
                                      labour_maintenance=5,
                                      gold=50,
                                      wood=10,
                                      output=25,
                                      description='Each {} provides enough grain for {} people a day.'),
                   'pastures': Building(base_name='pastures',
                                        class_name='dairy pasture',
                                        total=5,
                                        production_cost=20,
                                        labour_maintenance=15,
                                        gold=50,
                                        wood=10,
                                        output=30,
                                        description='Each {} can feed {} people a day, but excess milk is lost.'),
                   'mills': Building(base_name='mills',
                                     class_name='lumber mill',
                                     total=3,
                                     production_cost=25,
                                     labour_maintenance=15,
                                     gold=50,
                                     wood=25,
                                     output=3,
                                     description='Each {} produces {} wood a day.'),
                   'mines': Building(base_name='mines',
                                     class_name='iron mine',
                                     total=1,
                                     production_cost=35,
                                     labour_maintenance=15,
                                     gold=75,
                                     wood=15,
                                     output=3,
                                     description='Each {} produces {} iron a day.'),
                   'forts': Building(base_name='forts',
                                     class_name='palisade',
                                     total=0,
                                     production_cost=35,
                                     labour_maintenance=10,
                                     gold=75,
                                     wood=35,
                                     output=5,
                                     description='Each {} adds +{}% to your county\'s defence value.'),
                   'stables': Building(base_name='stables',
                                       class_name='stables',
                                       total=0,
                                       production_cost=45,
                                       labour_maintenance=5,
                                       gold=60,
                                       wood=25,
                                       output=6,
                                       description='Each {} lets your army return from battle {}% faster.'),
                   'guilds': Building(base_name='guilds',
                                      class_name='Thieves\' Guild',
                                      total=0,
                                      production_cost=45,
                                      labour_maintenance=10,
                                      gold=50,
                                      wood=25,
                                      output=5,
                                      description="Each {} improves the accuracy of your thief reports.")
                   }

all_armies = ["peasant", "archer", "soldier", "elite"]

dwarf_armies = {'peasant': Army(base_name='peasant',
                                class_name='miners',
                                total=35,
                                trainable_per_day=25,
                                gold=12,
                                iron=1,
                                wood=0,
                                upkeep=2,
                                attack=2,
                                defence=1,
                                health=2,
                                description='Miners deal extra damage when attacking.'),
                'soldier': Army(base_name='soldier',
                                class_name='axemen',
                                total=30,
                                trainable_per_day=15,
                                gold=15,
                                iron=3,
                                wood=2,
                                upkeep=4,
                                attack=3,
                                defence=2,
                                health=3,
                                description='Axemen are well-rounded soldiers.'),
                'archer': Army(base_name='archer',
                               class_name='crossbowmen',
                               total=25,
                               trainable_per_day=15,
                               gold=15,
                               iron=2,
                               wood=2,
                               upkeep=4,
                               attack=2,
                               defence=3,
                               health=3,
                               description='Crossbowmen can be trained more quickly than other archers.'),
                'elite': Army(base_name='elite',
                              class_name='greybeards',
                              total=0,
                              trainable_per_day=5,
                              gold=25,
                              iron=10,
                              wood=5,
                              upkeep=10,
                              attack=6,
                              defence=5,
                              health=5,
                              description='Greybeards are capable of defending, as well as attacking.')
                }

human_armies = {'peasant': Army(base_name='peasant',
                                class_name='men-at-arms',
                                total=40,
                                trainable_per_day=50,
                                gold=10,
                                iron=0,
                                wood=2,
                                upkeep=2,
                                attack=1,
                                defence=1,
                                health=1,
                                description='Men-at-arms can be trained extremely quickly.'),
                'soldier': Army(base_name='soldier',
                                class_name='footmen',
                                total=15,
                                trainable_per_day=15,
                                gold=15,
                                iron=3,
                                wood=2,
                                upkeep=4,
                                attack=3,
                                defence=2,
                                health=2,
                                description='Footmen are strong attackers.'),
                'archer': Army(base_name='archer',
                               class_name='bowmen',
                               total=35,
                               trainable_per_day=15,
                               gold=15,
                               iron=2,
                               wood=3,
                               upkeep=4,
                               attack=1,
                               defence=4,
                               health=2,
                               description='Bowmen are great at defending.'),
                'elite': Army(base_name='elite',
                              class_name='knights',
                              total=0,
                              trainable_per_day=5,
                              gold=30,
                              iron=15,
                              wood=2,
                              upkeep=10,
                              attack=8,
                              defence=2,
                              health=7,
                              description='Knights are one of the best attackers.')
                }

game_descriptions = {"attack": "How much power a unit has when attacking another county.",
                     "defence": "How much power a unit has when defending your county.",
                     "health": "Health affects how many of your units die in battle.",
                     "available_workers": "Any citizen not in the military or employed, is available. These workers "
                                          "will add production to your city which can be used to build new buildings. "
                                          "Unused production generates gold.",
                     "upkeep": "Monthly cost of paying your soldiers' salaries.",
                     "upkeep_daily": "Today's expected salary cost."}
