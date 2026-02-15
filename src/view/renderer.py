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

        # container
        self.margin_x = 50
        self.plot_width = self.width - (2 * self.margin_x)
        self.plot_top = 50
        self.plot_height = 280
        self.plot_bottom = self.plot_top + self.plot_height 

        self.x_pixels = np.arange(self.plot_width)

        self.screen.fill((20, 20, 20))

    def draw_axes(self):
        container_rect = (self.margin_x, self.plot_top, self.plot_width, self.plot_height)

        pygame.draw.rect(self.screen, (60, 60, 60), container_rect, 1)

        center_x = self.margin_x + (self.plot_width // 2)

        # main axis
        pygame.draw.line(
            self.screen,
            (60, 60, 60),
            (center_x, self.plot_top),
            (center_x, self.plot_bottom),
            1
        )

        # cross axis
        pygame.draw.line(
            self.screen,
            (60, 60, 60),
            (self.margin_x, self.plot_bottom), 
            (self.margin_x + self.plot_width, self.plot_bottom),
            1
        )


    def draw_interference(self, state):
        color = wavelength_to_rgb(m_to_nm(state.wavelength_m))

        # Convert pixel positions to physical positions
        x_array = (self.x_pixels / self.plot_width - 0.5) * 2.0 * state.screen_range_m

        # Calculate intensities at each position
        intensities = YoungEngine.calculate_intensity(x_array, state)

        # Map y positions in screen
        y_values = self.plot_bottom - (intensities * self.plot_height)

        x_screen = self.x_pixels + self.margin_x

        # Create points for drawing
        points = np.column_stack((x_screen, y_values))

        # Draw lines between points
        if len(points) > 1:
            pygame.draw.aalines(self.screen, color, False, points, blend = 1)