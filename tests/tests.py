import unittest
from entities.towers.base import AirTower, GroundTower, MultiTower
from entities.monsters.base import AirMonster, GroundMonster, MultiMonster


class TestDamageType(unittest.TestCase):
    def setUp(self) -> None:
        self.air_tower = AirTower()
        self.ground_tower = GroundTower()
        self.air_monster = AirMonster()
        self.ground_monster = GroundMonster()
        self.multi_monster = MultiMonster()
        self.multi_tower = MultiTower()

    def test_air_to_air(self):
        self.assertEqual(self.air_monster.damage_type == self.air_tower.damage_type, True)

    def test_air_to_ground(self):
        self.assertEqual(self.air_monster.damage_type == self.ground_tower.damage_type, False)

    def test_ground_to_ground(self):
        self.assertEqual(self.ground_monster.damage_type == self.ground_tower.damage_type, True)

    def test_ground_to_air(self):
        self.assertEqual(self.ground_monster.damage_type == self.air_tower.damage_type, False)

    def test_multi_to_air(self):
        self.assertEqual(self.multi_monster.damage_type == self.air_tower.damage_type, True)

    def test_multi_to_ground(self):
        self.assertEqual(self.multi_monster.damage_type == self.ground_tower.damage_type, True)

    def test_multi_to_multi(self):
        self.assertEqual(self.multi_monster.damage_type == self.multi_tower.damage_type, True)

    def test_air_to_multi(self):
        self.assertEqual(self.air_monster.damage_type == self.multi_tower.damage_type, True)

    def test_ground_to_multi(self):
        self.assertEqual(self.ground_monster.damage_type == self.multi_tower.damage_type, True)

    def test_wrong_inputs(self):
        self.assertEqual(self.air_monster.damage_type == self.air_monster, False)

    def test_wrong_inputs_again(self):
        self.assertEqual(self.multi_monster.damage_type == self.air_monster, False)


if __name__ == '__main__':
    unittest.main()
