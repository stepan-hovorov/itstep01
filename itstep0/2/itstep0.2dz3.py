phrase_1= input ("Введіть кодову фразу: ").strip()
print ("Перевіряємо: ", phrase_1)
phrase = phrase_1.upper()
rule_start = phrase.startswith("AGENT")
rule_end = phrase.endswith ("#")
rule_delta = phrase.find ("DELTA") != -1
rule_agent_count = phrase.count ("AGENT") == 1

if rule_start == True and rule_end == True and rule_delta == True:
    print ("Доступ дозволено")
else:
    print("Доступ заборонено")