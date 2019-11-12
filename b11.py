"""
11.	Una modista, para realizar sus prendas de vestir, encarga las telas al extranjero. Para cada pedido,
tiene que proporcionar las medidas de la tela en pulgadas, pero ella generalmente las trabaja  en metros.
Realice un algoritmo para ayudar a resolver el problema, determinando cuántas pulgadas debe pedir
con base en los metros que requiere. Represéntelo mediante el diagrama de flujo y el pseudocódigo (1 pulgada = 0.0254 m).
"""
medida = float(input("Ingrese medidas de la tela en metros:"))
pulgadas = medida / 0.0254
print(f"Usted debe pedir {pulgadas} pulgadas de tela.")