from dataclasses import dataclass

@dataclass
class ExperimentState:
  wavelength_m: float            # Lambda (m)
  slit_distance_m: float         # Distance between slits (m)
  slit_width_m: float            # Width of each slit (m)
  screen_distance_m: float       # Distance from slits to screen (m)  
  intensity_max: float = 1.00