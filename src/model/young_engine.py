import numpy as np
from .experiment_state import ExperimentState

class YoungEngine:
    @staticmethod
    def calculate_intensity(
        pos_x: float | np.ndarray, 
        state: ExperimentState) -> float | np.ndarray:
        """
        Calculate the light intensity at position x on the screen for Young's Double-Slit Experiment (Fraunhofer)

        Args: pos_x (float or numpy array): position on the screen (m)
        state (ExperimentState): current state of the experiment

        Returns: light intensity (float or numpy array)
        """ 

        # Parameters from state
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