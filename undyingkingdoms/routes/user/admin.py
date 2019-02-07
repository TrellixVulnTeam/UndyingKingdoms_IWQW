from random import randint, choice
from uuid import uuid4

from flask import render_template, url_for
from flask_login import login_required, current_user
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import SubmitField

from undyingkingdoms import app, db
from undyingkingdoms.models.kingdoms import Kingdom
from undyingkingdoms.models.counties import County
from undyingkingdoms.models.users import User
from undyingkingdoms.routes.helpers import in_active_session, admin_required


class AdminForm(FlaskForm):
    submit = SubmitField('Do this')


bot_county_prefix = ["Eldritch", "Dengmar", "Zort", "Pralde", "Eggroth", "Wuanlo", "Ildar", "Endo", "Vil", "Gong", "Fili"]
bot_county_suffix = ["ville", " Town", "ion", "oth", " Land", "don", "min", " Vale"]

bot_leader_prefix = ["Skri", "Aldar", "Frel", "Eldr", "Toth", "Zon", "Pandish", "Gresk", "Linsk"]
bot_leader_suffix = ["oth", "ith", "ion", "ilisk", "anth", "ills", "ondo", "alasl"]


@app.route('/user/admin/', methods=['GET', 'POST'])
@login_required
@in_active_session
@admin_required
def admin():
    bot_form = AdminForm()
    kingdoms = Kingdom.query.all()
    if bot_form.validate_on_submit():
        for i in range(3):
            smallest_kingdom = min(kingdoms, key=lambda x: len(x.counties))
            bot_name = uuid4()
            user = User("bot_{}".format(bot_name), "bot_{}@gmail.com".format(bot_name), "1234")
            user.is_bot = True
            user.save()
            county = County(smallest_kingdom.id, "{}{}".format(choice(bot_county_prefix), choice(bot_county_suffix)),
                            "{}{}".format(choice(bot_leader_prefix), choice(bot_leader_suffix)), user.id,
                            choice(["Human", "Elf", "Dwarf"]), choice(["Sir", "Lady"]),
                            choice(["Engineer", "Warlord", "Rogue", "Merchant"]))
            county.save()
            county.vote = county.id
    return render_template('user/admin.html', form=bot_form)
