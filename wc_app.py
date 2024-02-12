#wordcloud simple app endrinendring
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
from wordcloud import WordCloud


st.set_page_config(layout='wide')

text = st.text_area('sett in tekst her: ', value='''Det solfylte sommerbildet med brudefølget i båtene, stavkirken på odden og vestlands- naturen med fjord og fjell er et typisk uttrykk for nasjonalromantikkens opplevelse av norsk natur og folkeliv. Kunstnerne spilte en vesentlig rolle når det gjaldt å definere en nasjonal egenart etter at Norge hadde fått sin grunnlov i 1814. Dette motivet, som så sterkt uttrykker 1800-tallets skjønnhetsidealer, har vært dyrket som et ”ikon” av generasjoner av nordmenn. Maleriet har vært overført til teaterscenen både som levende tablå og ballett, og motivet er blitt ledsaget av dikt og musikk.

#Gjennom grafiske reproduksjoner fikk Brudeferd i Hardanger stor utbredelse, og på grunn av motivets spesielle popularitet har kunstnerne utført maleriet i flere versjoner. Adolph Tidemand var den første norske kunstner som slo seg ned i Düsseldorf. Sin ambisjon om å bli historiemaler oppga han for å bli folkelivsskildrer. Men Tidemand gir en ny verdighet til bøndene, og dikteren Bjørnstjerne Bjørnson skal ha sagt at uten Tidemands malerier hadde han ikke kunnet skrive sine bondefortellinger.

#Landskapsmaler Hans Gude, som var drøye ti år yngre enn Tidemand, presenterer her som 23-åring en storslagen skildring av norsk natur. Selv om det ikke dreier seg om en direkte gjengivelse av et bestemt landskap, er komposisjonen satt sammen av nøyaktige naturobservasjoner fra forskjellige steder i hjemlandet. Tidemand og Gude har utført flere malerier sammen, der alle motivene viser folk som er ute i båt.''')


st.write('''**Ordsky for teksten**''') 
wordcloud= WordCloud(collocations=True, min_word_length=3, width=800, height=800, background_color='white').generate(text)
fig, ax = plt.subplots(figsize = (12, 8))
ax.imshow(wordcloud)
plt.axis("off")
st.pyplot(fig)
