from sinais import Signal
import sympy as sp

funcoes_intervalos = []
while True:
    formula = input("Insira a formula do sinal(caso seja o final da descrição, digite 0): ");
    if formula != '0':
        formula_ind = sp.sympify(formula)

        inicio = float(input('Inicio do intervalo: '))
        fim = float(input('Fim do intervalo: '))

        funcoes_intervalos.append([formula_ind, [inicio, fim]])
    else:
        funcoes_intervalos.append('0')
        break

signal = Signal(funcoes_intervalos)

selected = False
while not selected:
    operation = input("Insira a operação a ser realizada: ");

    if operation == 'escalamento':
        parameter = int(input("Insira o parametro da operação: "))
        new_signal = signal.time_scaling(parameter)
        signal.plot('original.png')
        signal.plot_comparison(new_signal, 'Escalamento Temporal', 'escalamento_temporal.png')
        break

    if operation == 'reversao':
        new_signal = signal.reflection()
        signal.plot('original.png')
        signal.plot_comparison(new_signal, 'Reversão Temporal', 'reversao_temporal.png')
        break

    if operation == 'deslocamento':
        parameter = int(input("Insira o parametro da operação: "))
        new_signal = signal.time_shifting(parameter)
        signal.plot('original.png')
        signal.plot_comparison(new_signal, 'Deslocamento Temporal', 'deslocamento_temporal.png')
        break

    print("Operação inválida")
