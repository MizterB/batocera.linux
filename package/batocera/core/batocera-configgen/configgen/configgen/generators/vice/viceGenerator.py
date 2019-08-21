#!/usr/bin/env python
import Command
import batoceraFiles
from generators.Generator import Generator
import os.path
import glob


class ViceGenerator(Generator):

    def getResolutionMode(self, config):
        return 'default'
    
    # Main entry of the module
    # Return command
    def generate(self, system, rom, playersControllers, gameResolution):
        romPath = os.path.dirname(rom)
        romName = os.path.splitext(os.path.basename(rom))[0]

        commandArray = [batoceraFiles.batoceraBins[system.config['emulator']], 
                        "-config", batoceraFiles.viceConfig,
                        "-autostart", rom]

        return Command.Command(array=commandArray,  env={"SDL_VIDEO_GL_DRIVER": "/usr/lib/libGLESv2.so"})
