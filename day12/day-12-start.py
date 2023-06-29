################### Scope ####################

# enemies = 1
#
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Local Scope
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
#
# drink_potion()
# print(potion_streng)

# Global Scope
# player_health = 10
#
#
# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(potion_strength)
#
#     drink_potion()
#
#
# print(player_health)
#
# # There is no Block Scope
# game_level = 3
#
#
# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]
#     print(new_enemy)


# Modifying Global Scope
# enemies = 1
#
#
# def increase_enemies():
#     print(f'Enemies inside function: {enemies}')
#     return enemies + 1
#
#
# increase_enemies()
# print(f'Enemies outside function: {enemies}')


# Global Constants
PI = 3.14159
URL = "https://www.google.com"

