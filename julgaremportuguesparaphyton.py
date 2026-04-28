# Lista de opções para exibir ao usuário
opcoes = [
    "Shonen", "Shojo", "Seinen", "Josei", "Kodomomuke", "Isekai", "Tensei",
    "Romance", "Drama", "Comédia", "Ação", "Fantasia", "Ficção Científica",
    "Terror / Horror", "Mistério", "Slice of Life", "Esportes", "Comédia Romântica",
    "Ação Fantasia", "Drama Psicológico", "Gore", "Hentai", "Gore Hentai",
    "Rape Hentai", "Drama Hentai", "Comedy Hentai", "Terror Hentai", "Mecha",
    "Cyberpunk", "Sobrenatural", "Battle Royale", "Magical Girl", "Ecchi",
    "Harem", "Reverse Harem", "Psychological Thriller", "Dark Fantasy", "Dark Romance"
]

# Exibe todas as opções
for genero in opcoes:
    print(genero)

print("-" * 30)
print("Suba para cima para ver todas as opções")
escolhas = input("Escolha seu gênero favorito (a primeira letra deve ser maiúscula): ")

# Estrutura de decisão (if / elif / else)
if escolhas == "Shonen":
    print("Você é burro")
elif escolhas == "Shojo":
    print("Você é feliz")
elif escolhas == "Seinen":
    print("Você finge ser masculo")
elif escolhas == "Josei":
    print("Você gosta de ver homens galãs e ache seu anime superior a todos")
elif escolhas == "Kodomomuke":
    print("Você definitivamente não é criança mas vê do mesmo jeito")
elif escolhas == "Isekai":
    print("Você acha que iria se tornar fodão, mas só iria virar mendigo")
elif escolhas == "Tensei":
    print("Você ia nascer um normie e não ia virar um deus e NÃO ia fazer um harem")
elif escolhas == "Romance":
    print("eu te entendo...")
elif escolhas == "Drama":
    print("tu tem tempo livre, hein")
elif escolhas == "Comédia":
    print("tu gosta de ser feliz")
elif escolhas == "Ação":
    print("tu gosta de dopamina rápida")
elif escolhas == "Fantasia":
    print("ok...")
elif escolhas == "Ficção Científica":
    print("aceitavel")
elif escolhas == "Terror / Horror":
    print("tu gosta de ficar com medinho")
elif escolhas == "Mistério":
    print("aceitavel tbm...")
elif escolhas == "Slice of Life":
    print("tu não tem vida social e gosta de ver os outros sendo felizes... eu te entendo")
elif escolhas == "Esportes":
    print("G A Y... exceto se for anime de artes marciais")
elif escolhas == "Comédia Romântica":
    print("tu gosta de ver protagonistas virgens")
elif escolhas == "Ação Fantasia":
    print("tu gosta de dopamina viajada, ok")
elif escolhas == "Drama Psicológico":
    print("tu gosta de emoções 😊")
elif escolhas == "Gore":
    print("o que tem de errado com você?")
elif escolhas == "Hentai":
    print("tarado")
elif escolhas == "Gore Hentai":
    print("seu bosta, que porra é essa? 💀")
elif escolhas == "Rape Hentai":
    print("Você é sub-especie ☠️")
elif escolhas == "Drama Hentai":
    print("tu gosta de sentir emoções no ato?")
elif escolhas == "Comedy Hentai":
    print("estranho...")
elif escolhas == "Terror Hentai":
    print("tu é MUITOOO estranho")
elif escolhas == "Mecha":
    print("seu genero é uma bosta")
elif escolhas == "Cyberpunk":
    print("ok, futuro distante com tecnologias, ok")
elif escolhas == "Sobrenatural":
    print("ce gosta de coisas sobre-humanas")
elif escolhas == "Battle Royale":
    print("por que você veria isso? tipo, fortnite é gratis, cara 😐")
elif escolhas == "Magical Girl":
    print("Você é um pouco estranho, mas aceitavel")
elif escolhas == "Ecchi":
    print("sua mente é tão tarada quanto os fãs de Hentais e Harem")
elif escolhas == "Harem":
    print("você é solteiro e fede a cheetos. Sua mente é tão tarada quanto os fãs de Hentais e Ecchi")
elif escolhas == "Reverse Harem":
    print("TU GOSTA DE SE  P E N E T R A D O . E sua mente tambem é tarada")
elif escolhas == "Psychological Thriller":
    print("Você não existe")
elif escolhas == "Dark Fantasy":
    print("Você gosta de fantasia mas não quer ser chamado de criança.")
elif escolhas == "Dark Romance":
    print("Você é MUITOOOOOOOOOOOOOOOOOOOOOOOOOO estranho.")
else:
    print("gênero inexistente ou desconhecido")
