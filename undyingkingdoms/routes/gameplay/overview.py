from datetime import datetime

from flask import render_template, url_for, redirect
from flask_login import login_required, current_user

from undyingkingdoms import app
from undyingkingdoms.models import World, County, Kingdom, User
from undyingkingdoms.models.forms.attack import TempGameAdvance


@app.route('/gameplay/overview/<int:kingdom_id>/<int:county_id>/', methods=['GET', 'POST'])
@login_required
def overview(kingdom_id=0, county_id=0):
    for user in User.query.filter_by(_logged_in=True).all():
        time_since_last_activity = datetime.now() - user.time_modified
        if time_since_last_activity.total_seconds() > 300:  # A user who hasn't done anything in 5 minutes
            user.logged_in = False
    if not current_user.logged_in:
        current_user.logged_in = True
    if not current_user.county:
        return redirect(url_for('initialize'))

    kingdom = Kingdom.query.filter_by(id=kingdom_id).first()
    county = County.query.filter_by(id=county_id).first()
    # Below is clock functions
    world = World.query.first()
    world.check_clock()
    form = TempGameAdvance()
    if form.validate_on_submit():
        world.advance_day()
        world.advance_24h_analytics()
    # End of clock functions
    return render_template('gameplay/overview.html', form=form, selected_kingdom=kingdom, selected_county=county)
