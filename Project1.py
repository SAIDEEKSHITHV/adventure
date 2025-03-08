name = input("hey type your name: ")
print("Hello "+ name + " welcome to the game!" )

should_we_play = input("Do you want to play? ").lower()

if should_we_play == "y" or should_we_play == "yes":
    print("we are playing")
    
    direction = input("Do you want to go right or left? (right/left) ").lower()
    if direction == "right":
        choice = input("Okay, now you see a bridge, do you want to swim under it or cross it? (swim/cross) ")
        if choice == "swim":
            print("You got eaten by a Shark, you die, The End!")
        elif choice == "cross":
            print("You Have successfully crossed the bridge")
            second_direction = input("You have crossed, Do you want to take (right/left) ").lower()
            if second_direction == "right":
                print("You have entered the final stage")
                final_stage = input("Now you see two doors, which one do you want to choose (one/two) ").lower()
                if final_stage == "one":
                    print("You are safe but, No GOLD, better luck next time")
                elif final_stage == "two":
                    print("Congrats! You Won The GOLD!")
                else:
                    print("Wrong choice, you die!")
            else:
                print("Sorry wrong turn, You have eaten by Devil!")
        else:
            print("Sorry not valid reply, you die!")
    elif direction == "left":
        print("you went left and fell of a cliff, game over, try again.")
    else:
        print("Sorry not valid reply, you die!")
else:
    print("we are not playing...")
    