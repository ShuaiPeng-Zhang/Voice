import pyttsx3

# str = "Come on, Catherine"
with open('./斗破苍穹.txt','r+',encoding='utf-8') as f:
	str = f.read()[:1000]
	print(str[:10])
	engine = pyttsx3.init()
	engine.say(str)
	engine.runAndWait()
	f.close()