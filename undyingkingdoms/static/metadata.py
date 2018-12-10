from undyingkingdoms.models.achievements import Achievement
from undyingkingdoms.models.buildings import Building
from undyingkingdoms.models.armies import Army

kingdom_names = ["Faenoth"]

all_achievements = {
    'land': Achievement(category_name="land",
                        description="Have your county reach x amount of land in one playthrough.",
                        tier1=200, tier2=250, tier3=300, tier4=350, tier5=500, maximum_tier=5,
                        points_rewarded=5,
                        land=True),
    'population': Achievement(category_name="population",
                              description="Have your county reach x population in one playthrough.",
                              tier1=525, tier2=550, tier3=800, tier4=900, tier5=1000, maximum_tier=5,
                              points_rewarded=5,
                              population=True),
    'gold': Achievement(category_name="gold",
                        description="Have your county reach x gold in one playthrough.",
                        tier1=1250, tier2=1500, tier3=None, tier4=None, tier5=None, maximum_tier=2,
                        points_rewarded=5,
                        gold=True),
    'wood': Achievement(category_name="wood",
                        description="Have your county reach x wood in one playthrough.",
                        tier1=100, tier2=200, tier3=None, tier4=None, tier5=None, maximum_tier=2,
                        points_rewarded=5,
                        wood=True),
    'iron': Achievement(category_name="iron",
                        description="Have your county reach x iron in one playthrough.",
                        tier1=50, tier2=100, tier3=None, tier4=None, tier5=None, maximum_tier=2,
                        points_rewarded=5,
                        iron=True),
    'happiness': Achievement(category_name="happiness",
                             description="Have your county reach x happiness in one playthrough.",
                             tier1=525, tier2=550, tier3=800, tier4=900, tier5=1000, maximum_tier=5,
                             points_rewarded=5,
                             happiness=True),
    'hunger': Achievement(category_name="hunger",
                          description="Have your county reach x hunger in one playthrough.",
                          tier1=525, tier2=550, tier3=800, tier4=900, tier5=1000, maximum_tier=5,
                          points_rewarded=5,
                          hunger=True)
}

rations_translations_tables = {"None": 0, "Quarter": 0.25, "Half": 0.5, "Normal": 1, "Double": 2, "Triple": 3}

all_buildings = ['houses', 'fields', 'pastures', 'mills', 'mines', 'forts']

dwarf_buildings = {'houses': Building(base_name='houses',
                                      class_name='cottage',
                                      total=25,
                                      production_cost=20,
                                      labour_maintenance=0,
                                      gold=25,
                                      wood=25,
                                      description='Each cottage adds +1 to your birth rate.'),
                   'fields': Building(base_name='fields',
                                      class_name='grain field',
                                      total=15,
                                      production_cost=20,
                                      labour_maintenance=10,
                                      gold=25,
                                      wood=0,
                                      description='Each field adds 20 to your food production.'),
                   'pastures': Building(base_name='pastures',
                                        class_name='dwarf cow farm',
                                        total=10,
                                        production_cost=20,
                                        labour_maintenance=10,
                                        gold=25,
                                        wood=0,
                                        description='Adds 25 to your food production, but excess milk can not be'
                                                    ' stored and is lost.'),
                   'mills': Building(base_name='mills',
                                     class_name='lumber mill',
                                     total=5,
                                     production_cost=25,
                                     labour_maintenance=15,
                                     gold=25,
                                     wood=25,
                                     description='Each mill produces 1 wood a day.'),
                   'mines': Building(base_name='mines',
                                     class_name='iron mine',
                                     total=0,
                                     production_cost=35,
                                     labour_maintenance=20,
                                     gold=50,
                                     wood=10,
                                     description='Each mine produces 1 iron a day.'),
                   'forts': Building(base_name='forts',
                                     class_name='stronghold',
                                     total=0,
                                     production_cost=35,
                                     labour_maintenance=20,
                                     gold=50,
                                     wood=10,
                                     description='Adds +1% to your county\'s defence value.')
                   }

human_buildings = {'houses': Building(base_name='houses',
                                      class_name='house',
                                      total=25,
                                      production_cost=20,
                                      labour_maintenance=0,
                                      gold=25,
                                      wood=25,
                                      description='Each house adds +1 to your birth rate.'),
                   'fields': Building(base_name='fields',
                                      class_name='wheat field',
                                      total=15,
                                      production_cost=20,
                                      labour_maintenance=10,
                                      gold=25,
                                      wood=0,
                                      description='Each field adds 20 to your food production.'),
                   'pastures': Building(base_name='pastures',
                                        class_name='dairy pasture',
                                        total=10,
                                        production_cost=20,
                                        labour_maintenance=10,
                                        gold=25,
                                        wood=0,
                                        description='Adds 25 to your food production, but excess milk can not be'
                                                    ' stored and is lost.'),
                   'mills': Building(base_name='mills',
                                     class_name='lumber mill',
                                     total=5,
                                     production_cost=25,
                                     labour_maintenance=15,
                                     gold=25,
                                     wood=25,
                                     description='Each mill produces 1 wood a day.'),
                   'mines': Building(base_name='mines',
                                     class_name='iron mine',
                                     total=1,
                                     production_cost=35,
                                     labour_maintenance=20,
                                     gold=50,
                                     wood=10,
                                     description='Each mine produces 1 iron a day.'),
                   'forts': Building(base_name='forts',
                                     class_name='palisade',
                                     total=0,
                                     production_cost=35,
                                     labour_maintenance=20,
                                     gold=50,
                                     wood=10,
                                     description='Each fort adds +1% to your county\'s defence value.')
                   }

all_armies = ["peasant", "archer", "soldier", "elite"]

dwarf_armies = {'peasant': Army(base_name='peasant',
                                class_name='miners',
                                total=100,
                                trainable_per_day=25,
                                gold=1,
                                iron=1,
                                wood=1,
                                attack=2,
                                defence=1,
                                health=2,
                                description='Miners deal extra damage.'),
                'soldier': Army(base_name='soldier',
                                class_name='axemen',
                                total=15,
                                trainable_per_day=10,
                                gold=3,
                                iron=1,
                                wood=1,
                                attack=2,
                                defence=2,
                                health=3,
                                description='Axemen are well-rounded soldiers.'),
                'archer': Army(base_name='archer',
                               class_name='crossbowmen',
                               total=15,
                               trainable_per_day=15,
                               gold=3,
                               iron=1,
                               wood=1,
                               attack=1,
                               defence=3,
                               health=3,
                               description='Crossbowmen can be trained more quickly than other archers.'),
                'elite': Army(base_name='elite',
                              class_name='greybeards',
                              total=0,
                              trainable_per_day=5,
                              gold=10,
                              iron=2,
                              wood=1,
                              attack=6,
                              defence=5,
                              health=5,
                              description='Greybeards are capable of defending, as well as attacking.')
                }

human_armies = {'peasant': Army(base_name='peasant',
                                class_name='men-at-arms',
                                total=100,
                                trainable_per_day=50,
                                gold=1,
                                iron=0,
                                wood=1,
                                attack=1,
                                defence=1,
                                health=1,
                                description='Men-at-arms can be trained extremely quickly.'),
                'soldier': Army(base_name='soldier',
                                class_name='footmen',
                                total=15,
                                trainable_per_day=10,
                                gold=4,
                                iron=2,
                                wood=0,
                                attack=3,
                                defence=2,
                                health=2,
                                description='Footmen are strong attackers.'),
                'archer': Army(base_name='archer',
                               class_name='bowmen',
                               total=15,
                               trainable_per_day=10,
                               gold=2,
                               iron=0,
                               wood=3,
                               attack=1,
                               defence=3,
                               health=2,
                               description='Bowmen are great at defending.'),
                'elite': Army(base_name='elite',
                              class_name='knights',
                              total=0,
                              trainable_per_day=5,
                              gold=15,
                              iron=5,
                              wood=1,
                              attack=8,
                              defence=3,
                              health=7,
                              description='Knights are one of the best attackers.')
                }
