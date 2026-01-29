import numpy as np
from .experiment_state import ExperimentState

class YoungEngine:
  @staticmethod
  def calculate_intensity(pos_x: float, state: ExperimentState) -> float:
    """
    Calculate the light intensity at position x on the screen for Young's Double-Slit Experiment (Fraunhofer)

    Args: pos_x (float): position on the screen (m)
          state (ExperimentState): current state of the experiment

    Returns: light intensity (float)
    """ 
    
    # Parameters from state
    lambda_ = state.wavelength_m
    d = state.slit_distance_m
    a = state.slit_width_m
    L = state.screen_distance_m

    # Case pos_x == 0 to avoid division by 0
    if(abs(pos_x) < 1e-10): 
      return 1.0

    # Single-Slit Diffraction (Fraunhofer)
    alpha = (np.pi * a * pos_x) / (lambda_ * L)
    diffraction = (np.sin(alpha) / alpha) ** 2

    # Double-slit Interference
    beta = (np.pi * d * pos_x) / (lambda_ * L)
    interference = (np.cos(beta)) ** 2

    # Young's Double-Slit Intensity
    intensity = diffraction * interference

    return intensity