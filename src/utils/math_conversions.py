# =========================
# Unit conversions
# =========================

def nm_to_m(value_nm: float) -> float:
    """Nanometers to meters"""
    return value_nm * 1e-9

def m_to_nm(value_m: float) -> float:
    """Meters to nanometers"""
    return value_m * 1e9


def mm_to_m(value_mm: float) -> float:
    """Millimeters to meters"""
    return value_mm * 1e-3

def m_to_mm(value_m: float) -> float:
    """Meters to millimeters"""
    return value_m * 1e3


def um_to_m(value_um: float) -> float:
    """Micrometers to meters"""
    return value_um * 1e-6

def m_to_um(value_m: float) -> float:
    """Meters to micrometers"""
    return value_m * 1e6


def cm_to_m(value_cm: float) -> float:
    """Centimeters to meters"""
    return value_cm * 1e-2

def m_to_cm(value_m: float) -> float:
    """Meters to centimeters"""
    return value_m * 1e2