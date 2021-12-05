from gpiozero import LED, Button
from time import sleep
from datetime import datetime
import atexit

powerLight = LED(17)
powerLight.on()
selectedUser = 0

def exit_handler():
	powerLight.off()

atexit.register(exit_handler)

def writeEventToFile(eventName):
    with open("/home/pi/projects/moodbox/moodLog.csv", 'a') as file_object:
        dateString = datetime.now().isoformat()
        file_object.write("{},{},{}\n".format(dateString, eventName, selectedUserDict[selectedUser]['name']))

def handleEmotionPress(pressedButton):
	emotionProperties = pinToEmotionDict[pressedButton.pin]
	print('{} pushed the {} button'.format(selectedUserDict[selectedUser]['name'], emotionProperties['buttonName']))
	writeEventToFile(emotionProperties['buttonName'])
	emotionProperties['LEDOutput'].on()
	

def handleEmotionRelease(releasedButton):
	emotionProperties = pinToEmotionDict[releasedButton.pin]
	emotionProperties['LEDOutput'].off()


emotionButtons = [Button(5), Button(6), Button(13), Button(19)]
for emotionButton in emotionButtons:
	emotionButton.when_pressed = handleEmotionPress
	emotionButton.when_released = handleEmotionRelease

pinToEmotionDict = {}
pinToEmotionDict[emotionButtons[0].pin] = {'buttonName': 'happy', 'LEDOutput': LED(12)}
pinToEmotionDict[emotionButtons[1].pin] = {'buttonName': 'mediocre', 'LEDOutput': LED(16)}
pinToEmotionDict[emotionButtons[2].pin] = {'buttonName': 'sad', 'LEDOutput': LED(20)}
pinToEmotionDict[emotionButtons[3].pin] = {'buttonName': 'anxious', 'LEDOutput': LED(21)}

userSwitch = Button(4)
selectedUserDict = {}
selectedUserDict[0] = {'name': 'Russell', 'LEDOutput': 0}
selectedUserDict[1] = {'name': 'Elizabeth', 'LEDOutput': 1}

while True:
	if(userSwitch.is_pressed):
		selectedUser = 0 
	else:
		selectedUser = 1 
	continue

