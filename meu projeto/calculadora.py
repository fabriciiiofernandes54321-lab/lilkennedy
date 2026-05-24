import re

def calcular(expressao):
    expressao = expressao.strip()
    expressao = expressao.replace(',', '.')
    expressao = expressao.replace('^', '**')
    expressao = expressao.replace('x', '*').replace('X', '*')

    if not re.match(r'^[\d\s\+\-\*\/\.\(\)\*\%]+$', expressao):
        return "Erro: expressão inválida"

    try:
        resultado = eval(expressao)
        if isinstance(resultado, float) and resultado.is_integer():
            return int(resultado)
        return round(resultado, 10)
    except ZeroDivisionError:
        return "Erro: divisão por zero"
    except Exception:
        return "Erro: não entendi essa expressão"

print("=" * 40)
print("       CALCULADORA DE TERMINAL")
print("  Digite 'sair' para encerrar")
print("  Operações: + - * / % ^ ( )")
print("=" * 40)

while True:
    try:
        entrada = input("\n>>> ")
        if entrada.lower() in ("sair", "exit", "q"):
            print("Até mais!")
            break
        if entrada.strip() == "":
            continue
        resultado = calcular(entrada)
        print(f"    = {resultado}")
    except KeyboardInterrupt:
        print("\nAté mais!")
        break
