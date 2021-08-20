import pyparsing as pp


parseFormat = pp.Word(pp.alphas) + pp.Word(pp.alphanums) + \
         '-' + pp.Word(pp.alphas) + pp.Word(pp.alphanums) + pp.Word(pp.nums) + \
         '-' + pp.Word(pp.alphanums) + pp.Word(pp.alphas) + pp.Word(pp.printables) + pp.Word(pp.printables)

str1 = "LASR 102 - ARTH 322 001 - 2021W2 on 4/7/2022 (Thu)"
str2 = "BUCH B313 - GRSJ 224B 002 - 2021W2 on 4/7/2022 (Thu)"

print(parseFormat.parseString(str1))
print(parseFormat.parseString(str2))
