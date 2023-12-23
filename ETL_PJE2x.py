import re
from pathlib import Path

data_folder = Path("C:/Users/rdosa/source/repos/ETL_PJE2x/")
filename = data_folder / "extracao.txt"

pattern = r"^([0-9]{7})-([0-9]){2}\.([0-9]{4})\.([0-9]{1})\.([0-9]{2})\.([0-9]{4})$"

# Lista para armazenar todas as correspond�ncias encontradas
matches = []

# Abre o arquivo de entrada e procura por todas as correspond�ncias usando a codifica��o UTF-8
with open(filename, "r", encoding="utf-8", errors="ignore") as file:
    for line in file:
        # Encontra todas as correspond�ncias na linha
        line_matches = re.findall(pattern, line.strip())
        if line_matches:
            # Adiciona todas as correspond�ncias � lista
            formatted_matches = ['{}-{}.{}.{}.{}.{};'.format(*groups) for groups in line_matches]
            matches.extend(formatted_matches)
            # Imprime no terminal
            for formatted_match in formatted_matches:
                print(formatted_match)

# Salva o resultado no arquivo "resultado.txt"
with open(data_folder / "resultado.txt", "w", encoding="utf-8") as f:
    for item in matches:
        f.write("%s\n" % item)
