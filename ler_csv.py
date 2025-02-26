from src.interface.classes.csv_class import CsvProcessor

arquivo_csv = "exemplo.csv"
filtro = "estado"
limite = "SP"

csv = CsvProcessor(arquivo_csv)
csv.carregar_csv()
print(csv.filtrar_por(["estado", "preco"],["SP","18,90"]))