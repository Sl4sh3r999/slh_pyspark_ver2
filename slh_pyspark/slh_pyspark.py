def col_a_list(df, col):

    df_inter = df.select(f'{col}')
    df_inter = df_inter.dropDuplicates()
    n = df_inter.columns[0]
    row = df_inter.collect()
    s = str(row)
    s = s.replace('[', '').replace(']', '').replace(f'Row({n}=', '').replace(')', '').replace("'", "")
    ls = s.split(', ')

    return ls

def col_a_tupla(df, col):

    df_inter = df.select(f'{col}')
    df_inter = df_inter.dropDuplicates()
    n = df_inter.columns[0]
    row = df_inter.collect()
    s = str(row)
    s = s.replace('[', '').replace(']', '').replace(f'Row({n}=', '').replace(')', '').replace("'", "")
    tp = tuple(s.split(', '))

    return tp

def cols_para_sql_athena(schema_str):
    import re

    schema_str = schema_str.replace('-', '').replace('|', '').replace(':', '').replace(' (nullable = true)', ',')
    pattern = re.compile(r'(\w+)\s+string')
    result = re.sub(pattern, r'"\1" string', schema_str)

    return result