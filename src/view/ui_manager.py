import pygame
import pygame_gui
from src.utils.math_conversions import *

class UIManager:
    def __init__(self, screen_size, state):
        self.state = state
        self.manager = pygame_gui.UIManager(screen_size)

        # slider positions
        y_start = 520
        spacing = 50
        width = 320
        height = 25
        x = 50

        # wavelength slider
        self.wavelength_slider = pygame_gui.elements.UIHorizontalSlider(
            pygame.Rect((x, y_start), (width, height)),
            start_value = m_to_nm(state.wavelength_m),
            value_range = (380.0, 780.0),
            manager = self.manager,
        )

        self.wavelength_label = pygame_gui.elements.UILabel(
            pygame.Rect((x, y_start - 22), (width, 20)),
            "Comprimento de Onda λ (nm)",
            manager = self.manager
        )

        # slit distance slider
        self.slit_distance_slider = pygame_gui.elements.UIHorizontalSlider(
            pygame.Rect((x, y_start + spacing), (width, height)),
            start_value = m_to_um(state.slit_distance_m),
            value_range = (10.0, 200.0),
            manager = self.manager
        )

        self.slit_distance_label = pygame_gui.elements.UILabel(
            pygame.Rect((x, y_start + spacing - 22), (width, 20)),
            "Distância entre fendas (um)",
            manager=self.manager
        )

        # slit width slider
        self.slit_width_slider = pygame_gui.elements.UIHorizontalSlider(
            pygame.Rect((x, y_start + 2 * spacing), (width, height)),
            start_value = m_to_um(state.slit_width_m),
            value_range = (1.0, 50.0),
            manager = self.manager
        )

        self.slit_width_label = pygame_gui.elements.UILabel(
            pygame.Rect((x, y_start + 2*spacing - 22), (width, 20)),
            "Largura da fenda (um)",
            manager=self.manager
        )

        # screen distance slider
        self.screen_distance_slider = pygame_gui.elements.UIHorizontalSlider(
            pygame.Rect((x, y_start + 3 * spacing), (width, height)),
            start_value = state.screen_distance_m,
            value_range = (0.5, 5.0),
            manager = self.manager
        )

        self.screen_distance_label = pygame_gui.elements.UILabel(
            pygame.Rect((x, y_start + 3*spacing - 22), (width, 20)),
            "Distância da tela (m)",
            manager=self.manager
        )

        # screen range slider
        self.screen_range_slider = pygame_gui.elements.UIHorizontalSlider(
            pygame.Rect((x, y_start + 4 * spacing), (width, height)),
            start_value = state.screen_range_m * 200.0,
            value_range = (1.0, 100.0),
            manager = self.manager
        )

        self.screen_range_label = pygame_gui.elements.UILabel(
            pygame.Rect((x, y_start + 4*spacing - 22), (width, 20)),
            "Campo de visão (cm)",
            manager=self.manager
        )


    
    def process_events(self, event):
        self.manager.process_events(event)


    def update(self, time):
        self.manager.update(time)

        # update wavelength
        self.state.wavelength_m = nm_to_m(
            self.wavelength_slider.get_current_value()
        )

        self.wavelength_label.set_text(
            f"Comprimento de onda (nm): {self.wavelength_slider.get_current_value():.1f}"
        )

        # update slit distance
        self.state.slit_distance_m = um_to_m(
            self.slit_distance_slider.get_current_value()
        )

        self.slit_distance_label.set_text(
            f"Distância entre fendas (um): {self.slit_distance_slider.get_current_value():.1f}"
        )

        # update slit width
        self.state.slit_width_m = um_to_m(
            self.slit_width_slider.get_current_value()
        )

        self.slit_width_label.set_text(
            f"Largura da fenda (um): {self.slit_width_slider.get_current_value():.1f}"
        )

        # update screen distance
        self.state.screen_distance_m = (
            self.screen_distance_slider.get_current_value()
        )

        self.screen_distance_label.set_text(
            f"Distância da tela (m): {self.screen_distance_slider.get_current_value():.2f}"
        )

        # update screen range (zoom)
        self.state.screen_range_m = (
            self.screen_range_slider.get_current_value() / 200.0
            # (self.screen_range_slider.get_current_value() * 100.0) / 200.0
        )

        self.screen_range_label.set_text(
            f"Campo de visão (cm): {self.screen_range_slider.get_current_value():.1f}"
        )


    def draw(self, screen):
        self.manager.draw_ui(screen)
