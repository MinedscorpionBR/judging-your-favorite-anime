options = [
    "Shonen", "Shojo", "Seinen", "Josei", "Kodomomuke", "Isekai", "Tensei",
    "Romance", "Drama", "Comedy", "Action", "Fantasy", "Science Fiction",
    "Terror / Horror", "Mystery", "Slice of Life", "Sports", "Romantic Comedy",
    "Action Fantasy", "Psychological Drama", "Gore", "Hentai", "Gore Hentai",
    "Rape Hentai", "Drama Hentai", "Comedy Hentai", "Terror Hentai", "Mecha",
    "Cyberpunk", "Supernatural", "Battle Royale", "Magical Girl", "Ecchi",
    "Harem", "Reverse Harem", "Psychological Thriller", "Dark Fantasy", "Dark Romance"
]

# Displays all options
for genre in options:
    print(genre)

print("-" * 30)
print("Scroll up to see all options")
choice = input("Choose your favorite genre (the first letter must be capitalized): ")

# Decision structure (if / elif / else)
if choice == "Shonen":
    print("You are dumb")
elif choice == "Shojo":
    print("You are happy")
elif choice == "Seinen":
    print("You pretend to be manly")
elif choice == "Josei":
    print("You like watching handsome men and think your anime is superior to all others")
elif choice == "Kodomomuke":
    print("You are definitely not a kid but you watch it anyway")
elif choice == "Isekai":
    print("You think you'd become a badass, but you'd just end up a beggar")
elif choice == "Tensei":
    print("You'd be born a normie, wouldn't become a god, and WOULD NOT build a harem")
elif choice == "Romance":
    print("I understand you...")
elif choice == "Drama":
    print("you have a lot of free time, huh")
elif choice == "Comedy":
    print("you like being happy")
elif choice == "Action":
    print("you like fast dopamine")
elif choice == "Fantasy":
    print("ok...")
elif choice == "Science Fiction":
    print("acceptable")
elif choice == "Terror / Horror":
    print("you like getting a little scared")
elif choice == "Mystery":
    print("acceptable too...")
elif choice == "Slice of Life":
    print("you have no social life and like watching others be happy... I understand you")
elif choice == "Sports":
    print("G A Y... unless it's a martial arts anime")
elif choice == "Romantic Comedy":
    print("you like watching virgin protagonists")
elif choice == "Action Fantasy":
    print("you like trippy dopamine, ok")
elif choice == "Psychological Drama":
    print("you like emotions 😊")
elif choice == "Gore":
    print("what is wrong with you?")
elif choice == "Hentai":
    print("pervert")
elif choice == "Gore Hentai":
    print("you piece of shit, what the fuck is that? 💀")
elif choice == "Rape Hentai":
    print("You are a sub-species ☠️")
elif choice == "Drama Hentai":
    print("you like feeling emotions during the act?")
elif choice == "Comedy Hentai":
    print("weird...")
elif choice == "Terror Hentai":
    print("you are SOOOO weird")
elif choice == "Mecha":
    print("your genre is trash")
elif choice == "Cyberpunk":
    print("ok, distant future with technologies, ok")
elif choice == "Supernatural":
    print("you like superhuman things")
elif choice == "Battle Royale":
    print("why would you watch this? like, fortnite is free, man 😐")
elif choice == "Magical Girl":
    print("You're a bit weird, but acceptable")
elif choice == "Ecchi":
    print("your mind is as perverted as Hentai and Harem fans")
elif choice == "Harem":
    print("you are single and smell like cheetos. Your mind is as perverted as Hentai and Ecchi fans")
elif choice == "Reverse Harem":
    print("YOU LIKE GETTING  P E N E T R A T E D . And your mind is also perverted")
elif choice == "Psychological Thriller":
    print("You don't exist")
elif choice == "Dark Fantasy":
    print("You like fantasy but don't want to be called a kid.")
elif choice == "Dark Romance":
    print("You are SOOOOOOOOOOOOOOOOOOOOOOOOOO weird.")
else:
    print("non-existent or unknown genre")
