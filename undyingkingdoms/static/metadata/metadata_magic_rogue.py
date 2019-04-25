from undyingkingdoms.models.magic import Magic

rogue_spells = {
    'modify_thief_prevention': Magic(name='modify_thief_prevention',
                                     display_name='Shroud of Night',
                                     source='Rogue',
                                     category='timed',
                                     targets='hostile',
                                     known=True,
                                     mana_cost=25,
                                     duration=6,
                                     output=-50,
                                     description='Shrouds the enemy land in darkness, '
                                                 'greatly reducing their chance to catch thieves.'),
    'modify_death_rate': Magic(
        name='modify_death_rate',
        display_name='Poisoned Wells',
        category='timed',
        targets='hostile',
        known=True,
        mana_cost=30,
        duration=12,
        output=0.5,
        description='Poisons an enemy county for 12 days. '
                    'While poisoned, their people die 50% more quickly.'
    ),
}
