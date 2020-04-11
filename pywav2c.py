import wave
import sys


def main(argv):
    
    if len(argv) < 3:
        print("Uso 1: python3 pywav2c.py <file.wav> <output.c> <soundname>")
        # print("Uso 2: python3 pywav2c.py <file.wav> <output.c> <soundname> <amount of samples>")
        sys.exit(0)

    FILE_IN = argv[0]
    FILE_OUT = argv[1]
    SOUND_NAME = argv[2]
    AUDIO_PARAMS = None
    amostras = []

    with wave.open(FILE_IN, mode='rb') as audiowav:
        AUDIO_PARAMS = audiowav.getparams()
        print(AUDIO_PARAMS)

        while True:
            sample = audiowav.readframes(1)
            
            if sample == b'':
                break
            
            inteiro = int.from_bytes(sample, byteorder='little', signed=False)
            amostras.append(inteiro)

    with open(FILE_OUT, "w") as f:
        
        cabecalho = (
            "// Wav2c recriado em Python3 por Guilherme Rodrigues: https://github.com/guilhermerodrigues680/py-wav2c\n"
            "// Baseado no wav2c em C de Olle Jonsson: https://github.com/olleolleolle/wav2c\n\n"
            "// const int " + str(SOUND_NAME) + "_sampleRate = " + str(AUDIO_PARAMS.framerate) + "; \n"
            "const int " + str(SOUND_NAME) + "_length = " + str(len(amostras)) + "; \n\n"
            "const unsigned char " + str(SOUND_NAME) + "_data[] PROGMEM ={"
        )

        f.write(cabecalho)

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
  
    print('-> Conversao finalizada')


if __name__ == "__main__":
    main(sys.argv[1:])
