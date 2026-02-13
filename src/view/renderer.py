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

        # Convert pixel positions to physical positions
        x_array = (self.x_pixels / self.width - 0.5) * 2.0 * state.screen_range_m

        # Calculate intensities at each position
        intensities = YoungEngine.calculate_intensity(x_array, state)

        # Map y positions in screen
        y_values = self.center_y - (intensities * self.plot_height)

        # Create points for drawing
        points = np.column_stack((self.x_pixels, y_values))

        # Draw lines between points
        if len(points) > 1:
            pygame.draw.aalines(self.screen, color, False, points, blend = 1)