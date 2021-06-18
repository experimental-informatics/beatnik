import beatnik
import re

#insert a part of text
text = '''
He arrived.

He arrived at my door extremely late one day.

If you only did uninteresting, idle things in your life, always acting as if nothing he does will change your opinion ... can go well.

But one awful dilemma I face, is that growing emotion ruins my serious, careful way of thinking. If a love flame is forced and futile, why bother kindling another one?

Yet, you think, it might not be a bad idea. Relationships always work out, and this can be an escape from a tense, complex life. Unmarried at home, lost in a loud, irregular reality ... maybe sometime, just maybe, it's time I found the one.

If he's a guy who is faithful, kind, and will be mine joyously to the end, I will prove to him I shall cherish and treasure him just as much. But how do I say it? I can't place the words...

"You absolutely need to know", I say, nervously, "that I...I...I..."
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

beatnik.stack(word,VALUE,debug=False)
