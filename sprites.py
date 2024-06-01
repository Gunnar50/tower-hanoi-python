import pygame
from settings import *
from typing import Tuple, Generic, List, TypeVar, Iterator

StackType = TypeVar("StackType")


class Disc:
    def __init__(self, x: int, y: int, size: int, colour: Tuple[int, int, int]):
        self.width = 100 + (size - 1) * 30
        self.x, self.y = x - self.width // 2, y
        self.height = DISC_HEIGHT
        self.colour = colour

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))

    def is_mouse_in(self, mx, my):
        return (
            self.x <= mx < self.x + self.width and self.y <= my < self.y + self.height
        )

    def click(self):
        print(self.colour)

    def __repr__(self) -> str:
        return f"{self.colour}"


class Towers:
    def __init__(self):
        initial_towers = Stack[Disc]()
        for i in range(4, -1, -1):
            initial_towers.push(
                Disc(200, (DISC_HEIGHT + GAPSIZE) * i, i + 1, COLOURS[i])
            )

        self.towers: List[Stack[Disc]] = [
            initial_towers,
            Stack[Disc](),
            Stack[Disc](),
        ]
        print(self.towers)

    def draw(self, screen: pygame.Surface):
        for tower in self.towers:
            for disc in tower:
                disc.draw(screen)

    def events(self, mx: int, my: int):
        for tower in self.towers:
            for disc in tower:
                if disc.is_mouse_in(mx, my):
                    disc.click()


class Stack(Generic[StackType]):
    def __init__(self) -> None:
        self.stack: List[StackType] = []

    def push(self, item: StackType) -> None:
        self.stack.append(item)

    def pop(self) -> StackType:
        return self.stack.pop()

    def __iter__(self) -> Iterator[StackType]:
        return iter(self.stack)

    def __repr__(self) -> str:
        return f"{self.stack}"
