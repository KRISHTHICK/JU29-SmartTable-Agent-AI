smarttable-agent/
├── app.py                   # Streamlit UI
├── agent/
│   ├── table_reader.py      # Reads tables from Word
│   ├── pattern_finder.py    # Finds table structure patterns
│   └── human_review.py      # Allows human to accept/edit patterns
├── samples/
│   └── sample.docx          # Sample unstructured Word file
├── output/
│   ├── structured_tables.json
│   └── schema_patterns.json
├── requirements.txt
