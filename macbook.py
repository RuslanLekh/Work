import re

input_text = """
MacBook AIR
🔴MacBook Air 11" (2014) i5 4/128Gb Silver (MD711) - 190$
144 циклів
🔴MacBook Air 11" (2015) i5 4/128Gb Silver (MJVM2) - 200$
292 циклів

🔴MacBook Air 13" (2013) i5 4/128Gb Silver (MD760) - 220$
798 циклів
🔴MacBook Air 13" (2014) i5 4/128Gb Silver (MD760) - 220$
423 циклів
🔴MacBook Air 13" (2014) i5 4/128Gb Silver (MD760) - 210$
1053 циклів
🔴MacBook Air 13" (2015) i5 8/128Gb Silver (MMGF2) - 220$
1969 циклів
--------------------
MacBook PRO 
🔴MacBook Pro 13" (2013) i5 8/256Gb Space (ME865) - 320$
553 циклів
🔴MacBook Pro 13" (2015) i5 8/256Gb Silver (MF840) - 320$
 1011 циклів
🔴MacBook Pro 13" (2017) i5 8/128Gb Space (MPXQ2) - 400$
525 циклів
🔴MacBook Pro 13" (2020) i5 16/512Gb Silver (MWP72) - 780$
174 циклів
🔴MacBook Pro 13" (2022) M2 16/1Tb Silver (Z16S000ND) - 1330$
61 циклів
🔴 MacBook Air 13'' (2020) M1 8/256Gb Space (MGN63) - 750$ 
1 циклів

🔵MacBook Air 13'' (2020) M1 8/256Gb Space (MGN63) - 810$ 
3 циклів

"""

pattern = re.compile(r'🔴(MacBook (?:Air|Pro) \d{2}") \((\d{4})\) (i\d) (\d+/\d+Gb) (\w+) \((\w{5})\) - (\d+)\$(?:\s+(\d+ цикл[і|а]в?))?')

matches = pattern.findall(input_text)

for match in matches:
    model = match[0]
    year = match[1]
    processor = match[2]
    storage = match[3]
    color = match[4]
    identifier = match[5]
    price = int(match[6]) + 30  # Додавання 90 до ціни
    cycle_count = match[7] if match[7] else "Не вказано"

    print(f"💻 {price}$ - {model} ({year}) {processor} {storage} {color} ({identifier}) ({cycle_count})")
