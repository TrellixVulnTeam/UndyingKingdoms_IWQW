from undyingkingdoms.models.researches import Research

generic_armies = {'peasant': Army(name='peasant',
                                  class_name='peasant',
                                  class_name_plural='peasants',
                                  total=25,
                                  trainable_per_day=25,
                                  gold=5,
                                  iron=2,
                                  wood=1,
                                  upkeep=5,
                                  attack=1,
                                  defence=1,
                                  health=1,
                                  description='Unknown'),
                  'soldier': Army(name='soldier',
                                  class_name='soldier',
                                  class_name_plural='soldiers',
                                  total=0,
                                  trainable_per_day=15,
                                  gold=15,
                                  iron=6,
                                  wood=3,
                                  upkeep=15,
                                  attack=3,
                                  defence=1,
                                  health=3,
                                  description='Unknown'),
                  'archer': Army(name='archer',
                                 class_name='archer',
                                 class_name_plural='archers',
                                 total=30,
                                 trainable_per_day=10,
                                 gold=20,
                                 iron=8,
                                 wood=4,
                                 upkeep=15,
                                 attack=0,
                                 defence=5,
                                 health=3,
                                 description='Unknown'),
                  'elite': Army(name='elite',
                                class_name='elite',
                                class_name_plural='elites',
                                total=0,
                                trainable_per_day=5,
                                gold=40,
                                iron=15,
                                wood=6,
                                upkeep=25,
                                attack=8,
                                defence=5,
                                health=6,
                                description='Unknown'),
                  'monster': Army(name='monster',
                                  class_name='monster',
                                  class_name_plural='monsters',
                                  total=0,
                                  trainable_per_day=1,
                                  gold=250,
                                  iron=75,
                                  wood=50,
                                  upkeep=100,
                                  attack=50,
                                  defence=50,
                                  health=25,
                                  description='Unknown')
                  }
