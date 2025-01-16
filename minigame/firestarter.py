from time import time, sleep
from ui.input import enter_press, wait_for_continue
from ui.output import colored, gradient, SlowPrinter, key, clear
from os import system
import consts

def get_flame_color(heat: int | float) -> tuple[int, int, int]:
    """Gets the color that the prompt arrow should be, based on the inputted heat out of 255"""
    heat = int(heat)
    return (min(heat * 2, 255), min(heat, 255), 0)

def gameplay() -> int:
    """Controls the main gameplay. Returns the highest heat value the player reached."""
    heat = 0
    start = time()
    while time() - start < consts.cheating_threshold:
        input(colored('', *get_flame_color(heat)))
    
    # Tracks the highest temperature the player got
    highest_heat = 0
    
    while True:
        choice = enter_press(colored('. ', *get_flame_color(heat)))
        
        if choice == 'exit':
            break
        
        # Update time
        currtime = time()
        elapsed = currtime - start
        start = currtime
        
        # Update heat
        heat += 20 * (1 - (3 * elapsed))
        
        # Low-bound heat at 0
        if heat < 0:
            heat = 0
        
        # Update highest heat tracker
        highest_heat = max(highest_heat, heat)
        
        # If the time elapsed is less than the cheating threshhold, the player cheated.
        if elapsed < consts.cheating_threshold:
            return -1
        
        # If the heat is >255, you win.
        if highest_heat >= 255:
            break
        
    return highest_heat

def heat_to_celsius(heat: float) -> float:
    """Converts a heat value out of 255, to a temperature in Celsius"""
    return consts.heat_conversion * heat

def reward(player: "Player"):
    """Add a campfire the player's wilderness at their position"""
    area = player.wilderness[player.coordinates]
    area.add_feature('campfire')

def run(player: "Player") -> bool:
    """Run the firestarter minigame for a player, return a boolean value of if they made a fire or not"""
    clear()
    SlowPrinter.print(f"You make a primitive hand drill. \n"
                      f"To start a fire, rub the wood and stick together by repeatedly pressing the {key('Enter')} key.\n"
                      f"Be sure to do it quickly so that you can build up enough heat.\n"
                      f"You can also exit at any time by typing \"exit\".")
    highest_heat = gameplay()
    highest_temp = heat_to_celsius(highest_heat)
    
    if highest_heat >= 255:
        print(gradient('FWOOOOOOOOSH', 255, 128, 0, 255, 255, 0))
        sleep(1)
        SlowPrinter.print("You have successfully started a fire!\n\n")
        wait_for_continue()
        reward(player)
        return True
    elif highest_heat < 0:
        print(gradient('SNAP!', 128, 128, 64, 64, 64, 32))
        sleep(1)
        SlowPrinter.print("You rub the stick so quickly that you accidentally break it!\n"
                          "-1 stick.\n"
                          "(This is an anti-cheating measure. If you "
                          "got this message legitimately, hats off to you.)")
        # TODO: Player loses stick
        wait_for_continue()
    else:
        SlowPrinter.print("Your hand drill did not reach a high enough temperature this time, "
                "since it only reached a temperature of {:.2f}°C.".format(highest_temp))
    player.get_item('stick')
    player.get_item('wood')
    return False


if __name__ == '__main__':
    run()