from undyingkingdoms.models.buildings import Building


generic_buildings = {'house': Building(base_name='house',
                                       class_name='house',
                                       class_name_plural='houses',
                                       total=25,
                                       production_cost=20,
                                       labour_maintenance=0,
                                       gold=35,
                                       wood=25,
                                       output=1,
                                       description='Each {} adds +{} to your birth rate.'),
                     'field': Building(base_name='field',
                                       class_name='grain field',
                                       class_name_plural='grain fields',
                                       total=20,
                                       production_cost=20,
                                       labour_maintenance=5,
                                       gold=35,
                                       wood=5,
                                       output=25,
                                       description='Each {} provides enough grain for {} people a day.'),
                     'pasture': Building(base_name='pasture',
                                         class_name='goat farm',
                                         class_name_plural='goat farms',
                                         total=5,
                                         production_cost=20,
                                         labour_maintenance=15,
                                         gold=35,
                                         wood=5,
                                         output=30,
                                         description='Each {} can feed {} people a day, but excess milk is lost.'),
                     'mill': Building(base_name='mill',
                                      class_name='lumber mill',
                                      class_name_plural='lumber mills',
                                      total=3,
                                      production_cost=25,
                                      labour_maintenance=15,
                                      gold=50,
                                      wood=20,
                                      output=3,
                                      description='Each {} produces {} wood a day.'),
                     'mine': Building(base_name='mine',
                                      class_name='iron mine',
                                      class_name_plural='iron mines',
                                      total=1,
                                      production_cost=35,
                                      labour_maintenance=15,
                                      gold=65,
                                      wood=15,
                                      output=3,
                                      description='Each {} produces {} iron a day.'),
                     'fort': Building(base_name='fort',
                                      class_name='stronghold',
                                      class_name_plural='strongholds',
                                      total=0,
                                      production_cost=50,
                                      labour_maintenance=25,
                                      gold=100,
                                      wood=75,
                                      output=6,
                                      description='Dwarf {}s are very effective and add +{}% to your county\'s defence value.'),
                     'stables': Building(base_name='stables',
                                         class_name='pony stables',
                                         class_name_plural='pony stables',
                                         total=0,
                                         production_cost=25,
                                         labour_maintenance=15,
                                         gold=40,
                                         wood=20,
                                         output=4,
                                         description='Each {} lets your army return from battle {}% faster.'),
                     'guild': Building(base_name='guild',
                                       class_name='thieves\' den',
                                       class_name_plural='thieves\' dens',
                                       total=0,
                                       production_cost=45,
                                       labour_maintenance=25,
                                       gold=65,
                                       wood=50,
                                       output=1,
                                       description="Each {} gives you {} additional spies to send on missions."),
                     'bank': Building(base_name='bank',
                                      class_name='vault',
                                      class_name_plural='vaults',
                                      total=0,
                                      production_cost=50,
                                      labour_maintenance=5,
                                      gold=75,
                                      wood=25,
                                      output=10,
                                      description="Each {} gives you {} additional gold per day.")
                     }

