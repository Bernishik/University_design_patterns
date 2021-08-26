class HomeTheaterFacade:
    def __init__(self,tuner,amplifier,cdplayer,dvdPlayer):
        self.tuner = tuner
        self.amplifier = amplifier
        self.cdplayer = cdplayer
        self.dvdplayer = dvdPlayer

    def watchMovie(self):
        self.tuner.on()
        self.dvdplayer.on()
        self.dvdplayer.play()

    def endMovie(self):
        self.dvdplayer.stop()
        self.dvdplayer.off()

    def listenToCd(self):
        self.cdplayer.on()
        self.amplifier.on()
        self.cdplayer.play()

    def endToCd(self):
        self.cdplayer.stop()
        self.cdplayer.off()
        self.amplifier.off()

    def listenToRadio(self):
        self.tuner.on()
        self.tuner.setFm()

    def endRadio(self):
        self.tuner.off()
