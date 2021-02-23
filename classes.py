import pygame
from constants import WIDTH, HEIGHT, g, t

class Ball():
    def __init__(self, win, colour, x, y, radius, mass, V):
        self.win = win
        self.colour = colour
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.prev_pos = None
        self.V = V
        self.hold = False

    def pos(self):
        return (self.x, self.y)

    def draw(self):
        pygame.draw.circle(self.win, self.colour, self.pos(), self.radius)

    def update(self):
        if not self.hold:
            actualx, actualy = self.x, self.y
            futurex, futurey = actualx + self.V[0], actualy + self.V[1] + g * t
            if futurey > HEIGHT - self.radius:
                self.V[1] = -0.8*self.V[1]
                self.V[0] = 0.8*self.V[0]
                self.y -= 1
            if futurey == HEIGHT - self.radius:
                pass
            if futurey <= self.radius + 1:
                self.V[1] = -0.8*self.V[1]
                self.y += 1
            if futurex > WIDTH - self.radius:
                self.V[0] = -0.8*self.V[0]
                self.x -= 1
            if futurex < self.radius:
                self.V[0] = -0.8*self.V[0]
                self.x += 1
            else:
                self.V[1] += g * t
                self.y += self.V[1]
                self.x += self.V[0]

    def change_hold(self):
        if self.hold:
            self.hold = False
        elif not self.hold:
            self.hold = True





class Table():
    def __init__(self, win, objects=None):
        self.win = win
        if not objects:
            self.objects = []
        else:
            self.objects = objects

    def add_object(self, my_object):
        self.objects.append(my_object)

    def draw_objects(self):
        for obj in self.objects:
            obj.draw()

    def update(self):
        for obj in self.objects:
            obj.update()

        self.draw_objects()