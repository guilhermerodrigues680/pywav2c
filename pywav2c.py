import wave
from time import sleep


audiowav = wave.open('dm3000.wav', mode='rb')


sample_rate = audiowav.getframerate()
aux1 = audiowav.getnframes()
aux = audiowav.getparams()

print(aux)

amostras = []
while True:
    sample = audiowav.readframes(1)
    
    if sample == b'':
        break
    else:
        inteiro = int.from_bytes(sample, byteorder='little', signed=False)
        # print(sample.hex())
        # print(inteiro)
        amostras.append(inteiro)

f = open("sounddata.h", "w")

cabecalho = '''// Wav2c recriado em Python3 por Guilherme Rodrigues: https://github.com/guilhermerodrigues680/py-wav2c
// Baseado no wav2c em C de Olle Jonsson: https://github.com/olleolleolle/wav2c\n
'''

# f.write("// Wav2c recriado em Python3 por Guilherme Rodrigues: https://github.com/guilhermerodrigues680/py-wav2c \n\n")
# f.write("// Baseado no wav2c em C de Olle Jonsson: https://github.com/olleolleolle/wav2c \n")
f.write(cabecalho)
f.write("const int sounddata_sampleRate = " + str(sample_rate) + "; \n")
f.write("const int sounddata_length = " + str(len(amostras)) + "; \n\n")
f.write("const unsigned char sounddata_data[] PROGMEM ={")

for idx, amostra in enumerate(amostras):
    
    if len(str(amostra)) == 1:
        f.write('  ')
    elif len(str(amostra)) == 2:
        f.write(' ')
    
    f.write(str(amostra))

    if (idx + 1) != len(amostras):
        
        if idx % 20 == 0:
            f.write(',\n')
        else:
            f.write(', ')

    else:
        f.write(" };\n")



f.close()  
print('Conversao finalizada')