print("🎤 bem vindo ao quiz: qual música da olivia rodrigo você é?💜")

print("responda com a letra de cada alternativa A B ou C ")

get_him_back = 0
vampire = 0
pretty_isnt_pretty = 0

# primeira pergunta
print("  1️⃣  quando alguém te decepciona você...")
print("A) Finge que tá tudo bem mas guarda tudo por dentro")
print("B) Parte pra cima e resolve logo, sem enrolar")
print("C) Fica se comparando e se sentindo pior ainda")

resposta1 = input("sua resposta: ").lower()

if resposta1 == "a":
    vampire += 1
elif resposta1 == "b":
    get_him_back += 1
elif resposta1 == "c":
    pretty_isnt_pretty += 1

# segunda pergunta
print("  2️⃣  Quando você vê seu/sua ex com outra pessoa, você...") 
print("A) Finge que não liga, mas por dentro tá quebrando tudo")
print("B) Já pensa em um plano maquiavélico pra dar o troco")
print("C) Se olha no espelho e começa a se sentir insuficiente")

resposta2 = input("Sua resposta: ").lower()

if resposta2 == "a":
    vampire += 1
elif resposta2 == "b":
    get_him_back += 1
elif resposta2 == "c":
    pretty_isnt_pretty += 1
else:
    print("Resposta inválida. Responda com A, B ou C.")

# terceira pergunta
print("  3️⃣  Você está se sentindo triste, o que faz?")
print("A) Escreve no diário e ouve umas músicas tristes")
print("B) Manda textão no WhatsApp pra quem te deixou assim")
print("C) Se compara com as pessoas do Instagram por horas")

resposta3 = input("Sua resposta: ").lower()

if resposta3 == "a":
    vampire += 1
elif resposta3 == "b":
    get_him_back += 1
elif resposta3 == "c":
    pretty_isnt_pretty += 1
else:
    print("Resposta inválida. Responda com A, B ou C.")

# resultado final
print("\n🎶 Resultado final 🎶")

if vampire > get_him_back and vampire > pretty_isnt_pretty:
    print("Você é a música 'Vampire'! 🦇")
elif get_him_back > vampire and get_him_back > pretty_isnt_pretty:
    print("Você é a música 'Get Him Back'! 🔥")
elif pretty_isnt_pretty > vampire and pretty_isnt_pretty > get_him_back:
    print("Você é a música 'Pretty Isn't Pretty'! 💔")
else:
    print("Você tem uma vibe única, misturando todas as músicas! 💜")
