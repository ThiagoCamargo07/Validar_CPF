#Validando CPF

from validate_docbr import CPF,CNPJ

cpf = CPF()

numero= input("Digite seu CPF:")

if cpf.validate(numero):
    print("CPF valido ✅")
else:
    print("CPF inválido ❌")
    
    

cnpj = CNPJ()

numero= input("Digite seu CNPJ:")

if cnpj.validate(numero):
    print("CNPJ valido ✅")
else:
    print("CNPJ inválido ❌")