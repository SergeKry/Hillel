chess_players = {
"Carlsen, Magnus": 1865,
"Firouzja, Alireza": 2804,
"Ding, Liren": 2799,
"Caruana, Fabiano": 1792,
"Nepomniachtchi, Ian": 2773
}

new_chess_players = {v: k.split(',')[0]+k.split(',')[1][:2]+'.' for k, v in chess_players.items() if v > 2000}
print(new_chess_players)
