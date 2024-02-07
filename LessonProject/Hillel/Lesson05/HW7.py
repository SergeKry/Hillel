chess_players = {
"Carlsen, Magnus": 1865,
"Firouzja, Alireza": 2804,
"Ding, Liren": 2799,
"Caruana, Fabiano": 1792,
"Nepomniachtchi, Ian": 2773
}
new_chess_players = {}
for k in chess_players:
    v = chess_players[k]
    if v > 2000:
        key_split = k.split(',')
        k = key_split[0]+key_split[1][:2]+'.'
        new_chess_players.update({v: k})
print(new_chess_players)
