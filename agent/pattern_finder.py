import pandas as pd

def find_table_pattern(table_data):
    df = pd.DataFrame(table_data)
    pattern = {
        "shape": df.shape,
        "has_header": True if df.iloc[0].nunique() == df.shape[1] else False,
        "merged_cells_possible": any("" in cell for row in table_data for cell in row),
        "empty_cells": sum(cell == "" for row in table_data for cell in row)
    }
    return pattern, df
