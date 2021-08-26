from Amplifier import Amplifier
from CdPlayer import CdPlayer
from DvdPlayer import DvdPlayer
from HomeTheaterFacade import HomeTheaterFacade
from Tuner import Tuner

if __name__ == '__main__':
    tuner = Tuner()
    cd = CdPlayer()
    dvd = DvdPlayer()
    amp = Amplifier()
    f = HomeTheaterFacade(tuner,amp,cd,dvd)
    f.watchMovie()
    f.endMovie()