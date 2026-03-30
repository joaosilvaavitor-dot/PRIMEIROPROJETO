#Consumo de energia da geladeira
#Autor: João Silva
#Entrada

nome = input("Geladeira: ")
potencia = float(input("200W: "))
horas_dia = float(input("19h: "))

# Processamento
consumo_mensal = (potencia * horas_dia * 30) / 1000

# Saída
print("\n--- Resultado ---")
print(f"Aparelho: {nome}")
print(f"Consumo mensal: {consumo_mensal:.2f} kWh")


