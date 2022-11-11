import PyPDF2
from gtts import gTTS


language = 'es'
book = open('Un último respiro (GC).pdf', 'rb')
leer = '''Un último respiro

La mirada del joven se perdió en aquel momento en que su cabeza tocó el suelo. Una psicótica sonrisa sonó a su alrededor, tan bella, tan maligna. El joven muchacho sintió cada músculo fallecer, nada ni nadie podía detener el inminente final que se avecinaba. Una punzada de dolor en su cuello lo descolocó. Un insoportable dolor que quemaba su piel. Garras. Sentía su sangre brotar de la carne desgarrada, la misma esencia vital que emanaba formando un charco a su alrededor. El shock y el terror se apoderaron de él. El monstruo que lo atacó hablaba y reía pero no lograba entender ¿Cómo pudo ser que una niña fuera capaz de hacer tanto daño? La inocencia que irradiaba sólo era una máscara que escondía su verdadero rostro, un maldito rostro.
Ella acercó su cara hacia la suya, sus ojos que habían sido negros y brillantes como plumas de cuervo, se tornaron de un escalofriante color amarillo, la sonrisa suficientemente abierta para ver una hilera de dientes, cuyos colmillos afilados lo paralizaron de miedo. Lágrimas de desesperación surcaron su rostro mientras que el fétido aliento de la criatura invadía sus ya débiles fosas nasales. 
—Déjame ir...—susurró el muchacho al pequeño monstruo, pero ella no hacía más que sonreír como si fuese un juego para ambos. Negaba con la cabeza, su cabello rojo se mecía con el viento, sus ojos verdes brillaban en la penumbra. Levantó su mano. Con pavor observó cómo sus dedos se transformaban en unas pequeñas pero afiladas garras.
Comenzó a sollozar, el miedo a morir lo estaba dominando.'''
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
# speaker = gTTS()
page = pdfReader.getPage(0)
text = page.extractText()
tts = gTTS(leer, lang='es', tld='com.mx')
tts.save('Un último respiro.mp3')
#     speaker.runAndWait()