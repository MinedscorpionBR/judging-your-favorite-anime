sentakushi = [
    "Shonen", "Shojo", "Seinen", "Josei", "Kodomomuke", "Isekai", "Tensei",
    "Romansu", "Dorama", "Komedi", "Akushon", "Fantaji", "SF",
    "Hora", "Misuteri", "Nichijo-kei", "Supotsu", "Rabu Kome",
    "Akushon Fantaji", "Saiko Dorama", "Guro", "Hentai", "Guro Hentai",
    "Reipu Hentai", "Dorama Hentai", "Komedi Hentai", "Hora Hentai", "Mecha",
    "Saibapanku", "Cho-shizen", "Batoru Rowaiyaru", "Maho Shojo", "Ecchi",
    "Haremu", "Gyaku Haremu", "Saiko Surira", "Daku Fantaji", "Daku Romansu"
]

# すべての選択肢を表示する
for janru in sentakushi:
    print(janru)

print("-" * 30)
print("すべての選択肢を見るには上にスクロールしてください")
erabi = input("好きなジャンルを選んでください（最初の文字は大文字にしてください）: ")

# 決定構造 (if / elif / else)
if erabi == "Shonen":
    print("お前はバカだ")
elif erabi == "Shojo":
    print("お前は幸せ者だな")
elif erabi == "Seinen":
    print("男らしいフリをしてるだけだろ")
elif erabi == "Josei":
    print("イケメンを見るのが好きで、自分のアニメが一番だと思ってるだろ")
elif erabi == "Kodomomuke":
    print("絶対に子供じゃないのに、とにかく見てるよな")
elif erabi == "Isekai":
    print("最強になれると思ってるかもしれないが、ただのホームレスになるだけだぞ")
elif erabi == "Tensei":
    print("凡人として生まれて神にもなれないし、ハーレムなんて絶対に作れないからな")
elif erabi == "Romansu":
    print("わかるよ…")
elif erabi == "Dorama":
    print("暇人だな")
elif erabi == "Komedi":
    print("幸せになるのが好きなんだな")
elif erabi == "Akushon":
    print("手っ取り早いドーパミンが好きなんだろ")
elif erabi == "Fantaji":
    print("そっか…")
elif erabi == "SF":
    print("許容範囲だな")
elif erabi == "Hora":
    print("ちょっとビビるのが好きなんだな")
elif erabi == "Misuteri":
    print("これも許容範囲だな…")
elif erabi == "Nichijo-kei":
    print("社会生活がなくて、他人が幸せなのを見るのが好きなんだな… わかるよ")
elif erabi == "Supotsu":
    print("ゲ イ だ な… 格闘技アニメなら別だが")
elif erabi == "Rabu Kome":
    print("童貞の主人公を見るのが好きなんだろ")
elif erabi == "Akushon Fantaji":
    print("トリップしたドーパミンが好きなんだな、オーケー")
elif erabi == "Saiko Dorama":
    print("感情が揺さぶられるのが好きなんだな 😊")
elif erabi == "Guro":
    print("お前、頭おかしいんじゃないのか？")
elif erabi == "Hentai":
    print("変態野郎")
elif erabi == "Guro Hentai":
    print("このクソ野郎、一体なんだそれは？ 💀")
elif erabi == "Reipu Hentai":
    print("お前は亜種（クズ）だ ☠️")
elif erabi == "Dorama Hentai":
    print("行為中に感情を感じたいのか？")
elif erabi == "Komedi Hentai":
    print("キモいな…")
elif erabi == "Hora Hentai":
    print("お前、マジでキモいぞ")
elif erabi == "Mecha":
    print("お前のジャンルはゴミだ")
elif erabi == "Saibapanku":
    print("はいはい、遠い未来のテクノロジーね、はいはい")
elif erabi == "Cho-shizen":
    print("人間離れしたものが好きなんだな")
elif erabi == "Batoru Rowaiyaru":
    print("なんでこんなの見るんだ？フォートナイトは無料だぞ、お前 😐")
elif erabi == "Maho Shojo":
    print("ちょっとキモいけど、まあ許容範囲だな")
elif erabi == "Ecchi":
    print("お前の頭の中は、ヘンタイやハーレムのファンと同じくらい変態だぞ")
elif erabi == "Haremu":
    print("お前は独り身でチートスの匂いがするな。頭の中はヘンタイやエッチのファンと同じくらい変態だ")
elif erabi == "Gyaku Haremu":
    print("お前、挿 入 さ れ る の が 好 き だ ろ。そして頭の中も変態だ")
elif erabi == "Saiko Surira":
    print("お前は存在しない")
elif erabi == "Daku Fantaji":
    print("ファンタジーは好きだけど、子供扱いされたくないんだろ。")
elif erabi == "Daku Romansu":
    print("お前は超絶怒涛にキモすぎるぞ。")
else:
    print("存在しない、または未知のジャンル")
