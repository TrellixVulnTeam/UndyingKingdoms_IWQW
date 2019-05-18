from undyingkingdoms.models.counties.counties import County


def test_alchemy_technology_effects(ctx):
    county = County.query.filter_by(leader="Elthran").one()
    scientist = county.scientist

    research_change = scientist.research_change
    assert scientist.research_change == research_change

    tech = county.technologies['basic alchemy']
    tech.completed = True

    expected_change = 0
    # I should add this code to effects class?
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


