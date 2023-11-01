def col_a_list(df, col):

    try:
        df_inter = df.select(f'{col}')
        df_inter = df_inter.dropDuplicates()
        n = df_inter.columns[0]
        row = df_inter.collect()
        s = str(row)
        s = s.replace('[', '').replace(']', '').replace(f'Row({n}=', '').replace(')', '').replace("'", "")
        ls = s.split(', ')
    except:
        print(f'Example:\nslh.col_a_list(Dataframe, "Colum_Name")')
        ls = None

    return ls

def col_a_tupla(df, col):

    try:
        df_inter = df.select(f'{col}')
        df_inter = df_inter.dropDuplicates()
        n = df_inter.columns[0]
        row = df_inter.collect()
        s = str(row)
        s = s.replace('[', '').replace(']', '').replace(f'Row({n}=', '').replace(')', '').replace("'", "")
        tp = tuple(s.split(', '))
    except:
        print(f'Example:\nslh.col_a_tupla(Dataframe, "Colum_Name")')
        tp = None

    return tp

def cols_para_sql_athena(esquema):

    print(f'Example:\nslh.cols_para_sql_athena(df.printSchema)\nImportant: do not use "()" at the end of DF funtion\n\n')

    estring = str(esquema)
    
    estring = estring.split('DataFrame[')[-1].split(']')[0]
    lineas = estring.split(', ')
    lineas = [linea.strip() for linea in lineas if linea.strip()]
    
    separacion = ',\n'.join(lineas)
    separacion = separacion.replace(':', '')
    
    try:
        separacion = separacion.replace('long', 'bigint')
    except:
        pass

    return separacion
