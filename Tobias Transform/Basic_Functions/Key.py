from keyboard import Keyboard

""" Control the WINDOWS Volume. Can trigger sound and mute functions.
    Should be fully functional affter calling any function (IE resets) """

class Key():

    def __init__():
        currentVolume = 0
        is_muted = False
        
    """ Gets current volume """
    @staticmethod
    def current_volume():
        return Key.currentVolume

    """ Choose Volume between 0 and 100 """
    @staticmethod
    def set_current_volume(volume):
        if volume > 100:
            Key.currentVolume = 100
        elif volume < 0:
            Key.currentVolume = 0
        else:
            Key.currentVolume = volume

   # currentVolume = 0

   # is_muted = False

    """ Returns if muted """
    @staticmethod
    def is_muted():
        return Key.is_muted

    """ Starts Volume Tracking """
    @staticmethod
    def track():
        if Key.currentVolume == None:
            Key.currentVolume = 0
            for i in range(0, 50):
                Key.volume_up()
    @staticmethod
    def playpause():
        Keyboard.key(Keyboard.VK_MEDIA_PLAY_PAUSE)
    
    @staticmethod
    def nexttrack():
        Keyboard.key(Keyboard.VK_MEDIA_NEXT_TRACK)

    @staticmethod
    def previoustrack():
        Keyboard.key(Keyboard.VK_MEDIA_PREV_TRACK)

    """ Mute/Unmute """
    @staticmethod
    def mute():
        Key.track()
        Key.is_muted = (not Key.is_muted)
        Keyboard.key(Keyboard.VK_VOLUME_MUTE)

    """ Triggers a volume up key event """
    @staticmethod
    def volume_up():
        Key.track()
        Key.set_current_volume(Key.current_volume() + 2)
        Keyboard.key(Keyboard.VK_VOLUME_UP)

    """ Triggers a volume down key event """
    @staticmethod
    def volume_down():
        Key.track()
        Key.set_current_volume(Key.current_volume() - 2)
        Keyboard.key(Keyboard.VK_VOLUME_DOWN)


    @staticmethod
    def volume_set(amount):
        """
        Set the volume to a specific volume, limited to even numbers.
        This is due to the fact that a VK_VOLUME_UP/VK_VOLUME_DOWN event increases
        or decreases the volume by two every single time.
        :return: void
        """
        Key.track()

        if Key.current_volume() > amount:
            for i in range(0, int((Key.current_volume() - amount) / 2)):
                Key.volume_down()
        else:
            for i in range(0, int((amount - Key.current_volume()) / 2)):
                Key.volume_up()

    """ Set volume to Min (0) """
    @staticmethod
    def volume_min():
        Key.volume_set(0)

    """ Set volume to Max (100) """
    @staticmethod
    def volume_max():
        Key.volume_set(100)

    """ Browser Controls """
    
    @staticmethod
    def browserback():
        Keyboard.key(Keyboard.VK_BROWSER_BACK)

    @staticmethod
    def browsernext():
        Keyboard.key(Keyboard.VK_BROWSER_FORWARD)

    @staticmethod
    def browserrefresh():
        Keyboard.key(Keyboard.VK_BROWSER_REFRESH)

    @staticmethod
    def browserhome():
        Keyboard.key(Keyboard.VK_BROWSER_HOME)
