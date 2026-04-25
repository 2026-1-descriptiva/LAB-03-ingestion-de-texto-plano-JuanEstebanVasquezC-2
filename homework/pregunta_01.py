"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    with open('files/input/clusters_report.txt') as file:
        first = file.readline().strip()
        second = file.readline().strip()
        aditionals = second.split("  ")

        col = first.split("  ")
        col = [s for s in col if s]
        col[1] = col[1]+" "+aditionals[0]
        col[2] = col[2]+" "+aditionals[1]
        col = [c.lower().strip().replace(' ','_') for c in col]

        master = []
        mark = True
        for line in file.readlines()[2:]:
            record = line.strip().split("  ")
            record = [r for r in record if r]
            if mark:
                c1, c2, c3, *c4 = record
                record = [c1,c2,c3," ".join(c4)]
                master.append(record)
                mark = False
            else:
                if record:
                    master[-1][-1] = master[-1][-1] + " "+" ".join(record)
                else:
                    mark = True
        
        df = pd.DataFrame(master,columns=col)
        df['cluster'] = df["cluster"].astype(int)
        df['cantidad_de_palabras_clave'] = df["cantidad_de_palabras_clave"].astype(int)
        df['porcentaje_de_palabras_clave'] = df['porcentaje_de_palabras_clave'].str.replace(' %','').str.replace(',','.').astype(float)
        df['principales_palabras_clave'] = df['principales_palabras_clave'].str.split(',')
        df['principales_palabras_clave'] = df['principales_palabras_clave'].apply(lambda x: [' '.join(p.split()) for p in x])
        df['principales_palabras_clave'] = df['principales_palabras_clave'].apply(lambda x: ', '.join([r.strip() for r in x]))
        df['principales_palabras_clave'] = df['principales_palabras_clave'].str.rstrip('.')

        return df

print(pregunta_01())



