from game_messages import Message


class BasicMonster:
    def take_turn(self, target, game_map, entities):
        results = []
        monster = self.owner

        if game_map.fov[monster.x, monster.y]:
            if monster.distance_to(target) >= 2:
                monster.move_towards(target.x, target.y, game_map, entities)

            elif target.fighter.hp > 0:
                attack_results = monster.fighter.attack(target)
                results.extend(attack_results)

        return results


class BasicNPC:
    def take_turn(self, target, game_map, entities):
        results = []
        npc = self.owner

        if npc.distance_to(target) == 1:
            results.append({'message': Message('Hello {0}.'.format(target.name))})

        return results
