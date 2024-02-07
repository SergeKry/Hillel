chess_players = {
"Carlsen, Magnus": 1865,
"Firouzja, Alireza": 2804,
"Ding, Liren": 2799,
"Caruana, Fabiano": 1792,
"Nepomniachtchi, Ian": 2773
}
chess_players_reverse = {}
for k in chess_players:
    v = chess_players[k]
    if v > 2000:
        key_split = k.split(',')
        k = key_split[0]+key_split[1][:2]+'.'
        chess_players_reverse.update({v: k})
print(chess_players_reverse)
