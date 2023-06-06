from datos_validator import validate_data

class Datos:

    def __init__(self, peso):
        validate_data(peso)
        self.peso = peso

    def to_db_collection(self):
        return {
            'peso': self.peso,
        }