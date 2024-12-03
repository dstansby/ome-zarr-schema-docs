from pathlib import Path

from json_schema_for_humans.generate import generate_from_filename, GenerationConfiguration

def get_version_index_html(*, version: str, schmea_fnames: list[Path]) -> str:
    schemas_list = "\n".join([f"<li><a href={p.name}>{p.stem}</a> </li>" for p in schmea_fnames])
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Overpass:300,400,600,800">
    <script src="https://code.jquery.com/jquery-3.4.1.min.js" integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo=" crossorigin="anonymous"></script>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
	<link rel="stylesheet" type="text/css" href="schema_doc.css">
    <script src="https://use.fontawesome.com/facf9fa52c.js"></script>
    <script src="schema_doc.min.js"></script>
    <meta charset="utf-8"/>


    <title>Verison {version}</title>
</head>
<body onload="anchorOnLoad();" id="root">

    <div class="breadcrumbs"></div> <h1>Version {version}</h1><br/>
    <ul>
    {schemas_list}
    </ul>
</body>
</html>
"""




if __name__ == "__main__":
    for version in ["0.4"]:
        version_output_path = Path(__file__).parent / version
        schema_path = Path(__file__).parent / "schemas" / version
        # TODO: download schemas from source
        for schema_file in schema_path.glob("*.schema"):
            print(schema_file)
            generate_from_filename(
                schema_file,
                result_file_name=version_output_path / schema_file.with_suffix(".html").name,
                config=GenerationConfiguration(template_name="js")
            )

        schema_fnames = [p for p in version_output_path.glob("*.html") if p.name != "index.html"]
        with open(version_output_path / "index.html", 'w') as f:
            f.write(get_version_index_html(version=version, schmea_fnames=schema_fnames))
