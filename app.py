#Consumo de energia da geladeira
#Autor: João Silva
#Entrada

nome = input("Digite o nome do aparelho: ")
potencia = float(input("Potência (em watts): "))
horas_dia = float(input("Horas de uso por dia: "))

# Processamento
consumo_mensal = (potencia * horas_dia * 30) / 1000

# Saída
print("\n Consumo Estimado ")
print(f"Aparelho: {nome}")
print(f"Consumo mensal: {consumo_mensal:.2f} kWh")


