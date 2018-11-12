from undyingkingdoms.models.buildings import Building
from undyingkingdoms.models.armies import Army

kingdom_names = ["Elthrania", "Galbador", "Faenoth"]

# (name, amount, maintenance, description)
all_buildings = ['houses', 'fields', 'mills', 'mines']

dwarf_buildings = {'houses': Building(base='houses',
                                      name='cottage',
                                      amount=25,
                                      production=20,
                                      labour=0,
                                      gold=25,
                                      wood=25,
                                      description='Each cottage adds +1 to your birth rate.'),
                   'fields': Building(base='fields',
                                      name='grain field',
                                      amount=20,
                                      production=20,
                                      labour=15,
                                      gold=25,
                                      wood=0,
                                      description='Each field adds +10 to your food production.'),
                   'mills': Building(base='mills',
                                     name='lumber mill',
                                     amount=5,
                                     production=25,
                                     labour=20,
                                     gold=25,
                                     wood=25,
                                     description='Each mill produces 1 wood a day.'),
                   'mines': Building(base='mines',
                                     name='iron mine',
                                     amount=1,
                                     production=35,
                                     labour=25,
                                     gold=50,
                                     wood=10,
                                     description='Each mine produces 1 iron a day.')
                   }

human_buildings = {'houses': Building(base='houses',
                                      name='house',
                                      amount=25,
                                      production=20,
                                      labour=0,
                                      gold=25,
                                      wood=25,
                                      description='Each house adds +1 to your birth rate.'),
                   'fields': Building(base='fields',
                                      name='wheat field',
                                      amount=20,
                                      production=20,
                                      labour=15,
                                      gold=25,
                                      wood=0,
                                      description='Each field adds +10 to your food production.'),
                   'mills': Building(base='mills',
                                     name='lumber mill',
                                     amount=5,
                                     production=25,
                                     labour=20,
                                     gold=25,
                                     wood=25,
                                     description='Each mill produces 1 wood a day.'),
                   'mines': Building(base='mines',
                                     name='iron mine',
                                     amount=1,
                                     production=35,
                                     labour=25,
                                     gold=50,
                                     wood=10,
                                     description='Each mine produces 1 iron a day.')
                   }

# (name, amount, attack, defence, health)
all_armies = ["peasant", "archer", "soldier", "elite"]

dwarf_armies = {'peasant': Army(base='peasant',
                                name='miners',
                                amount=100,
                                training=25,
                                gold=1,
                                iron=1,
                                wood=1,
                                attack=2,
                                defence=1,
                                health=2,
                                description='Miners deal extra damage.'),
                'soldier': Army(base='soldier',
                                name='axemen',
                                amount=15,
                                training=10,
                                gold=3,
                                iron=1,
                                wood=1,
                                attack=2,
                                defence=2,
                                health=3,
                                description='Axemen are well-rounded soldiers.'),
                'archer': Army(base='archer',
                               name='crossbowmen',
                               amount=15,
                               training=15,
                               gold=3,
                               iron=1,
                               wood=1,
                               attack=1,
                               defence=3,
                               health=3,
                               description='Crossbowmen can be trained more quickly than other archers.'),
                'elite': Army(base='elite',
                              name='greybeards',
                              amount=0,
                              training=5,
                              gold=10,
                              iron=2,
                              wood=1,
                              attack=6,
                              defence=5,
                              health=5,
                              description='Greybeards are capable of defending, as well as attacking.')
                }

human_armies = {'peasant': Army(base='peasant',
                                name='men-at-arms',
                                amount=100,
                                training=50,
                                gold=1,
                                iron=0,
                                wood=1,
                                attack=1,
                                defence=1,
                                health=1,
                                description='Men-at-arms can be trained extremely quickly.'),
                'soldier': Army(base='soldier',
                                name='footmen',
                                amount=15,
                                training=10,
                                gold=4,
                                iron=2,
                                wood=0,
                                attack=3,
                                defence=2,
                                health=2,
                                description='Footmen are strong attackers.'),
                'archer': Army(base='archer',
                               name='bowmen',
                               amount=15,
                               training=10,
                               gold=2,
                               iron=0,
                               wood=3,
                               attack=1,
                               defence=3,
                               health=2,
                               description='Bowmen are great at defending.'),
                'elite': Army(base='elite',
                              name='knights',
                              amount=0,
                              training=5,
                              gold=15,
                              iron=5,
                              wood=1,
                              attack=8,
                              defence=3,
                              health=7,
                              description='Knights are one of the best attackers.')
                }
