import re

input_text_watch = """
 


New :
⌚️9 41 Starlight (MR8V3) - 390$

 Open Box :
⌚️9 45 Midnight (MR9A3) - 370$ (не актив)
⌚️9 45 Silver (MR9E3) - 360$
⌚️9 41 Midnight (MR8W3) - 340$ (не актив)
⌚️9 41 Starlight (MR8T3) - 340$ (не актив)
⌚️8 45 Silver (MP6Q3) - 310$
⌚️8 41 Silver (MP6L3) - 290$
⌚️SE2 44 Midnight (MRE93) - 240$ (не актив)

 USED :
⌚️1 38 Rose (MNNH2) - 40$ A 
⌚️1 42 Silver SS (MJ3Y2) - 50$ A 
⌚️4 44 Gold SS (MU6F2) - 180$ A- 
⌚️4 44 Silver (MU6A2) - 95$ A (пляма на екрані) 
⌚️6 44 Blue (M00J3) - 140$  B 
⌚️7 45 Red (MKJC3) - 220$ A 

"""

pattern_watch = re.compile(r'⌚️\s*(.*?)\s*(\d+)\s*(\d+)\s*(\w*.*?)\s*\((\w+)\)\s*-\s*(\d+)\$')

matches_watch = pattern_watch.findall(input_text_watch)

for match_watch in matches_watch:
    symbol_watch = "⌚️"
    model_watch = match_watch[0]
    size_watch = match_watch[2]
    color_watch = match_watch[3]
    identifier_watch = match_watch[4]
    price_watch = int(match_watch[5]) + 20  # Віднімаємо 20$ від ціни

    print(f"⌚️{price_watch}$ - Apple Watch {size_watch}'' {model_watch} {color_watch} ({identifier_watch})")
