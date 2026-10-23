"""Simulação dos cinco níveis de água de um reservatório."""

from colorama import Fore, Style, init


def definir_cor(nivel):
    """Retorna a cor correspondente a um nível inteiro de 1 a 5."""
    if type(nivel) is not int or not 1 <= nivel <= 5:
        raise ValueError("O nível deve ser um número inteiro entre 1 e 5.")

    cores = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE]
    # A lista começa no índice zero; os níveis começam em 1.
    return cores[nivel - 1]


def exibir_situacao(nivel):
    """Mostra a situação atual e restaura o estilo do terminal."""
    situacoes = [
        "Muito baixo (crítico)",
        "Baixo",
        "Médio",
        "Alto",
        "Muito alto (alerta)",
    ]

    # A função também valida o nível antes de acessar a lista.
    cor = definir_cor(nivel)
    mensagem = f"Nível {nivel}: {situacoes[nivel - 1]}"
    print(cor + mensagem + Style.RESET_ALL)


def main():
    """Executa uma simulação sem solicitar entrada do usuário."""
    # Prepara as cores, inclusive em terminais Windows compatíveis.
    init()
    print("CONTROLE DE NÍVEIS DE ÁGUA")
    print("Simulação: cada linha representa uma leitura do reservatório.\n")

    niveis = [1, 2, 3, 4, 5]
    for nivel_atual in niveis:
        exibir_situacao(nivel_atual)


if __name__ == "__main__":
    main()
