from datetime import datetime, timedelta
from random import randint

from flask import redirect, url_for, render_template
from flask_login import login_required, current_user
from flask_mobility.decorators import mobile_template
from sqlalchemy import desc

from undyingkingdoms import app
from undyingkingdoms.models import Infiltration, County, Notification
from undyingkingdoms.models.forms.infiltrate import InfiltrateForm
from undyingkingdoms.static.metadata.metadata import infiltration_missions, infiltration_success_modifier


@app.route('/gameplay/infiltrate/<int:county_id>', methods=['GET', 'POST'])
@mobile_template('{mobile/}gameplay/infiltrate.html')
@login_required
def infiltrate(template, county_id):
    if not current_user.in_active_session:
        current_user.in_active_session = True
    if county_id == current_user.county.id:
        return redirect(url_for('overview', kingdom_id=0, county_id=0))

    target = County.query.filter_by(id=county_id).first()

    form = InfiltrateForm()
    form.county_id.data = current_user.county.id
    thieves = min(current_user.county.get_number_of_available_thieves(), 3)
    form.amount.choices = [(i + 1, i + 1) for i in range(thieves)]
    form.mission.choices = [(index, name) for index, name in enumerate(infiltration_missions)]

    if form.validate_on_submit():
        mission = infiltration_missions[form.mission.data]
        report = Infiltration(current_user.county.id, target.id, current_user.county.county_days_in_age,
                              current_user.county.kingdom.world.day,
                              mission, form.amount.data)
        report.save()

        chance_of_success = target.get_chance_to_be_successfully_infiltrated() + form.amount.data
        modifier = 1 + infiltration_success_modifier.get(current_user.county.race, ("", 0))[1] \
                   + infiltration_success_modifier.get(current_user.county.background, ("", 0))[1]
        chance_of_success *= modifier

        if chance_of_success >= randint(1, 100):
            report.success = True
            if mission == 'pilfer':
                gold_stolen = int(min(randint(12 * form.amount.data, 20 * form.amount.data) * 1.25, target.gold))
                target.gold -= gold_stolen
                current_user.county.gold += gold_stolen
                report.pilfer_amount = gold_stolen
                report.duration = randint(13, 15)
                notification = Notification(target.id,
                                            "Thieves raided our lands",
                                            "They stole {} gold from our coffers".format(gold_stolen),
                                            current_user.county.kingdom.world.day)
            elif mission == 'burn crops':
                crops_burned = min(target.buildings['field'].total, form.amount.data)
                target.buildings['field'].total -= crops_burned
                report.crops_burned = crops_burned
                report.duration = randint(19, 20)
                notification = Notification(target.id,
                                            "Thieves raided our lands",
                                            "They burned {} of our crops".format(crops_burned),
                                            current_user.county.kingdom.world.day)
            elif mission == 'sow distrust':
                happiness_lost = min(target.happiness, form.amount.data * 3)
                target.happiness -= happiness_lost
                report.distrust = happiness_lost
                report.duration = randint(17, 19)
                notification = Notification(target.id,
                                            "Thieves raided our lands",
                                            "They have caused some unrest in our kingdom",
                                            current_user.county.kingdom.world.day)
            elif mission == 'scout military':
                report.get_troop_report(current_user.county, target, form.amount.data)
                report.duration = 6
                notification = Notification(target.id,
                                            "Thieves raided our lands",
                                            "They have found out some secrets regarding our military",
                                            current_user.county.kingdom.world.day)
        else:
            notification = Notification(target.id, "You caught enemy thieves from {}".format(current_user.county.name),
                                        "You caught them before they could accomplish their task",
                                        current_user.county.kingdom.world.day)
            report.duration = randint(20, 26)
            report.success = False
        notification.save()

        return redirect(url_for('infiltration'))

    return render_template(template, target=target, form=form)
