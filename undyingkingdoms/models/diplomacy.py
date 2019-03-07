from undyingkingdoms.models.bases import GameEvent, db


class Diplomacy(GameEvent):

    kingdom_id = db.Column(db.Integer, db.ForeignKey('kingdom.id'), nullable=False)
    target_id = db.Column(db.Integer, db.ForeignKey('kingdom.id'), nullable=False)
    world_day = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    status = db.Column(db.String(16))
    action = db.Column(db.String(16))

    # War
    attacker_current = db.Column(db.Integer)
    defender_current = db.Column(db.Integer)
    attacker_goal = db.Column(db.Integer)
    defender_goal = db.Column(db.Integer)

    kingdom = db.relationship('Kingdom', foreign_keys=[kingdom_id])
    target_kingdom = db.relationship('Kingdom', foreign_keys=[target_id])

    def __init__(self, kingdom_id, target_id, world_day, duration=None, action="Unknown", status="Pending"):

        self.kingdom_id = kingdom_id
        self.target_id = target_id
        self.world_day = world_day
        self.duration = duration

        self.action = action
        self.status = status

        self.attacker_current = 0
        self.defender_current = 0
        self.attacker_goal = 0
        self.defender_goal = 0

    def get_other_kingdom(self, kingdom):
        return self.target_kingdom if self.target_id != kingdom.id else self.kingdom
