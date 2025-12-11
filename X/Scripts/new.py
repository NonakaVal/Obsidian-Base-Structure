import csv

def csv_to_html(input_csv, output_html):
    items = []

    # Ler o CSV (uma coluna)
    with open(input_csv, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                valor = row[0].strip()
                if valor:
                    items.append(valor)

    # Construir HTML
    html_content = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<title>Lista de Subreddits</title>
<style>
body { font-family: Arial, sans-serif; padding: 20px; }
.item { margin-bottom: 10px; }
</style>
</head>
<body>
<h2>Lista Gerada A-Z subs</h2>
<form>
"""

    for valor in items:
        url = f"https://www.reddit.com/r/{valor}"
        html_content += f'''
<div class="item">
    <input type="checkbox" id="{valor}" name="{valor}">
    <label for="{valor}">
        <a href="{url}" target="_blank">{url}</a>
    </label>
</div>
'''

    html_content += """
</form>
</body>
</html>
"""

    # Salvar HTML
    with open(output_html, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"HTML gerado em: {output_html}")


# Exemplo de uso
if __name__ == "__main__":
    csv_to_html("input.csv", "output.html")
