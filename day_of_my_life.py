"""Welcome to the most interesting day of my life!"""

import random
from collections import deque

class State:
    """States of the day."""
    WAKE_UP = 0
    EAT = 1
    STUDY = 2
    SLEEP = 3
    VIDEO_GAMES = 4
    WALK_WITH_FRIENDS = 5

class DayOfMyLife:
    """A day of my life."""
    HOURS_IN_A_DAY = deque(range(24))
    def __init__(self):
        self.state = State.SLEEP
        self.hour = DayOfMyLife.HOURS_IN_A_DAY.popleft()

    def run(self):
        """Main loop of the day."""
        print('Beginning of the day!')
        while self.HOURS_IN_A_DAY:
            if self.state == State.SLEEP:
                self.sleep()
            if self.state == State.WAKE_UP:
                self.wake_up()
            if self.state == State.EAT:
                self.eat()
            if self.state == State.STUDY:
                self.study()
            if self.state == State.VIDEO_GAMES:
                self.video_games()
            if self.state == State.WALK_WITH_FRIENDS:
                self.walk_with_friends()
        print('11:00 pm - Time to sleep! Bye!')

    def sleep(self):
        """I'm sleeping!"""
        if self.hour in range(0, 7):
            random_sleep = random.choice([0, 0, 0, 0, 0, 0, 1, 2]) ###
            if random_sleep == 0:
                print(f"{str(self.hour) + ':00 am'} - I'm sleeping!")
                self.hour = DayOfMyLife.HOURS_IN_A_DAY.popleft()
            elif random_sleep == 1:
                print(f"{str(self.hour) + ':00 am'} - I'm having a nightmare where I get talon!")
                for _ in range(2):
                    self.hour = DayOfMyLife.HOURS_IN_A_DAY.popleft()
            else:
                print(f"{str(self.hour) + ':00 am'} - I'm having a nice dream where I get 100 points in Discrete Math!")
                for _ in range(2):
                    self.hour = DayOfMyLife.HOURS_IN_A_DAY.popleft()
        if self.hour in (7, 8):
            self.state = State.WAKE_UP
        elif self.hour in range(9, 19):
            print(f'{str(self.hour) + ":00 am" if self.hour < 12 else str(self.hour-12) + ":00 pm" if self.hour != 12 else str(self.hour) + ":00 pm"} - Oh no! I fell asleep again! My deadlines!')
            for _ in range(3):
                self.hour = DayOfMyLife.HOURS_IN_A_DAY.popleft()
                self.state = State.STUDY
        elif self.hour in range(19, 24):
            print(f'{str(self.hour) + ":00 pm" if self.hour < 12 else str(self.hour-12) + ":00 pm" if self.hour != 12 else str(self.hour) + ":00 pm"} - Oh no! I fell asleep again! Well, I will sleep until the morning!')
            while self.HOURS_IN_A_DAY:
                self.hour = DayOfMyLife.HOURS_IN_A_DAY.popleft()

    def wake_up(self):
        """I woke up!"""
        if self.hour == 7:
            print('7:00 am - Oh no! I slept too little! Now I have to drink coffee!')
            self.hour = DayOfMyLife.HOURS_IN_A_DAY.popleft()
            self.state = State.EAT
        elif self.hour == 8:
            print('8:00 am - I woke up! What a beautiful day! I will eat breakfast!')
            self.hour = DayOfMyLife.HOURS_IN_A_DAY.popleft()
            self.state = State.EAT

    def eat(self):
        """I'm eating!"""
        if self.hour == 8:
            print('8:00 am - I drank coffee and now I want to study! No breakfast today!')
            self.hour = DayOfMyLife.HOURS_IN_A_DAY.popleft()
            self.state = State.STUDY
        elif self.hour == 9:
            print('9:00 am - I ate breakfast! What a delicious pizza from Trapezna!')
            random_act = random.choice([0, 0, 0, 1, 2, 3]) ###
            self.hour = DayOfMyLife.HOURS_IN_A_DAY.popleft()
            if random_act == 0:
                self.state = State.STUDY
            elif random_act == 1:
                self.state = State.VIDEO_GAMES
            elif random_act == 2:
                self.state = State.WALK_WITH_FRIENDS
            else:
                self.state = State.SLEEP
        else:
            print(f'{str(self.hour) + ":00 am" if self.hour < 12 else str(self.hour-12) + ":00 pm" if self.hour != 12 else str(self.hour) + ":00 pm"} - I\'m eating in Trapezna again! Yummy! Now I want to study!')
            self.hour = DayOfMyLife.HOURS_IN_A_DAY.popleft()
            self.state = State.STUDY

    def study(self):
        """I'm studying!"""
        random_study = random.choice([0, 1, 2])
        if random_study == 0:
            print(f"{str(self.hour) + ':00 am' if self.hour < 12 else str(self.hour-12) + ':00 pm' if self.hour != 12 else str(self.hour) + ':00 pm'} - I'm studying Discrete Math! So cool!")
        elif random_study == 1:
            print(f"{str(self.hour) + ':00 am' if self.hour < 12 else str(self.hour-12) + ':00 pm' if self.hour != 12 else str(self.hour) + ':00 pm'} - I'm studying Math Analisys! Wow!")
        elif random_study == 2:
            print(f"{str(self.hour) + ':00 am' if self.hour < 12 else str(self.hour-12) + ':00 pm' if self.hour != 12 else str(self.hour) + ':00 pm'} - I'm studying Programming! So interesting!")
        if self.hour >= 20:
            while self.HOURS_IN_A_DAY:
                self.hour = DayOfMyLife.HOURS_IN_A_DAY.popleft()
                self.state = State.SLEEP
        else:
            for _ in range(3):
                self.hour = DayOfMyLife.HOURS_IN_A_DAY.popleft()
            random_state = random.choice([0, 1, 2])
            if random_state == 0:
                self.state = State.VIDEO_GAMES
            elif random_state == 1:
                self.state = State.WALK_WITH_FRIENDS
            else:
                self.state = State.SLEEP

    def video_games(self):
        """I'm playing video games!"""
        random_game = random.choice([0, 1])
        if random_game == 0:
            print(f"{str(self.hour) + ':00 am' if self.hour < 12 else str(self.hour-12) + ':00 pm' if self.hour != 12 else str(self.hour) + ':00 pm'} - I'm playing Fireboy and Watergirl with my friend! She's always dying! Now it's time for a walk!")
        if random_game == 1:
            print(f"{str(self.hour) + ':00 am' if self.hour < 12 else str(self.hour-12) + ':00 pm' if self.hour != 12 else str(self.hour) + ':00 pm'} - I'm playing Minecraft with a friend! She's always killing me! Now it's time for a walk!")
        if self.hour in range(21, 24):
            while self.HOURS_IN_A_DAY:
                self.hour = DayOfMyLife.HOURS_IN_A_DAY.popleft()
                self.state = State.SLEEP
        else:
            for _ in range(2):
                self.hour = DayOfMyLife.HOURS_IN_A_DAY.popleft()
                self.state = State.WALK_WITH_FRIENDS

    def walk_with_friends(self):
        """I'm walking with friends!"""
        if self.hour in range(19, 24):
            print(f"{str(self.hour) + ':00 pm' if self.hour < 12 else str(self.hour-12) + ':00 pm' if self.hour != 12 else str(self.hour) + ':00 pm'} - I'm walking with my friends in Stryistyi park! What a majestic place! Now it's time to sleep!")
            while self.HOURS_IN_A_DAY:
                self.hour = DayOfMyLife.HOURS_IN_A_DAY.popleft()
                self.state = State.SLEEP
        else:
            print(f"{str(self.hour) + ':00 pm' if self.hour < 12 else str(self.hour-12) + ':00 pm' if self.hour != 12 else str(self.hour) + ':00 pm'} - I'm walking with my friends and eating Faini lyody! So delicious!")
            for _ in range(3):
                self.hour = DayOfMyLife.HOURS_IN_A_DAY.popleft()
            self.state = State.EAT

if __name__ == "__main__":
    day = DayOfMyLife()
    day.run()
