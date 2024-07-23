import re

input_text_watch = """
⌚️ 8 41 Silver (MP6L3) - 330$ (не актив)
⌚️ 8 45 Midnight (MNUL3) - 360$
⌚️ 8 45 Silver (MP6Q3) - 360$
⌚️ Ultra 49 Titanium Midnight (MQET3) - 650$
⌚️ 1 38 Rose (MNNH2) - 50$ A 
⌚️ 1 42 Silver SS (MJ3Y2) - 60$ A 
⌚️ 4 40 Space (MU662) - 100$ A-
⌚️ 4 44 Black SS (MTV52) - 150$ A-
⌚️ 4 44 Gold SS (MU6F2) - 180$ A- 
⌚️ 4 44 Silver (MU6A2) - 100$ A (пляма на екрані) 
⌚️ 6 44 Blue (M00J3) - 160$  B+ 
⌚️ 6 44 Space (M00H3) - 170$  A- 
⌚️ 7 45 Red (MKJC3) - 250$ A 
⌚️ 8 45 Midnight LTE (MNK43) - 320$ A 
⌚️ SE 44 Space (MKRR3) - 120$ A-
"""

pattern_watch = re.compile(r'⌚️\s*(.*?)\s*(\d+)\s*(\d+)\s*(\w*.*?)\s*\((\w+)\)\s*-\s*(\d+)\$\s*(\(.*\))?')

matches_watch = pattern_watch.findall(input_text_watch)

for match_watch in matches_watch:
    symbol_watch = "⌚️"
    model_watch = match_watch[0].strip()
    size_watch = match_watch[2]
    color_watch = match_watch[3]
    condition_watch = match_watch[4]
    identifier_watch = match_watch[5]
    
    if len(match_watch) > 6:
        try:
            price_watch = int(match_watch[6]) + 20  # Додаємо +20$ до ціни
        except ValueError:
            price_watch = None  # Якщо не можна перетворити в int, ігноруємо
        status_watch = match_watch[7].strip() if match_watch[7] else ""
    else:
        price_watch = None
        status_watch = ""

    if price_watch is not None:
        print(f"⌚️ {price_watch}$ - Apple Watch {model_watch} {size_watch}mm {color_watch} ({identifier_watch}) {status_watch}")
    else:
        print(f"⌚️ Не вдалося отримати ціну для Apple Watch {model_watch} {size_watch}mm {color_watch} ({identifier_watch}) {status_watch}")
