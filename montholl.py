
import random

def monty_hall(simulations=1000):
    switch_win = 0
    stay_win = 0
    for _ in range(simulations):
        # Place a car behind one of the doors (either 0, 1, or 2)
        car_position = random.randint(0, 2)
        # Participant makes a choice
        choice = random.randint(0, 2)
        # Host opens a door that neither contains the car nor the participant's choice
        open_door = next(i for i in range(3) if i != choice and i != car_position)
        # Participant switches their choice
        switch_choice = next(i for i in range(3) if i != choice and i != open_door)
        # Record the results
        if switch_choice == car_position:
            switch_win += 1
        if choice == car_position:
            stay_win += 1

    print(f"Winning by switching: {switch_win} times ({switch_win/simulations*100:.2f}%)")
    print(f"Winning by staying: {stay_win} times ({stay_win/simulations*100:.2f}%)")

# Run the simulation
monty_hall(1000)
