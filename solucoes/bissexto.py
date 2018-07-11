ano = int( input( "Ano: " ) )

if ano % 400 == 0:
    print("É bissexto!")
elif ano % 100 == 0:
    print("Não é bissexto!")
elif ano % 4 == 0:
    print("É bissexto!")
else:
    print("Não é bissexto!")

print("Fim!")
