#przyklad5-rozklad.py

sentence = "i ogólnie wtedy pomyślałem, że ogólnie mógłbym się napić ogólnie jakiegoś napoju"

parts = sentence.split("ogólnie")

print(type(parts))
print(parts)                   
print("generalnie".join(parts))
