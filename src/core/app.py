import pygame
from src.model.experiment_state import ExperimentState
from src.view.renderer import Renderer
from src.view.ui_manager import UIManager
from src.utils.math_conversions import *

class App:
    def __init__(self):
        pygame.init()

        # Screen size
        self.size = (1540, 800)

        self.screen = pygame.display.set_mode(self.size, pygame.RESIZABLE)
        pygame.display.set_caption("Simulação - Experimento da Fenda Dupla de Young")

        self.clock = pygame.time.Clock()
        self.running = True

        self.font = pygame.font.SysFont("Arial", 18)

        # Initial experiment state
        self.state = ExperimentState(
            wavelength_m = nm_to_m(637.5),
            slit_distance_m = um_to_m(30),
            slit_width_m = um_to_m(5.0),
            screen_distance_m = 1.2,
            screen_range_m = cm_to_m(8)
        )

        self.renderer = Renderer(self.screen)
        self.ui_manager = UIManager(self.size, self.state)


    def run(self):
        while self.running:
            time = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                self.ui_manager.process_events(event)

            self.ui_manager.update(time)

            self.screen.fill((20, 20, 20))
            self.renderer.draw_axes()
            self.renderer.draw_interference(self.state)
            self.ui_manager.draw(self.screen)

            pygame.display.flip()

        pygame.quit()
