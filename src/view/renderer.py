import pygame
import numpy as np
from src.model.young_engine import YoungEngine
from src.view.colors import wavelength_to_rgb
from src.utils.math_conversions import *

class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()

        # plot position
        self.center_y = self.height // 2 
        self.plot_height = 200

        self.x_pixels = np.arange(self.width)

        self.screen.fill((20, 20, 20))

    def draw_axes(self):
        # main axis
        pygame.draw.line(
            self.screen,
            (200, 200, 200),
            (0, self.center_y),
            (self.width, self.center_y),
            1
        )


    def draw_interference(self, state):
        color = wavelength_to_rgb(m_to_nm(state.wavelength_m))

        for px in range(self.width):
            x_m = pixel_to_meter(px, self.width, state.screen_range_m)
            intensity = YoungEngine.calculate_intensity(x_m, state)

            y = int(self.center_y - intensity * self.plot_height)

            pygame.draw.circle(self.screen, color, (px, y), 1)
