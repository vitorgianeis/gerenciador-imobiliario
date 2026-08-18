
with open("pagina_imobiliaria.html", "w") as pagina:
    pagina.write("<body><h2>lista das liguagem de programaçao</h2>")
    pagina.write("<h3>lista que o usuario vai interagir:<h3>")

    # a linha abaixo cria uma linha
    pagina.write("<ul>")

    linguagem = ''

    while linguagem != 's' and linguagem != 's':
        linguagem = input("digite a linguagem de programaçao ou s para sair:")

        if linguagem !="S" and linguagem !="s":
            pagina.write(f"<li>{linguagem}</li>")

    pagina.write("</ul><boy>")
