class Explosive:

    def __init__(self, blast_radius, era, explosive_type, dud=False):
        self.blast_radius = blast_radius
        self.era = era
        self.explosive_type = explosive_type
        self.has_exploded = False
        self.dud = dud

    def explode(self):
        if not self.dud:
            self.has_exploded = True
            print(f'The {self.explosive_type} exploded with a blast radius of {self.blast_radius}.')
        else:
            print('It was a dud.')


class Missile(Explosive):

    def __init__(self, blast_radius, era, missile_shape, payload_type, dud=False):
        super().__init__(blast_radius, era, explosive_type='missile', dud=dud)
        self.missile_shape = missile_shape
        self.payload = Payload(payload_type)

    def launch(self, target):
        print(f'The {self.missile_shape} missile was launched at {target}.')
        super().explode()
        if self.payload.fallout:
            print('The nuclear fallout has rendered the target area uninhabitable' +
                  'for hundreds of years.')

    def explode(self):
        if not self.dud:
            self.has_exploded = True
            print(f'The missile exploded at the launch site '
                  f'with a blast radius of {self.blast_radius}.')
        else:
            print('Good thing it was a dude or it would have exploded the launch site.')


class Payload:

    def __init__(self, payload_type):
        self.type = payload_type
        if self.type.lower() == 'nuclear':
            self.volatility = 'high'
            self.fallout = True
        else:
            self.volatility = 'low'
            self.fallout = False
