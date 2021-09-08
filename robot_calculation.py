import math
import pint
import numpy as np


ureg = pint.UnitRegistry()

# piston constants
BORE_SIZE = 32 * ureg.mm  # diameter of piston head
STROKE = 200 * ureg.mm
PISTON_WEIGHT = 910 * ureg.g


# mass of chassis
CHASSIS_WEIGHT = 2 * ureg.kg

# compressor constants
COMPRESSOR_PRESSURE = 30 * ureg.psi

# natural constants
ATMOS_PRESSURE = 1 * ureg.bar
GRAVITY_ACCELLERATION = 9.8 * ureg.m/ureg.s**2


# area is pi*r^2
piston_area = np.pi * (BORE_SIZE/2)**2

force_exerted = ((COMPRESSOR_PRESSURE - ATMOS_PRESSURE)*piston_area).to(ureg.newton)
print("force exerted at each point of piston stroke:", force_exerted)

energy_exerted = (force_exerted * STROKE).to(ureg.joules)
print("work done by piston:", energy_exerted)

# gravity is acting on device when piston is expanding upwards
energy_plus_gravity = energy_exerted - GRAVITY_ACCELLERATION*(PISTON_WEIGHT + CHASSIS_WEIGHT)*STROKE
print("pison force minus gravity:", energy_plus_gravity)

exit_velocity_squared = (2 * energy_plus_gravity / (PISTON_WEIGHT + CHASSIS_WEIGHT)).to((ureg.m/ureg.s)**2)
exit_velocity = np.sqrt(exit_velocity_squared)
print("exit velocity of robot is:", exit_velocity)

