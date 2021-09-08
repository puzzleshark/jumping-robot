import math
import pint


ureg = pint.UnitRegistry()

# piston constants
BORE_SIZE = 32 * ureg.mm  # diameter of piston head
STROKE = 200 * ureg.mm
PISTON_WEIGHT = 910 * ureg.g

# compressor constants
COMPRESSOR_PRESSURE = 100 * ureg.psi

# natural constants
ATMOS_PRESSURE = 1 * ureg.bar
GRAVITY_ACCELLERATION = 9.8 * ureg.m / ureg.s ** 2



piston_area = BORE_SIZE * math.pi * ureg.mm  # area is diameter * pi

force_exerted = (COMPRESSOR_PRESSURE - ATMOS_PRESSURE) * piston_area
force_exerted = force_exerted.to(ureg.newton)

print(force_exerted)