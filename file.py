name = input("file name without extention")
#LOB19input
searched_part = "/ufi/reaction/profile/browser/?ft_ent_identifier="

f = open('name.txt', 'r')
adress = []
str = f.read()
while str.find(searched_part) > -1:
    begin = str.find(searched_part)+1
    end = str.find('"',begin+6)
    if adress.count(str[begin:end]) == 0:
        adress.append(str[begin:end])
     #   print(str[begin:end])
      #  input()
    str = str[end:]
print(adress)
f.close()
