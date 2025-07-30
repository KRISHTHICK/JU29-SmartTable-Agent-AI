import json

def save_structure(df, pattern, output_dir='output'):
    df.to_json(f"{output_dir}/structured_tables.json", orient='split')
    with open(f"{output_dir}/schema_patterns.json", "w") as f:
        json.dump(pattern, f, indent=4)
