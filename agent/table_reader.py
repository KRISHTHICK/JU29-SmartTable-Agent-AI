from docx import Document

def extract_tables_from_docx(file_path):
    doc = Document(file_path)
    all_tables = []

    for table in doc.tables:
        table_data = []
        for row in table.rows:
            row_data = [cell.text.strip() for cell in row.cells]
            table_data.append(row_data)
        all_tables.append(table_data)
    return all_tables
