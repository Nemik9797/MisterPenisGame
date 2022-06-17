import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Sounds:
    _cwd = os.getcwd()

    main_menu_sound = os.path.join(_cwd, "content", "Sounds", "Kristofer Maddigan - Introduction.mp3")