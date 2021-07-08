from beatnik import beatnik_stack
import re

#insert a part of text
text = '''
Sind Zeichen oder Programmierkenntnisse somit Texte, wenn Entscheidungsfindungen statt in Zusammenhang mit uns in einem größeren Kontext (also im System: Material) stehen?
He Hazardous
of we strong
follow bacteria walks
by town guy place
Er stand neben mir,
sprach er Sätze, dass nicht von mir versteht wurden.
bis übermorgen, blieben die Sätze mir im Gedächtnis.
fünf verschiedene Grammatiken, verwendente er.
Schritt für Schritt. Ohne jede vernünftige Struktur, gabe er mir.
Farbe, dass niemand viel findet, wurde gezeigt.
aus der und die
alle in alt
und das land schiß
sang der haß der flöhe für die hysterischen und ausgeschlossenen frauen
Of neighborhood reputation:
Doubted empty buses’ land  A very cold girl  Taxi of attempt
By Paris’ gestures
Man sagt, dass alle Übersetzungen nur für den Leser sind. Werke dienen nur der Hörerschaft, oder? Es gibt Werke, die dienen. Es gibt überdies Leben – das doppelsinnige Dichterische oder geheimnisvolle Bild. Es gilt: Wesentliche Übersetzer, das sind Dichter. Genug für den Augenblick, oder nicht? Darauf: translate!
sing walfisch! vorhin loesten anderswo dicke boote ihre anker.
Man sagt, dass alle Übersetzungen nur für den Leser sind. Genug, denn gegenüber gibt es eines Dichtung. tongue teilt doppelsinnig tongue teilt mutter tongue macht übel oder grundsätzlich nicht translate.
mit Körperflüssigkeiten verschwimmen mit Resilienz Poren mit Erderwärmung nicht sich.
'''


##This part of text is impliment in function "preprocess"
text=text.replace("ä","ae").replace("Ä","Ae").replace("ö","oe").replace("Ö","oe").replace("ü","ue").replace("Ü","ue")
remove_digits = str.maketrans('', '', '0123456789')
text = text.translate(remove_digits)
textt = re.sub(r'[^\w\s]','',text)
word = textt.split()
#####################################


VALUE = []
for i in word:
    value = beatnik.scrabble(i)
    VALUE.append(value)

beatnik_stack(word,VALUE,debug=False)
