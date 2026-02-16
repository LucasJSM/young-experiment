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

        # side margin
        self.margin_x = 50
        
        # plot dimensions
        self.plot_width = self.width - (2 * self.margin_x)
        self.plot_height = 280
        self.plot_top = 50
        self.plot_bottom = self.plot_top + self.plot_height

        self.x_pixels = np.arange(self.plot_width)

        self.screen.fill((20, 20, 20))

        # screen view for displaying the interference on the wall
        self.screen_height = 70
        self.screen_y = self.plot_bottom + 20

        # surface for drawing the screen view
        self.strip_surface = pygame.Surface((self.plot_width, self.screen_height))


    def draw_container(self):
        # dimensions of the container
        container_rect = (self.margin_x, self.plot_top, self.plot_width, self.plot_height)

        # draw container
        pygame.draw.rect(self.screen, (30, 30, 35), container_rect, 0)

        # draw container border
        pygame.draw.rect(self.screen, (100, 100, 100), container_rect, 2)

        # main axis
        center_x = self.margin_x + (self.plot_width // 2)
        pygame.draw.line(
            self.screen,
            (60, 60, 60),
            (center_x, self.plot_top),
            (center_x, self.plot_bottom),
            2
        )

        # cross axis
        pygame.draw.line(
            self.screen,
            (60, 60, 60),
            (self.margin_x, self.plot_bottom), 
            (self.margin_x + self.plot_width, self.plot_bottom),
            2
        )


    def draw_interference(self, state):
        color = wavelength_to_rgb(m_to_nm(state.wavelength_m))

        # Convert pixel positions to physical positions
        x_array = (self.x_pixels / self.plot_width - 0.5) * state.screen_range_m

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
        
        self.draw_screen(intensities, color)

    
    def draw_screen(self, intensities, color):
        screen_y = self.plot_bottom + 10
        
        # clamp intensity values to prevent color overflow
        intensities_clipped = np.clip(intensities, 0.0, 1.0)
        
        # scale the color by the intensity at each point and convert to uint8
        r = (color[0] * intensities_clipped).astype(np.uint8)
        g = (color[1] * intensities_clipped).astype(np.uint8)
        b = (color[2] * intensities_clipped).astype(np.uint8)
        rgb_array = np.column_stack((r, g, b))
        
        # expand the 1D array into a 2D image array by repeating each color value
        surface_array = np.repeat(
            rgb_array[:, np.newaxis, :],
            self.screen_height,
            axis = 1
        )
            
        # copy NumPy array data into the surface
        pygame.surfarray.blit_array(self.strip_surface, surface_array)

        # render the surface on the screen
        self.screen.blit(self.strip_surface, (self.margin_x, screen_y))

        # draw border
        pygame.draw.rect(
            self.screen, 
            (100, 100, 100), 
            (self.margin_x, screen_y, self.plot_width, self.screen_height), 
            2
        )