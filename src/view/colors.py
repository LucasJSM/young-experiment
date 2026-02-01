def wavelength_to_rgb(l: float):
    """
    Convert wavelength (nm) to RGB (0-255 range)
    """
    r = g = b = 0.0

    if 380 <= l < 440:
        r = -(l - 440) / (440 - 380)
        b = 1
    elif 440 <= l < 490:
        g = (l - 440) / (490 - 440)
        b = 1
    elif 490 <= l < 510:
        g = 1
        b = -(l - 510) / (510 - 490)
    elif 510 <= l < 580:
        r = (l - 510) / (580 - 510)
        g = 1
    elif 580 <= l < 645:
        r = 1
        g = -(l - 645) / (645 - 580)
    elif 645 <= l <= 780:
        r = 1

    R = int(r * 255)
    G = int(g * 255)
    B = int(b * 255)

    return (R, G, B)