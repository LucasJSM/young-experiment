import pygame
import pygame_gui
from src.utils.math_conversions import *

class UIManager:
    def __init__(self, screen_size, state):
        self.state = state
        self.manager = pygame_gui.UIManager(screen_size, theme_path="theme.json")

        # dictionary to hold references to UI components
        self.components = {}

        # UI layout params
        x_start = 50
        y_start = 520
        spacing = 50
        width = 320
        height = 25
        input_width = 80

        # to_state/from_state functions convert between UI values and state values
        self.build_components(
            name = "wavelength",
            label_text = "Comprimento de Onda λ (nm)",
            x = x_start,
            y = y_start,
            slider_range = (380.0, 780.0),
            start_value = m_to_nm(state.wavelength_m),
            to_state = nm_to_m,
            from_state = m_to_nm,
        )

        self.build_components(
            name = "slit_distance",
            label_text = "Distância entre fendas (μm)",
            x = x_start,
            y = y_start + spacing,
            slider_range = (10.0, 200.0),
            start_value = m_to_um(state.slit_distance_m),
            to_state = um_to_m,
            from_state = m_to_um,
        )

        self.build_components(
            name = "slit_width",
            label_text = "Largura da fenda (μm)",
            x = x_start,
            y = y_start + 2 * spacing,
            slider_range = (1.0, 50.0),
            start_value = m_to_um(state.slit_width_m),
            to_state = um_to_m,
            from_state = m_to_um,
        )

        self.build_components(
            name = "screen_distance",
            label_text = "Distância da tela (m)",
            x = x_start,
            y = y_start + 3 * spacing,
            slider_range = (0.5, 5.0),
            start_value = state.screen_distance_m,
            to_state = lambda x: x,
            from_state = lambda x: x,
        )

        self.build_components(
            name = "screen_range",
            label_text = "Campo de visão (cm)",
            x = x_start,
            y = y_start + 4 * spacing,
            slider_range = (2.0, 20.0),
            start_value = m_to_cm(state.screen_range_m),
            to_state = cm_to_m,
            from_state = m_to_cm,
        )


    def build_components(self, name, label_text, x, y, slider_range, start_value, to_state, from_state):
        slider_width = 250
        label_width = 320

        label_x = x - (label_width - slider_width) // 2

        label = pygame_gui.elements.UILabel(
            relative_rect = pygame.Rect((label_x, y - 20), (label_width, 20)),
            text = label_text,
            manager = self.manager,
        )
        
        slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect = pygame.Rect((x, y), (250, 25)),
            start_value = start_value,
            value_range = slider_range,
            manager = self.manager,
            object_id = "#slider",
        )

        input_field = pygame_gui.elements.UITextEntryLine(
            relative_rect = pygame.Rect((x + 270, y), (80, 25)),
            manager = self.manager,
        )

        input_field.set_text(f"{start_value:.2f}")

        self.components[name] = {
            "slider": slider,
            "input": input_field,
            "to_state": to_state,
            "from_state": from_state,
        }

    
    def process_events(self, event):
        self.manager.process_events(event)

        if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
            for name, param in self.components.items():
                if event.ui_element == param["slider"]:
                    value = event.value
                    param["input"].set_text(f"{value:.2f}")

                    setattr(
                        self.state,
                        f"{name}_m",
                        param["to_state"](value),
                    )

        if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
            for name, param in self.components.items():
                if event.ui_element == param["input"]:
                    try:
                        value = float(param["input"].get_text())

                        min_val, max_val = param["slider"].value_range
                        value = max(min_val, min(max_val, value))

                        param["slider"].set_current_value(value)

                        setattr(
                            self.state,
                            f"{name}_m",
                            param["to_state"](value),
                        )

                    except ValueError:
                        pass
    

    def update(self, time):
        self.manager.update(time)


    def draw(self, screen):
        self.manager.draw_ui(screen)
