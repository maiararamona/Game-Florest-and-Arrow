
from code.background import Background
from code.enemy import Enemy
from code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'floresta1':
                return [
                    Background('floresta1', (0, 0), 0.5),
                    Background('floresta2', (0, 0), 1.0),
                    Background('floresta3', (0, 0), 1.5),
                    Background('floresta4', (0, 0), 2.0),
                    Background('floresta5', (0, 0), 2.5),
                    Background('floresta6', (0, 0), 3.0),
                    Background('floresta7', (0, 0), 3.5),
                ]
            case '0_Forest_Ranger_passo1':
                return Player('0_Forest_Ranger_passo1', position )
            case '0_Orc_passo1':
                return Enemy(position)
