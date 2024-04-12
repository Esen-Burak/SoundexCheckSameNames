def soundex(name):

    soundexCode = [' ', ' ', ' ', ' ']
    soundexCodeIndex = 1

    ########### ABCDEFGHIJKLMNOPQRSTUVWXYZ
    mappingNumbers = "01230120022455012623010202"

    soundexCode[0] = name[0].upper()

    for i in range(1, len(name)):

         c = ord(name[i].upper()) - 65

         if c >= 0 and c <= 25:

             if mappingNumbers[c] != '0':

                 if mappingNumbers[c] != soundexCode[soundexCodeIndex-1]:
                     soundexCode[soundexCodeIndex] = mappingNumbers[c]
                     soundexCodeIndex += 1

                 if soundexCodeIndex > 3:
                     break

    if soundexCodeIndex <= 3:
        while(soundexCodeIndex <= 3):
            soundexCode[soundexCodeIndex] = '0'
            soundexCodeIndex += 1

    return ''.join(soundexCode) 