import math
import pint
import numpy as np


ureg = pint.UnitRegistry()

# piston constants
BORE_SIZE = 32 * ureg.mm  # diameter of piston head
STROKE = 200 * ureg.mm
PISTON_WEIGHT = 910 * ureg.g


# mass of chassis
CHASSIS_WEIGHT = 8 * ureg.kg

# compressor constants
COMPRESSOR_PRESSURE = 70 * ureg.psi

# natural constants
ATMOS_PRESSURE = 1 * ureg.bar
GRAVITY_ACCELLERATION = 9.8 * ureg.m/ureg.s**2

print("total weight", (CHASSIS_WEIGHT+PISTON_WEIGHT).to(ureg.lb))

# area is pi*r^2
piston_area = np.pi * (BORE_SIZE/2)**2
print("piston area is", piston_area.to(ureg.inch ** 2))

force_exerted = ((COMPRESSOR_PRESSURE - ATMOS_PRESSURE)*piston_area).to(ureg.newton)
print("force exerted at each point of piston stroke:", force_exerted)

energy_exerted = (force_exerted * STROKE).to(ureg.joules)
print("work done by piston:", energy_exerted)

# gravity is acting on device when piston is expanding upwards
energy_plus_gravity = energy_exerted - GRAVITY_ACCELLERATION*(PISTON_WEIGHT + CHASSIS_WEIGHT)*STROKE
print("piston force minus gravity:", energy_plus_gravity)

exit_velocity_squared = (2 * energy_plus_gravity / (PISTON_WEIGHT + CHASSIS_WEIGHT)).to((ureg.m/ureg.s)**2)
exit_velocity = np.sqrt(exit_velocity_squared)
print("exit velocity of robot is:", exit_velocity)

# formula for velocity vs. time -g*t + v0
# therefore formula for x is -(g/2)*t**2 + v0*t
# therefore landing time -g*t + v0 = -v0 => g*t = 2v0 => t = 2v0/g
# therefore airtime is
airtime = 2 * exit_velocity / GRAVITY_ACCELLERATION
print("robot will be airborne for ", airtime)

# with max height of
max_height = -(GRAVITY_ACCELLERATION/2)*(airtime/2)**2 + exit_velocity * (airtime/2)
print("max height", max_height)
max_height_energy_calc = (energy_plus_gravity/((PISTON_WEIGHT+CHASSIS_WEIGHT)*GRAVITY_ACCELLERATION)).to(ureg.m)
print("max height energy calc", max_height)

