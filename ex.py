import pygame
import sys
import math
from random import randint

x = 1900
y = 1000


class Micky:
    def __init__(self, screen):
        self.screen = screen
        self.color = randint(0, 255), randint(0, 255), randint(0, 255)
        self.center = randint(300, 1600), y // 4
        self.radius = 150
        self.width = 4
        self.act = 1
        self.mouth_coords = self.center[0] - 100, self.center[1]
        self.eyes = [[self.screen, self.color, [self.center[0] - 50, self.center[1] - 50], 15, 2],
                     [self.screen, self.color, [self.center[0] + 50, self.center[1] - 50], 15, 2]]
        self.nose = [self.screen, self.color, pygame.Rect(self.center[0] - 20, self.center[1] - 15, 40, 30), 2]
        self.mouth = [self.screen, self.color, pygame.Rect(self.center[0] - 75, self.center[1],
                                                           self.radius, self.radius / 2), math.pi, math.pi * 2]
        self.ears = [[self.screen, self.color, [self.center[0] - self.radius, self.center[1] - self.radius], 65, 2],
                     [self.screen, self.color, [self.center[0] + self.radius, self.center[1] - self.radius], 65, 2]]
        self.body = [self.screen, self.color, pygame.Rect(self.center[0] - 50, self.center[1] + self.radius, 100, 300),
                     2, 40]
        self.left_arm = [[self.screen, self.color, [self.center[0] - 50, self.center[1] + self.radius*9/7],
                          [self.center[0] - self.radius * 3/2,
                           self.center[1] + self.radius*9/7 + (-1)**(self.act + 1)*self.radius*2/7], 2],
                         [self.screen, self.color,
                          [self.center[0]-self.radius*27/16,
                           self.center[1] + self.radius*9/7 + (-1)**(self.act + 1)*self.radius*3/7]
                             , self.radius / 4, 3]]
        self.right_arm = [[self.screen, self.color, [self.center[0] + 50, self.center[1] + self.radius*9/7],
                          [self.center[0] + self.radius * 3/2,
                           self.center[1] + self.radius*9/7 + (-1)**self.act*self.radius*2/7], 2],
                         [self.screen, self.color,
                          [self.center[0]+self.radius*27/16,
                           self.center[1] + self.radius*9/7 + (-1)**self.act*self.radius*3/7]
                             , self.radius / 4, 3]]
        self.left_leg = [[self.screen, self.color, [self.center[0] - 50, self.center[1] + self.radius*39/14],
                          [self.center[0] - self.radius/2 + (-1)**(self.act + 1)*self.radius/6,
                           self.center[1] + self.radius*25/7], 2],
                         [self.screen, self.color,
                          [self.center[0] - self.radius/2 + (-1)**(self.act + 1)*self.radius/6,
                           self.center[1] + self.radius*107/28]
                             , self.radius / 4, 3]]
        self.right_leg = [[self.screen, self.color, [self.center[0]+self.radius/3, self.center[1] + self.radius*39/14],
                          [self.center[0] + self.radius/2 + (-1)**(self.act + 1)*self.radius/6,
                           self.center[1] + self.radius*25/7], 2],
                         [self.screen, self.color,
                          [self.center[0] + self.radius/2 + (-1)**(self.act + 1)*self.radius/4,
                           self.center[1] + self.radius*107/28]
                             , self.radius / 4, 3]]

    def change_color(self):
        self.color = randint(0, 255), randint(0, 255), randint(0, 255)
        self.eyes[0][1] = self.color
        self.eyes[1][1] = self.color
        self.nose[1] = self.color
        self.mouth[1] = self.color
        self.ears[0][1] = self.color
        self.ears[1][1] = self.color
        self.body[1] = self.color
        self.left_arm[0][1] = self.color
        self.left_arm[1][1] = self.color
        self.left_leg[0][1] = self.color
        self.left_leg[1][1] = self.color
        self.right_arm[0][1] = self.color
        self.right_arm[1][1] = self.color
        self.right_leg[0][1] = self.color
        self.right_leg[1][1] = self.color

    def tick(self):
        self.act += 1
        self.act %= 8
        self.left_leg[0][3][0] = self.center[0] - self.radius/2 + (-1)**(self.act + 1)*self.radius/6
        self.left_leg[1][2][0] = self.center[0] - self.radius/2 + (-1)**(self.act + 1)*self.radius/6
        self.right_leg[0][3][0] = self.center[0] + self.radius/2 + (-1)**(self.act + 1)*self.radius/6
        self.right_leg[1][2][0] = self.center[0] + self.radius / 2 + (-1) ** (self.act + 1) * self.radius / 6
        self.left_arm[0][3][1] = self.center[1] + self.radius*9/7 + (-1)**(self.act + 1)*self.radius*2/7
        self.left_arm[1][2][1] = self.center[1] + self.radius*9/7 + (-1)**(self.act + 1)*self.radius*3/7
        self.right_arm[0][3][1] = self.center[1] + self.radius*9/7 + (-1)**self.act*self.radius*2/7
        self.right_arm[1][2][1] = self.center[1] + self.radius*9/7 + (-1)**self.act*self.radius*3/7
        if not(self.act % 4):
            self.change_color()
        pass

    def draw(self):
        pygame.draw.circle(self.screen,
                           self.color,
                           self.center,
                           self.radius,
                           self.width)
        pygame.draw.circle(*self.eyes[0])
        pygame.draw.circle(*self.eyes[1])
        pygame.draw.ellipse(*self.nose)
        pygame.draw.arc(*self.mouth)
        pygame.draw.circle(*self.ears[0])
        pygame.draw.circle(*self.ears[1])
        pygame.draw.rect(*self.body)
        pygame.draw.line(*self.left_arm[0])
        pygame.draw.circle(*self.left_arm[1])
        pygame.draw.line(*self.right_arm[0])
        pygame.draw.circle(*self.right_arm[1])
        pygame.draw.line(*self.left_leg[0])
        pygame.draw.circle(*self.left_leg[1])
        pygame.draw.line(*self.right_leg[0])
        pygame.draw.circle(*self.right_leg[1])
        self.tick()


def main():
    pygame.init()
    screen = pygame.display.set_mode([x, y])
    emojis = [Micky(screen) for _ in range(100)]
    tick = 0
    game_over = False
    while not game_over:
        if tick == 1000 and len(emojis) < 1000:
            tick = 0
            emojis.append(Micky(screen))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        screen.fill([0, 0, 0])
        [i.draw() for i in emojis]
        pygame.display.flip()
        tick += 100
        pygame.time.wait(15)
    sys.exit()


if __name__ == '__main__':
    main()
