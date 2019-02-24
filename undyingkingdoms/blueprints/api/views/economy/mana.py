from flask import jsonify
from flask.views import MethodView
from flask_login import login_required, current_user


class ManaAPI(MethodView):
    @login_required
    def get(self):
        county = current_user.county

        return jsonify(
            status='success',
            message='You called the mana api.',
            manaAmount=county.mana,
            manaIncome=county.get_mana_change(),
        )
