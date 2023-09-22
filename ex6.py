perguntas = ["é bolsonaro ou não é?",
             "o ceu é azul?",
             "faz o L?",
             "o céu é rosa",
             "leo lins é bala",
             "orgulho de ser sesi?",
             "cabo de santo agostinho é fim de mundo?",
             "biruleibileibe",
             "ai neymar"]

respostas = ["é",
             "tecnicamente sim",
             "FAZ O L",
             "não",
             "mto",
             "nem um pouco",
             "pra caramba",
             "a ti toma no",
             "gosta de bater né"]

x = 0 

for i in range(len(perguntas)):
    resposta = input(perguntas[i])
    if (resposta.lower() == respostas[i]):
        print('macaco esperto')  
        x = x + 1
    else:
       print("macaco burro")