#function for converting cyrillic to latin
def cir_to_lat(c_str):


    cir =['а','б','в','г','д','ђ','е','ж','з','и','ј','к','л','љ',\
         'м','н','њ','о','п','р','с','т','ћ','у','ф','х','ц','ч','џ','ш',\
         'А','Б','В','Г','Д','Ђ','Е','Ж','З','И','Ј','К','Л','Љ','М',\
         'Н','Њ','О','П','Р','С','Т','Ћ','У','Ф','Х','Ц','Ч','Џ','Ш']

    lat = ['a','b','v','g','d','đ','e','ž','z','i','j','k','l','lj','m',\
         'n','nj','o','p','r','s','t','ć','u','f','h','c','č','dž','š',\
        'A','B','V','G','D','Đ','E','Ž','Z','I','J','K','L','LJ','M','N',\
         'NJ','O','P','R','S','T','Ć','U','F','H','C','Č','DŽ','Š']
    cir_lat ={}
    for c,l in zip(cir,lat):
        cir_lat[c]=l


    nes = []

    for s in str(c_str):
        if s in cir:

            nes.append(s.replace(s,cir_lat[s]))
        else:
            nes.append(s)
    k = ''
    return k.join(nes)
