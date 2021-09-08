import math
import pint


ureg = pint.UnitRegistry()

BORE_SIZE = 32 * ureg.mm  # diameter of piston head
STROKE = 200 * ureg.mm
PISTON_WEIGHT = 910 * ureg.g

piston_area = BORE_SIZE * math.pi
