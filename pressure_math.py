# Average Mud Weight Calculation
height_of_mud_one = input('Height Mud 1: ')
weight_of_mud_one = input('Weight Mud 1: ')
height_of_mud_two = input('Height Mud 2: ')
weight_of_mud_two = input('Weight Mud 1: ')
total_tvd = input('Total TVD: ')

average_weight = ((height_of_mud_one * weight_of_mud_one) + (height_of_mud_two * weight_of_mud_two)) / total_tvd
print('Average Mud Weight:')
print(average_weight)

psi_constant = 0.052

total_psi = (weight_of_mud_one * height_of_mud_one * psi_constant) + (weight_of_mud_two * height_of_mud_two * psi_constant)
print('Total PSI:')
print(total_psi)


Pipe Light Calculations

surface_annular_pressure = input('Surface Annular Pressure: ')
surface_annular_pump_pressure = input('Annular Pump Pressure: ')
drill_pipe_outside_dimater = input('Drill Pipe OD: ')
weight_of_pipe_per_foot = input('Weight of Drill Pipe per Foot: ')
mud_weight = input('Light Annular Mud Weight: ')
kill_mud_weight = input('Kill Weight Mud: ')
pi = 3.14
lifting_force_constant = 4 # Check this number

lifting_force = (drill_pipe_outside_dimater ** 2) /lifting_force_constant * pi * (surface_annular_pressure + surface_annular_pump_pressure)
boyancy_factor = (65.5 - mud_weight) / 65.5

minimum_length_of_pipe_before_pipe_light = lifting_force / (weight_of_pipe_per_foot * boyancy_factor)

print('Lifting Force: ')
print(lifting_force)
print('Minimum Length of Pipe: ')
print(minimum_length_of_pipe_before_pipe_light)

# Height of Kill Mud Calculations
print('--------------------')
casing_inside_diameter = input('Casing ID: ')
annular_capacity = (casing_inside_diameter ** 2 - drill_pipe_outside_dimater ** 2) / 1029.4

height_of_kill_mud = surface_annular_pressure / ((kill_mud_weight - mud_weight) * 0.052)
barrels_of_kill_mud = height_of_kill_mud * (annular_capacity)

print('Height of Kill Mud: ')
print(height_of_kill_mud)
print('Barrels of Kill Mud Required: ')
print(barrels_of_kill_mud)
