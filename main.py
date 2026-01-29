import numpy as np
from src.model.young_engine import YoungEngine
from src.model.experiment_state import ExperimentState
from src.utils.math_conversions import *

# Initial Experiment State
state = ExperimentState(
    wavelength_m = nm_to_m(637.5),
    slit_distance_m = mm_to_m(0.3),
    slit_width_m = mm_to_m(0.05),
    screen_distance_m = 1.0
)

pos_xs = np.linspace(-0.01, 0.01, 9)

for x in pos_xs:
  intensity = YoungEngine.calculate_intensity(x, state)
  print(f"x = {x:+.4f} m -> Intensity = {intensity:.4f} {'-> MAX' if abs(x) < 1e-12 else ''}")