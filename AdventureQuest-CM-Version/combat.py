import random
from save_load import wrapped_text, wrapped_text_prompt
from character import Character
from exceptions import *

class Combat:
    def __init__(self, enemy_name: str, enemy_health: int, enemy_strength: int, rewards) -> None:
        self.enemy_name = enemy_name
        self.enemy_health = enemy_health
        self.enemy_strength = enemy_strength
        self.rewards = rewards
        self.is_defending: bool = False

    def player_attack(self, character: Character):
        """
        Calculates damage dealt by the player.
        """
        attack_damage: int = character.strength + random.randint(1, 5)
        wrapped_text(f"You attack the {self.enemy_name} for {attack_damage} damage!")
        self.enemy_health -= attack_damage

    def enemy_attack(self, character: Character):
        """
        Calculate damage dealt by enemy.
        """
        base_attack_damage: int = self.enemy_strength + random.randint(0,4)
        attack_damage: int = base_attack_damage // 2 if self.is_defending else base_attack_damage
        wrapped_text(f"{self.enemy_name} attacks you for {attack_damage} damage!")
        character.health -= attack_damage
        self.is_defending: bool = False

        if character.health <= 0:
            raise GameOverError(f"You have died from your mortal wounds inflicted by the {self.enemy_name}...")
    
    def run(self, character: Character):
        """
        Calculate chance of escaping successfully (without receiving damage).
        """
        chance_of_success: bool = random.random() < 0.5
        potential_damage: int = 0
        if chance_of_success:
            return chance_of_success, potential_damage
        else:
            potential_damage: int = random.randint(1, self.enemy_strength)
            character.health -= potential_damage
            return chance_of_success, potential_damage

    def engage(self, character: Character):
        """
        Simulate combat with player; can attack, defend or run. The enemy will attack after turn.
        """
        wrapped_text(f"{self.enemy_name} has appeared! Prepare for combat!")
        wrapped_text(f"[Combat Starts]")
        wrapped_text(f"Creature: {self.enemy_name} | Health: {self.enemy_health}")
        
        while self.enemy_health > 0 and character.health > 0:
            try:
                wrapped_text(f"What will you do?")
                action: str = wrapped_text_prompt(f"[Options: attack, defend, flee]", ": ").strip().lower()
                if action == "attack":
                    self.player_attack(character)
                    if self.enemy_health <= 0:
                        wrapped_text(f"You defeated the {self.enemy_name}! You emerge victorious!")
                        character.add_to_inventory(**self.rewards)
                        break
                    else:
                        self.enemy_attack(character)
                elif action == "defend":
                    self.is_defending = True
                    wrapped_text(f"You brace for the next enemy attack!")
                    self.enemy_attack(character)
                elif action == "run":
                    chance_of_success, damage = self.run(character)
                    if chance_of_success:
                        wrapped_text(f"You escaped unharmed! You live to fight another day!")
                        break
                    else:
                        wrapped_text(f"In your attempt to escape, the {self.enemy_name} struck you for {damage} damage!")
                else:
                    raise InvalidActionError("Invalid combat command. Use 'attack', 'defend' or 'run'")
            
                if character.health <= 0:
                    raise GameOverError("You have fallen in combat. Your journey ends here...")
                    
            except InvalidActionError as e:
                wrapped_text(str(e))
                continue