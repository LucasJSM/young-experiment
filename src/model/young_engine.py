import numpy as np
from .experiment_state import ExperimentState

class YoungEngine:
    @staticmethod
    def calculate_intensity(
        pos_x: float | np.ndarray, 
        state: ExperimentState) -> float | np.ndarray:
        """
            Calculate the intensity of light on the screen.

            Parameters:
            - pos_x: Position(s) on the screen (in meters) where intensity is calculated
            - state: An instance of ExperimentState containing the parameters of the experiment

            Returns:
            - Intensity of light at the given position(s) on the screen
        """ 

        lambda_ = state.wavelength_m
        d = state.slit_distance_m
        a = state.slit_width_m
        L = state.screen_distance_m

        # Single-Slit Diffraction (Fraunhofer)
        u_diffraction = (a * pos_x) / (lambda_ * L)
        diffraction = np.sinc(u_diffraction) ** 2 # sinc function avoid division by zero

        # Double-slit Interference
        beta = (np.pi * d * pos_x) / (lambda_ * L)
        interference = (np.cos(beta)) ** 2

        # Young's Double-Slit Intensity
        intensity = diffraction * interference

        return intensity
    

    @staticmethod
    def calculate_fringe_spacing(state: ExperimentState) -> float:
        """
            Calculate the distance between adjacent maxima on the screen.

            Parameters:
            - state: An instance of ExperimentState containing the parameters of the experiment

            Returns:
            - Distance between adjacent maxima on the screen (in meters)
        """

        lambda_ = state.wavelength_m
        d = state.slit_distance_m
        L = state.screen_distance_m

        if d == 0:
            return 0.0
        
        delta_y = (lambda_ * L) / d
        
        return delta_y