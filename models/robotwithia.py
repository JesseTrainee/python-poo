from models.robot import Robot

class RobotWithIA(Robot):
    """
    Classe que representa um robô com IA
    Atributos:
    - name: nome do robô.
    - year: ano de criação.
    - value: valor estimado.
    - _has_ai: estado de IA
    """
    def __init__(self, name, year, value, ia_features):
        super().__init__(name, year, value)
        self.ia_features = ia_features
        self._has_ai = False

    def __str__(self):
                return f'Name: {self.name.ljust(25)}, Year: {self.year}, Value: R${self.value}, Has AI: {self.has_ai}, Features: {self.ia_features}'

    @property
    def has_ai(self):
        return 'Habilitado' if self._has_ai else 'Desabilitado'

    @classmethod
    def switch_ia_status(self):
        self.has_ai = not self.has_ai