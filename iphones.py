import re

input_text = """

📲14 Pro 128 Space Black 100% - 760$ (A+) e-sim
📲14 Pro 128 Space Black 100% - 750$ (A) e-sim
📲14 Pro 128 Deep Purple 90% - 760$ (A) sim
📲14 Pro 128 Deep Purple 93% - 760$ (A) e-sim
📲14 Pro 128 Silver 87% - 730$ (A) sim

"""

pattern = re.compile(r'📲([\w\s]+) (\d+Gb|\d+|\w+) (\w+).*?(\d+%).*?(\d+\$) (\w*)')

matches = pattern.findall(input_text)

for match in reversed(matches):
    symbol = "📲"
    model = match[0].strip()
    memory = match[1]
    color = match[2]
    condition = match[3]
    price = int(match[4].replace('$', '')) + 20  # Додаємо +20$ до ціни
    status = match[5].strip()

    print (f"📲 {price}$ - iPhone {model} {memory} {color} {condition} ")
    


