import pyparsing as pp

greet = pp.Word(pp.alphas) + "," + pp.Word(pp.alphas) + "!"


hello = "Hello, World!"
print(hello, "->", greet.parseString(hello))

for greeting_str in [
            "Hello, World!",
            "Bonjour, Monde!",
            "Hola, Mundo!",
            "Hallo, Welt!",
        ]:
    # print(greet)
    greeting = greet.parseString(greeting_str)
    print(greeting)

greet2 = pp.Word(pp.alphas) + " " + pp.Word(pp.alphas)

str1 = "LASR 102 - ARTH 322 001 - 2021W2 on 4/7/2022 (Thu)"
str2 = "BUCH B313 - GRSJ 224B 002 - 2021W2 on 4/7/2022 (Thu)"

print(greet2.parseString())
