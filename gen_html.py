from pathlib import Path

from json_schema_for_humans.generate import generate_from_filename

if __name__ == "__main__":
    schema_path = Path(__file__).parent / "schemas" / "0.4"
    # TODO: download schemas from source
    for schema_file in schema_path.glob("*.schema"):
        print(schema_file)
        generate_from_filename(schema_file, result_file_name=Path(__file__).parent / "0.4" / schema_file.with_suffix(".html").name)
