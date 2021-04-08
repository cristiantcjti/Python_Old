import re

padrao1 = "[0123456789][0123456789][0123456789][0123456789][-][0123456789][0123456789][0123456789][0123456789]"
padrao2 = "[0-9]{4}[-][0-9]{4}"
padrao3 = "[0-9]{4,5}-[0-9]{4}"

# Vamos testar esse padrão.
texto =  "Meu número para contato é 2633-5723"
retorno1 = re.search(padrao1,texto)
retorno2 = re.search(padrao2,texto)
retorno3 = re.search(padrao3,texto)

print("Padrao1",retorno1.group())
print("Padrao2",retorno2.group())
print("Padrao3",retorno3.group())