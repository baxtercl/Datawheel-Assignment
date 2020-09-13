Se obtienen los datos desde el sitio:
https://www2.census.gov/programs-surveys/acs/data/pums/2018/1-Year/

Los archivos con csv_h[xx].zip, corresponden a Households (Hogares)

Los archivos con csv_p[xx].zip, corresponden a Populations (Poblaciones)
[xx] = Abreviación del nombre del estado

Link: https://www2.census.gov/programs-surveys/acs/data/pums/2018/1-Year/PUMS_file_naming_convention.pdf

Link: https://www2.census.gov/programs-surveys/acs/tech_docs/pums/data_dict/PUMS_Data_Dictionary_2018.pdf?#


Los datos utilizados para este caso, fueron de los csv de poblaciones (ver arriba), los cuales contenían la información de los Estados y también un monto asignado a salario.

STATE = ST

SALARY = WAGP


El archivo importardata.py, recorre todos los csv y guarda la información de Estado y Salario en el archivo data.csv. Por otra parte, el archivo salaries.py, lo que hace es leer el archivo data.csv y generar un resumen por Estado, para luego guardar la información obtenida en salaries.csv.
