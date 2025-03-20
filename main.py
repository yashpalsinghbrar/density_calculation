import pandas as pd
import numpy as np

# Read and clean sucrose data
file_path = 'sucrose_de_e.xls'
df_sucrose = pd.read_excel(file_path, sheet_name=0)
matrix_sucrose = df_sucrose.values[2:,:]
sucrose_ww = pd.to_numeric(matrix_sucrose[:,0], errors='coerce')
sucrose_d = pd.to_numeric(matrix_sucrose[:,1], errors='coerce')

# Read and clean glucose data
file_path = 'd_glucose_de_e.xls'
df_glucose = pd.read_excel(file_path, sheet_name=0)
matrix_glucose = df_glucose.values[2:,:]
glucose_ww = pd.to_numeric(matrix_glucose[:,0], errors='coerce')
glucose_d = pd.to_numeric(matrix_glucose[:,1], errors='coerce')

# Input validation
while True:
    try:
        option = int(input('Please choose the chemical - \n1. D-Glucose\n2. Sucrose\nEnter Option: '))
        if option in [1, 2]:
            break
        print('Please enter a valid input, there are only 2 option mate. Do not try to play smart.')
    except:
        print('Please enter a valid input, there are only 2 option mate. Do not try to play smart.')

while True:
    try:
        conc = float(input('Please enter the concentration of the Solution (in M): '))
        if conc < 0:
            print('How can concentration be NEGATIVE? Are you stupid?')
        else:
            break
    except:
        print('Concentration can only be a poisitve real number. Are you dumb?')

# Molecular weights
mw_sucrose = 342.296
mw_glucose = 180.16

# Polynomial fits (degree 4)
degree = 4
coeff_g = np.polyfit(glucose_ww, glucose_d, degree)
coeff_s = np.polyfit(sucrose_ww, sucrose_d, degree)
f_glucose = np.poly1d(coeff_g)
f_sucrose = np.poly1d(coeff_s)

# Calculate density
volume = 1000  # 1L in mL
if option == 1:
    m_solute = conc * mw_glucose
    f = f_glucose
    name = "glucose"
else:
    m_solute = conc * mw_sucrose
    f = f_sucrose
    name = "sucrose"

# Initial guess
density = 1.0  # Start with water’s density
mass_solution = volume * density
m_water = mass_solution - m_solute
if m_water < 0:
    m_water = 0
    mass_solution = m_solute
    density = m_solute/volume
per_w_by_w = 100 * m_solute / mass_solution

# Refine iteratively
tolerance = 0.000001
for i in range(100):
    old_density = density
    mass_solution = density * volume
    per_w_by_w = 100 * m_solute / mass_solution
    if per_w_by_w > 100:
        per_w_by_w = 100
    density = f(per_w_by_w)
    if abs(density - old_density) < tolerance:
        break

print(f'% w/w of {name} solution is {per_w_by_w:.2f}%. Density of {name} solution is {density} g/mL.')