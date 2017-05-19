# wrappersinaica
## Es para sacar información de las estaciones de monitoreo de calidad del aire.

               https://pacific-garden-86188.herokuapp.com/estacion?estacion=144&Fecha=2017-03-08&parametro=CO&rango=4

## estación puede ser :
range(1,340)
esta lista son las probadas por mi:

[31, 33, 38, 39, 46, 47, 53, 56, 58, 59, 60, 65, 69, 70, 76, 77, 78, 82, 84, 90, 92, 96, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 123, 125, 127, 131, 137, 139, 141, 145, 147, 171, 174, 234, 236, 242, 244, 245, 247, 248, 249, 250, 251, 252, 256, 258, 259, 260, 261, 262, 263, 265, 266, 267, 268, 269, 270, 271, 291, 292, 297, 303, 304, 305, 306]


## Fecha es la fecha inicial para sacar información : YYYY-MM-DD

## Parámetro es el contaminante puede ser cualquiera de los siguientes :
[O3, NOX, NOx, NO, NO2, SO2, HCT, CH4, HDM, H2S, VV, TMP, PB, PP, CO, PM10, PM2.5, PST, DV, HR, RS, IUV, UVA, UVB]

*No todas las estaciones tienen todas las mediciones.

## rango está en semanas: puede ser:
[1, 2, 3, 4]
