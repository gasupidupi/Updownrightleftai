import random

class Main:

    directions = ["up", "down", "right", "left"]
    weights = [50, 50, 50, 50]
    position = [1, 1]
    map = [[-1, -1, -1], [-1, -1, 1], [-1, -1, -1]]

    def __init__(self):
        pass


    def main(self):
        for i in range(100):
            direction = random.choices(
                self.directions,
                weights=(
                    self.weights[0],
                    self.weights[1],
                    self.weights[2],
                    self.weights[3]
                ),
                k=1
            )[0]
            self.go_direction(direction)
            reward = self.check_reward()
            self.adjust_weight(direction, reward)
            self.reset_position()
        print(self.directions)
        print(self.weights)

    def go_direction(self, direction):
        if direction == "up":
            self.position[0] += 1
        if direction == "down":
            self.position[0] -= 1
        if direction == "right":
            self.position[1] += 1
        if direction == "left":
            self.position[1] -= 1

    def check_reward(self):
        return self.map[self.position[0]][self.position[1]]

    def adjust_weight(self, direction, reward):
        if direction == "up":
            self.weights[0] += reward
        if direction == "down":
            self.weights[1] += reward
        if direction == "right":
            self.weights[2] += reward
        if direction == "left":
            self.weights[3] += reward

    def reset_position(self):
        self.position = [1, 1]


if __name__=="__main__":
    main = Main()
    main.main()
