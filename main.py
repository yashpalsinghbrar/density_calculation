import pandas as pd

# Read the .xls file for sucrose and store the data
file_path = 'sucrose_de_e.xls'
df_sucrose = pd.read_excel(file_path, sheet_name=0)  # sheet_name=0 reads the first sheet

matrix_sucrose = df_sucrose.values  # Converts DataFrame to NumPy array (2D matrix)
matrix_sucrose = matrix_sucrose[2:,:]

# Read the .xls file aor D-Glucose and store the data
file_path = 'd_glucose_de_e.xls'  
df_glucose = pd.read_excel(file_path, sheet_name=0)  # sheet_name=0 reads the first sheet

matrix_glucose = df_glucose.values  # Converts DataFrame to NumPy array (2D matrix)
matrix_glucose = matrix_glucose[2:,:]