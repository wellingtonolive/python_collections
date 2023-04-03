from collections import Counter

texto1 = """
A linguagem Python está entre as 3 linguagens mais populares no mundo, segundo a pesquisa da RedMonk. Essa popularidade se dá principalmente por sua característica de exigir poucas linhas de código e permitir uma leitura fácil, além de ter várias bibliotecas do mundo de desenvolvimento web, Data Science, Machine Learning, automação e jogos.
Na Formação Python e orientação a objetos, você vai aprender a versão 3 dessa linguagem na prática, aplicando orientação a objetos em seu código e boas práticas de programação. Você também vai entender como tratamos erros e conhecer diversas funcionalidades para tratar os diferentes tipos de coleções. Veremos também como ler e escrever diferentes formatos de arquivos usando Python.
"""

texto2 = """
Por fim, vamos colocar tudo isso em prática para vermos algum exemplo diferente? Então o que eu queria fazer agora não é um contador de palavras, eu fazer um contador de letras para vermos uma coisa interessante que acontece na língua portuguesa e em outras línguas, para ser sincero, também. Então eu vou criar aqui uma nova sessão que é "#Testando o uso de diversas coleções".
Então o que vamos fazer é o seguinte: vamos pegar dois textos, por exemplo eu posso entrar no blog da Alura e pegar textos do blog da Alura. Eu posso pegar um texto que está falando sobre expressões regulares e posso pegar um outro texto de outro assunto, só para não termos dois assuntos similares. Vou pegar um o outro assunto, temos um de programação e um aqui que é de negócios: B2C, B2B, coisas do gênero. Então dois assuntos distintos, um de programação e um não de programação.
Então dois assuntos, dois textos. Vamos separar esses dois textos? Então vou copiar uma parte desse texto aqui, vou copiar três parágrafos. Vou copiar uns três parágrafos iniciais, então três aspas e três aspas para poder ter várias linhas, então no Python várias linhas, três parágrafos. Repara, eu não vou copiar o código, eu não quero o código, eu quero o texto em português, então vou copiar essas outras aqui, quatro parágrafos, que também é texto em português.Então eu quero copiar o texto em português sobre programação e mais um pouco aqui, copiar tudo isso. Então eu tenho um texto, que é um texto razoável, posso rodar, é um texto sobre programação e vou colocar um texto2 também, três aspas, Enter. E agora um texto sobre B2C, B2B, e por aí vai. Então vou pegar esse texto aqui, e olha, tem bastante texto, tem bastante texto mesmo. Não é programação, então vou copiar todo esse texto, porque não falou de programação. Copiei.
"""


def analise_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    total_caracteres = sum(aparicoes.values())

    print("Total de Caracterers")
    print(total_caracteres)

    proporcoes = [(letra, frequencia / total_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)

    for caractere, proporcao in mais_comuns:
        print("{} => {:.2f}%".format(caractere, proporcao*100))


analise_frequencia_de_letras(texto1)
analise_frequencia_de_letras(texto2)
