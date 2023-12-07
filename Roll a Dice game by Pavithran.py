import random
import time

def roll_dice():
    return random.randint(1, 6)

def display_dice(dice_result):
    dice_faces = [
        "+-------+",
        "|       |",
        f"|   {dice_result}   |",
        "|       |",
        "+-------+"
    ]
    for line in dice_faces:
        print(line)

def use_lucky_charm():
    return random.randint(4, 6)  # Guarantees a roll between 4 and 6

def special_event():
    events = [
        "You found a hidden treasure! Gain 10 extra points!",
        "A mischievous leprechaun appears. Lose 5 points.",
        "You stumbled upon a shortcut. Skip the next turn!"
    ]
    event = random.choice(events)
    print(event)

def visit_shop(total_score):
    print("\nWelcome to the Shop!")
    print(f"You have {total_score} points to spend.")

    while True:
        print("\nShop Menu:")
        print("1. Lucky Charm (Cost: 5 points) - Guarantees a roll between 4 and 6.")
        print("2. Extra Turn (Cost: 10 points) - Earn an extra turn in the next round.")
        print("3. Quit Shop")

        choice = input("Enter your choice (1-3): ")

        if choice == '1' and total_score >= 5:
            total_score -= 5
            return use_lucky_charm()
        elif choice == '2' and total_score >= 10:
            total_score -= 10
            print("You purchased an extra turn!")
            return 0  # Returns 0 to indicate an extra turn
        elif choice == '3':
            print("Exiting the shop.")
            break
        else:
            print("Invalid choice or not enough points. Try again.")

def dynamic_weather_system():
    weather_conditions = ["Clear", "Rainy", "Stormy"]
    current_weather = random.choice(weather_conditions)
    print(f"\nCurrent weather: {current_weather}")

    if current_weather == "Rainy":
        print("The rain makes the dice slippery. Rolls are more unpredictable!")
        return 1  # Returns 1 to indicate modified dice rolls
    elif current_weather == "Stormy":
        print("A storm is brewing. Brace yourself for a challenging round!")
        return 2  # Returns 2 to indicate a more challenging round
    else:
        return 0  # Returns 0 for normal conditions

def main():
    print("Welcome to the Ultimate Dice Rolling Game!")

    total_score = 0
    max_turns = 5
    current_turn = 1
    leaderboard = []
    difficulty_level = 1  # Start with a basic difficulty level

    while current_turn <= max_turns:
        print(f"\nTurn {current_turn} - Total Score: {total_score} - Difficulty Level: {difficulty_level}")

        # Countdown timer for each turn
        for seconds in range(3, 0, -1):
            print(f"Rolling dice in {seconds} seconds...")
            time.sleep(1)

        input("Press Enter to roll the dice...")

        # Apply dynamic weather effects
        weather_modifier = dynamic_weather_system()

        # Check if the player has a lucky charm
        has_lucky_charm = input("Do you want to use your lucky charm? (yes/no): ").lower()
        if has_lucky_charm == 'yes':
            dice_result = use_lucky_charm()
            print("You used your lucky charm!")
        else:
            dice_result = roll_dice()

            # Apply weather modifier
            if weather_modifier == 1:
                print("The rain affects the dice roll!")
                dice_result = roll_dice()
            elif weather_modifier == 2:
                print("The storm makes the dice more challenging!")
                dice_result = roll_dice() + 1  # Increase difficulty by adding 1

        display_dice(dice_result)

        if dice_result == 1:
            print("Oh no! You rolled a 1. Your turn is over.")
        else:
            total_score += dice_result
            print(f"Total score: {total_score}")

            if dice_result == 6:
                print("Wow! You rolled a 6 and earned an extra turn!")

            # Check for special events
            if random.randint(1, 5) == 1:  # 20% chance of a special event
                special_event()

            double_or_nothing = input("Do you want to go double or nothing? (yes/no): ").lower()

            if double_or_nothing == 'yes':
                double_result = roll_dice()
                print(f"You rolled a {double_result} for double or nothing!")

                if double_result == 6:
                    print("Congratulations! You doubled your score!")
                    total_score *= 2
                else:
                    print("Oops! You lost it all!")
                    total_score = 0

        # Visit the shop
        if current_turn < max_turns:
            shop_choice = input("Do you want to visit the shop? (yes/no): ").lower()
            if shop_choice == 'yes':
                extra_turn = visit_shop(total_score)
                if extra_turn:
                    print("Enjoying your extra turn!")
                    current_turn -= 1  # Adjust turn count for the extra turn

        # Increase difficulty level with each turn
        difficulty_level += 1

        current_turn += 1

    print("\nGame Over!")
    print(f"Total Score: {total_score}")

    # Update leaderboard
    leaderboard.append(total_score)
    leaderboard.sort(reverse=True)

    print("\nLeaderboard:")
    for i, score in enumerate(leaderboard[:5], start=1):
        print(f"{i}. Score: {score}")

    if total_score >= 20:
        print("Congratulations! You've scored 20 or more. You win!")
    else:
        print("Better luck next time. You did not reach 20 points.")

if __name__ == "__main__":
    main()
