import re

def виправити_помилки_в_тексті(текст):
    # Визначаємо регулярний вираз для виявлення помилок
    регулярка = re.compile(r'(\d+)\s+(\d+)%')
    
    # Замінюємо помилки в тексті
    виправлений_текст = регулярка.sub(r'\1\2%', текст)
    
    return виправлений_текст

# Приклад використання
початковий_текст = """
📲 165$ - iPhone X 64 Silver 7 5% 
📲 165$ - iPhone X 64 Silver 7 7% 
📲 165$ - iPhone X 64 Silver 7 4%
📲 165$ - iPhone X 64 Silver 7 2%
📲 195$ - iPhone XR 64 Black 8 8%
📲 195$ - iPhone XR 64 Black 8 8%
📲 220$ - iPhone XR 128 Red 8 1%
📲 220$ - iPhone Xs 64 Silver 10 0%
📲 320$ - iPhone Xs Max 512 Silver 10 0%
📲 190$ - iPhone SE2 128 White 10 0%
📲 245$ - iPhone 11 64 Black 9 2%
📲 250$ - iPhone 11 64 Black 9 4%
📲 290$ - iPhone 11 128 Black 10 0%
📲 300$ - iPhone 11 Pro 64 Gold 10 0%
📲 300$ - iPhone 11 Pro Max 64 Gold 7 6%
📲 240$ - iPhone 12 mini 128 Red 8 5%
📲 270$ - iPhone 12 64 Blue 8 5%
📲 270$ - iPhone 12 64 Black 9 9%
📲 360$ - iPhone 12 128 White 8 9%
📲 430$ - iPhone 12 Pro 128 Blue 8 9%
📲 430$ - iPhone 12 Pro 128 Graphite 8 5%
📲 430$ - iPhone 12 Pro 128 Graphite 9 0%
📲 520$ - iPhone 12 Pro Max 128 Silver 8 6%
📲 510$ - iPhone 12 Pro Max 128 Blue 8 3%
📲 430$ - iPhone 13 mini 128 Pink 8 5%
📲 430$ - iPhone 13 128Gb Red 8 3%
📲 570$ - iPhone 13 Pro 128 Sierra Blue 8 8%
📲 750$ - iPhone 13 Pro Max 256 Sierra Blue 8 4%
📲 730$ - iPhone 13 Pro Max 256 Graphite 8 9%
📲 580$ - iPhone 14 128 Purple 8 8%
📲 590$ - iPhone 14 Plus 128 Midnight 9 2%
📲 830$ - iPhone 14 Pro 256 Space Black 8 7%
📲 870$ - iPhone 14 Pro Max 128 Gold 8 7%
📲 940$ - iPhone 14 Pro Max 128 Space Black 9 9%
📲 900$ - iPhone 14 Pro Max 256 Deep Purple 8 8%
📲 710$ - iPhone 15 128 Blue 10 0%
"""
виправлений_текст = виправити_помилки_в_тексті(початковий_текст)

print(f"Виправлений текст: {виправлений_текст}")
