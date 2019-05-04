from copy import deepcopy

from tests import bp
from undyingkingdoms.models.technologies import Technology
from utilities.helpers import romanize

generic_technology = [
    Technology(
        name='Agriculture',
        cost=500,
        max_level=2,
        description="+{output:0.0%} bonus to all grain production within your county.",
        output=0.25
    ),
    Technology(
        name='Animal Husbandry',
        cost=500,
        max_level=1,
        description='+50% bonus to all dairy production within your county.',
    ),
    Technology(
        name='Steel',
        cost=1000,
        max_level=1,
        description='+10% Attack Power bonus to all offensive invasions you perform.',
    ),
    Technology(
        name='Engineering',
        cost=250,
        max_level=1,
        description='+1 building can be built each day.',
    ),
    Technology(
        name='Logistics',
        cost=500,
        max_level=1,
        description='Your armies return from battle one day sooner.',
    ),
    Technology(
        name='Public Works',
        cost=1000,
        max_level=1,
        description='Your county generates an additional 1 happiness each day.',
    ),
    Technology(
        name='Arcane Knowledge',
        cost=500,
        max_level=3,
        description='Each level raises your maximum mana by {output:.0f}.',
        output=20,
    ),
]


def generate_tech_levels(techs, requirements):
    """Generate each level up tech up to max level.
    """
    all_techs = []
    all_reqs= {}
    for tech in techs:
        all_techs.append(tech)
        for level in range(1, tech.max_level):
            next_level_tech = deepcopy(tech)
            next_level_tech.tier = tech.tier + level
            next_level_tech.name = romanize(tech.name, next_level_tech.tier)
            try:
                next_level_tech.output = tech.output * (level + 1)
            except TypeError:
                pass
            all_techs.append(next_level_tech)

            # merge custom and generated requirements
            try:
                all_reqs[next_level_tech.key] = set(requirements[next_level_tech.key]) | {all_techs[-2].key}
            except KeyError:
                all_reqs[next_level_tech.key] = {all_techs[-2].key}

    return {
        tech.key: tech
        for tech in all_techs
    }, all_reqs


custom_requirements = {
    'public works': ['engineering']
}

generic_technology, generic_requirements = generate_tech_levels(generic_technology, custom_requirements)

# for tech in generic_technology.values():
#     print(tech.description)


# randomly generated by fake.requirements() as an example
"""
generic_requirements = {
    'agriculture II': ['public works III'],
    'agriculture IV': ['logistics IV', 'engineering IV'],
    'animal husbandry I': ['logistics I'],
    'animal husbandry II': ['logistics II'],
    'animal husbandry III': ['logistics III'],
    'arcane knowledge I': ['logistics I', 'engineering I'],
    'engineering I': ['logistics I'],
    'engineering II': ['steel II'],
    'engineering IV': ['public works IV'],
    'logistics I': ['animal husbandry I'],
    'logistics II': ['agriculture II'],
    'logistics III': ['animal husbandry III', 'public works III'],
    'logistics IV': ['engineering IV', 'arcane knowledge IV'],
    'logistics V': ['public works V', 'steel V'],
    'public works': ['arcane knowledge'],
    'public works III': ['agriculture III', 'logistics III'],
    'public works IV': ['animal husbandry IV'],
    'public works V': ['logistics V'],
    'steel': ['engineering'],
    'steel II': ['animal husbandry II', 'logistics II'],
    'steel III': ['public works III', 'animal husbandry III']
}
"""
