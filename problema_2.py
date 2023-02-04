# Aluno: Akenathon Jamisse Barros Furtado

from sys import stdin
#from sys import exit

sufix_dict = {
    4:{"aist": ("futuro","2a pessoa")},
    3:{"ais":("futuro","2a pessoa"), "aem": ("futuro","4a pessoa"),"ons":("presenete","5a pessoa"), "est":("preterito","5a pessoa"),
    "aim": ("futuro","6a pessoa")},
    2:{"ei": ("preterito", "1a pessoa"), "ai": ("futuro","1a pessoa"), "os": ("presente", "2a pessoa"), "es": ("preterito","2a pessoa"),
    "om": ("presente","4a pessoa"), "em": ("preterito", "4a pessoa"), "am": ("presente","6a pessoa"),"im": ("preterito","6a pessoa")},
    1:{"o": ("presente","1a pessoa"), "a": ("presente", "3a pessoa"), "e": ("preterito","3a pessoa"), "i": ("futuro", "3a pessoa")}
}

def main():
#    stdin = open("entrada.in","r")

    while True:
        line = stdin.readline().strip()
        if line == "":
            break

        i = 4
        while i>0:
            if line[-4:] not in sufix_dict[4].keys() and line[-3:] not in sufix_dict[3].keys() and line[-2:] not in sufix_dict[2].keys() and line[-1] not in sufix_dict[1].keys():
                print(line + " - " + "não é um tempo verbal")
                break
            if line[-i:] in sufix_dict[i].keys():
                for x in sufix_dict[i].keys():
                    if x == line[-i:]:
                        master_key = x
                verbo = line[:-(len(master_key))] + "en"
                pessoa, tempo_verbal = (sufix_dict[i][master_key])
                print(line + " - " + "verbo " + verbo + ", " + pessoa + ", " + tempo_verbal)
                break
            elif line[-i:] in sufix_dict[i].keys():
                for x in sufix_dict[i].keys():
                    if x == line[-i:]:
                        master_key = x
                verbo = line[:-(len(master_key))] + "en"
                pessoa, tempo_verbal = (sufix_dict[i][master_key])
                print(line + " - " + "verbo " + verbo + ", " + pessoa + ", " + tempo_verbal)
                break
            elif line[-i:] in sufix_dict[i].keys():
                for x in sufix_dict[i].keys():
                    if x == line[-i:]:
                        master_key = x
                verbo = line[:-(len(master_key))] + "en"
                pessoa, tempo_verbal = (sufix_dict[i][master_key])
                print(line + " - " + "verbo " + verbo + ", " + pessoa + ", " + tempo_verbal)
                break
            elif line[-i] in sufix_dict[i].keys():
                for x in sufix_dict[i].keys():
                    if x == line[-i:]:
                        master_key = x
                verbo = line[:-(len(master_key))] + "en"
                pessoa, tempo_verbal = (sufix_dict[i][master_key])
                print(line + " - " + "verbo " + verbo + ", " + pessoa + ", " + tempo_verbal)
                break
            i -= 1
   
if __name__ == "__main__":
    main()