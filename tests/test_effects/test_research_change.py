from undyingkingdoms.models.counties.counties import County


def test_alchemy_technology_effects(ctx):
    county = County.query.filter_by(leader="Elthran").one()

    # A county with no labs should get 0 research a turn
    county.buildings['lab'].total = 0
    assert county.scientist.research_change == 0

    # A county with one lab should get the lab output of research a turn
    county.buildings['lab'].total = 1
    assert county.scientist.research_change == county.buildings['lab'].output

    scientist = county.scientist
    research_change = scientist.research_change

    # Now that the county has alchemy, it should add the alchemy value
    tech = county.technologies['basic alchemy']
    tech.completed = True
    expected_change = 0
    for effect in tech.effects:
        expected_change += effect.kwargs.get('research_change', 0)

    assert scientist.research_change > research_change
    assert scientist.research_change == research_change + expected_change

    #
    # assert county.research_change == 0
    #
    # county.technologies['basic alchemy'].completed = True
    #
    # assert county.research_change == 10
    #
    # county.technologies['basic alchemy ii'].completed = True
    #
    # assert county.research_change == 20
    #
    # county.technologies['basic alchemy ii'].completed = False
    # county.technologies['basic alchemy'].completed = False
    #
    # assert county.research_change == 0


