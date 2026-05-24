import pyttsx3

# =====================================================
# SPEAK ALERT
# =====================================================

def speak_alert(message):

    engine = pyttsx3.init()

    engine.setProperty(
        'rate',
        150
    )

    engine.setProperty(
        'volume',
        1
    )

    voices = engine.getProperty(
        'voices'
    )

    engine.setProperty(
        'voice',
        voices[0].id
    )

    engine.say(message)

    engine.runAndWait()