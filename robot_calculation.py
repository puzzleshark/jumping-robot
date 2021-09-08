import math
import pint


ureg = pint.UnitRegistry()

BORE_SIZE = 32 * ureg.mm  # diameter of piston head
STROKE = 200 * ureg.mm
PISTON_WEIGHT = 910 * ureg.g


COMPRESSOR_PRESSURE = 100 * ureg.psi
ATMOS_PRESSURE = 1 * ureg.bar

piston_area = BORE_SIZE * math.pi * ureg.mm  # area is diameter * pi

force_exerted = (COMPRESSOR_PRESSURE - ATMOS_PRESSURE) * piston_area

force_exerted = force_exerted.to(ureg.newton)

print(force_exerted)