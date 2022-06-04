import os
from dataclasses import dataclass

import pygame
import utils.display_functions as display


#screen = display.displayInit()


@dataclass(frozen=True)
class Font:
    # ['arial', 'arialblack', 'bahnschrift', 'calibri', 'cambria', 'cambriamath', 'candara', 'comicsansms',
    # 'consolas', 'constantia', 'corbel', 'couriernew', 'ebrima', 'franklingothicmedium', 'gabriola', 'gadugi',
    # 'georgia', 'impact', 'inkfree', 'javanesetext', 'leelawadeeui', 'leelawadeeuisemilight', 'lucidaconsole',
    # 'lucidasans', 'malgungothic', 'malgungothicsemilight', 'microsofthimalaya', 'microsoftjhenghei',
    # 'microsoftjhengheiui', 'microsoftnewtailue', 'microsoftphagspa', 'microsoftsansserif', 'microsofttaile',
    # 'microsoftyahei', 'microsoftyaheiui', 'microsoftyibaiti', 'mingliuextb', 'pmingliuextb', 'mingliuhkscsextb',
    # 'mongolianbaiti', 'msgothic', 'msuigothic', 'mspgothic', 'mvboli', 'myanmartext', 'nirmalaui',
    # 'nirmalauisemilight', 'palatinolinotype', 'segoemdl2assets', 'segoeprint', 'segoescript', 'segoeui',
    # 'segoeuiblack', 'segoeuiemoji', 'segoeuihistoric', 'segoeuisemibold', 'segoeuisemilight', 'segoeuisymbol',
    # 'simsun', 'nsimsun', 'simsunextb', 'sitkasmall', 'sitkatext', 'sitkasubheading', 'sitkaheading',
    # 'sitkadisplay', 'sitkabanner', 'sylfaen', 'symbol', 'tahoma', 'timesnewroman', 'trebuchetms', 'verdana',
    # 'webdings', 'wingdings', 'yugothic', 'yugothicuisemibold', 'yugothicui', 'yugothicmedium', 'yugothicuiregular',
    # 'yugothicregular', 'yugothicuisemilight', 'holomdl2assets', 'century', 'leelawadee', 'microsoftuighur',
    # 'wingdings2', 'wingdings3', 'tempussansitc', 'pristina', 'papyrus', 'mistral', 'lucidahandwriting',
    # 'kristenitc', 'juiceitc', 'frenchscript', 'freestylescript', 'bradleyhanditc', 'bookantiqua', 'garamond',
    # 'monotypecorsiva', 'centurygothic', 'algerian', 'baskervilleoldface', 'bauhaus93', 'bell', 'berlinsansfb',
    # 'bernardcondensed', 'bodonipostercompressed', 'britannic', 'broadway', 'brushscript', 'californianfb',
    # 'centaur', 'chiller', 'colonna', 'cooperblack', 'footlight', 'harlowsolid', 'harrington', 'hightowertext',
    # 'jokerman', 'kunstlerscript', 'lucidabright', 'lucidacalligraphy', 'lucidafaxregular', 'magneto',
    # 'maturascriptcapitals', 'modernno20', 'niagaraengraved', 'niagarasolid', 'oldenglishtext', 'onyx', 'parchment',
    # 'playbill', 'poorrichard', 'ravie', 'informalroman', 'showcardgothic', 'snapitc', 'stencil', 'vinerhanditc',
    # 'vivaldi', 'vladimirscript', 'widelatin', 'twcen', 'twcencondensed', 'script', 'rockwellextra',
    # 'rockwellcondensed', 'rockwell', 'rage', 'perpetuatitling', 'perpetua', 'palacescript', 'ocraextended',
    # 'maiandragd', 'lucidasanstypewriterregular', 'lucidasansregular', 'imprintshadow', 'haettenschweiler',
    # 'goudystout', 'goudyoldstyle', 'gloucesterextracondensed', 'gillsansultracondensed', 'gillsansultra',
    # 'gillsanscondensed', 'gillsans', 'gillsansextcondensed', 'gigi', 'franklingothicmediumcond',
    # 'franklingothicheavy', 'franklingothicdemicond', 'franklingothicdemi', 'franklingothicbook', 'forte',
    # 'felixtitling', 'erasmediumitc', 'erasitc', 'erasdemiitc', 'engravers', 'elephant', 'edwardianscriptitc',
    # 'curlz', 'copperplategothic', 'centuryschoolbook', 'castellar', 'calisto', 'bookmanoldstyle',
    # 'bodonicondensed', 'bodoniblack', 'bodoni', 'blackadderitc', 'arialrounded', 'agencyfb', 'bookshelfsymbol7',
    # 'msreferencesansserif', 'msreferencespecialty', 'berlinsansfbdemi', 'lucidafax', 'twcencondensedextra',
    # 'lucidasanstypewriter', 'lucidasanstypewriteroblique', 'lucidasansroman', 'extra', 'msoutlook', 'opensans',
    # 'opensanssemibold', 'teamviewer15']
    _cwd = os.getcwd()

    standart_font_size = 36
    standart_font_file_path = os.path.join(_cwd, 'constants', 'fonts', 'ITCBLKAD.TTF')

    minotaure_font_size = 36
    minotaure_font_file_path = os.path.join(_cwd, 'constants', 'fonts', 'Minotaure.ttf')

   # standart_font = pygame.font.Font(, 36)
   # minotaure_font = pygame.font.Font(os.path.join(_cwd, 'constants', 'fonts', 'Minotaure.ttf'), 36)