anuncio = input().split()
dicionario_anuncio = dict()
lista_pontuação = [",", "."]            
lista_endereço = ["Rua", "Avenida"]     
endereço = []                           
lista_frases=[]                         
count=0
for i in anuncio:
    if '.'==i[len(i)-1]:                
        indice= anuncio.index (i)
        lista_frases.append (anuncio [count:indice+1])  
        count=indice+1
indice=0
nome= []
nome_final= []
dicionario_frequencia= dict ()
frase_final= lista_frases[len(lista_frases)-1]
for c in frase_final:
    if c not in dicionario_frequencia:
        dicionario_frequencia[c]=1    
    else:
        dicionario_frequencia[c]+=1
while indice<len(frase_final)-1:
    if frase_final[indice][0].isupper() and frase_final[indice+1][0].isupper():
        if frase_final[indice] not in nome:
            nome.append(frase_final[indice])
        elif dicionario_frequencia[frase_final[indice]]>1:
            nome.append (frase_final[indice])
            dicionario_frequencia[frase_final[indice]]-=1
        if frase_final [indice+1] not in nome:
            nome.append (frase_final[indice+1])
        elif dicionario_frequencia[frase_final[indice+1]]>1:
            nome.append (frase_final[indice+1])
            dicionario_frequencia[frase_final[indice+1]]-=1
    indice+=1
for i in nome:
    if 'Responsavel' not in dicionario_anuncio:
        if '.'==i[len(i)-1] or ','==i[len(i)-1]:
            dicionario_anuncio['Responsavel']=i [:len(i)-1]
        else:
            dicionario_anuncio['Responsavel']=i 
    else:
        if '.'==i[len(i)-1] or ','==i[len(i)-1]:
            dicionario_anuncio['Responsavel']+=' '+ i [:len(i)-1]
        else:
            dicionario_anuncio['Responsavel']+=' ' + i 
for c in anuncio:
    if c in lista_endereço:
        indice_endereço = anuncio.index(c)
while True:
    tamanho = len(anuncio[indice_endereço]) - 1
    if anuncio[indice_endereço][tamanho] in lista_pontuação:
        string_nova = anuncio[indice_endereço][:tamanho]
        if string_nova.isnumeric():
            endereço.append(string_nova)
            break
        else:
            endereço.append(anuncio[indice_endereço])
    else:
        if anuncio[indice_endereço].isnumeric():
            endereço.append(anuncio[indice_endereço])
            break
        else:
            endereço.append(anuncio[indice_endereço])
    indice_endereço += 1
for c in endereço:
    if "Endereco" not in dicionario_anuncio:
        dicionario_anuncio['Endereco']= c
    else:
        dicionario_anuncio['Endereco']+= " " + c
for c in anuncio:
    if ","== c[len(c)-1]:
        tamanho_fatia = len(c) - 1
        indice = anuncio.index(c)
        anuncio[indice] = c[:tamanho_fatia]
    elif "."==c[len(c)-1]:
        tamanho_fatia = len(c) - 1
        indice = anuncio.index(c)
        anuncio[indice] = c[:tamanho_fatia]
lista_area = ["m2.", "metros", "m2", "m2,"]
for c in anuncio:
    if c in lista_area:
        indice = anuncio.index(c)
        dicionario_anuncio["Area"] = int(anuncio[indice - 1])
lista_valor = ["R$", "reais"]
for c in anuncio:
    indice = anuncio.index(c)
    for i in lista_valor:
        if i in c:
            if i == "R$":
                dicionario_anuncio["Valor"] = c[2:]
            else:
                dicionario_anuncio["Valor"] = anuncio[indice - 1]
lista_aluguel = ["alugo", "alugar", "aluguel", "Alugo", "Alugar", "Aluguel"]
lista_venda = ["vendo", "vender", "venda", "Vendo", "Vender", "Venda"]
for i in lista_aluguel:
    if i in anuncio:
        dicionario_anuncio["Modalidade"] = "Aluguel"
for i in lista_venda:
    if i in anuncio:
        dicionario_anuncio["Modalidade"] = "Venda"
lista_casa = ["casa", "Casa"]
lista_apartamento = ["apartamento", "Apartamento"]
for i in lista_casa:
    if i in anuncio:
        dicionario_anuncio["Tipo"] = "Casa"
for i in lista_apartamento:
    if i in anuncio:
        dicionario_anuncio["Tipo"] = "Apartamento"
count_num = 0
count_tel=0
for c in anuncio:
    for i in c:
        if i.isnumeric():
            count_num += 1
    if count_num > 0:
        if "-" in c:
            indice = c.index("-")
            if len(c) - (indice + 1) == 3:
                dicionario_anuncio["CEP"] = c
            elif len(c) - (indice + 1) == 4:
                if "Telefone" not in dicionario_anuncio:
                    dicionario_anuncio["Telefone"] = c
                    count_tel+=1
                else:
                    dicionario_anuncio["Telefones"] = dicionario_anuncio["Telefone"]+", " + c
                    count_tel+=1
if "Area" not in dicionario_anuncio:
    dicionario_anuncio["Area"] = "nao informado"
if "Valor" not in dicionario_anuncio:
    dicionario_anuncio["Valor"] = "nao informado"
if "CEP" not in dicionario_anuncio:
    dicionario_anuncio["CEP"] = "nao informado"
if count_tel==1:
    lista_ordem = ["Modalidade", "Tipo", "Endereco", "CEP", "Area", "Valor", "Telefone","Responsavel"]
else:
    lista_ordem = ["Modalidade", "Tipo", "Endereco", "CEP", "Area", "Valor", "Telefones","Responsavel"]
for c in lista_ordem:
    print(c + ":", dicionario_anuncio[c])