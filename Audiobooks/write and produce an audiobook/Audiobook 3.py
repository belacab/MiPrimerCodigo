from gtts import gTTS

f = open('The Antigonish.txt', 'w')
f.write('''Yesterday, upon the stair,
I met a man who wasn't there!
He wasn't there again today,
Oh how I wish he'd go away!

When I came home last night at three
The man was waiting there for me
But when I looked around the hall,
I couldn't see him there at all!
Go away, go away, don't you come back any more!
Go away, go away, and please don't slam the door...

Last night I saw upon the stair,
A little man who wasn't there,
He wasn't there again today
Oh, how I wish he'd go away....''')
f.close()
f = open('The Antigonish.txt', 'r')
print(f.read())
language = 'en'
book = open('The Antigonish.txt', 'rb')
leer = ('''Yesterday, upon the stair,
I met a man who wasn't there!
He wasn't there again today,
Oh how I wish he'd go away!

When I came home last night at three
The man was waiting there for me
But when I looked around the hall,
I couldn't see him there at all!
Go away, go away, don't you come back any more!
Go away, go away, and please don't slam the door...

Last night I saw upon the stair,
A little man who wasn't there,
He wasn't there again today
Oh, how I wish he'd go away....''')
print(f.write)
tts = gTTS(leer, lang='en', tld='com')
tts.save('The Antigonish.mp3')
