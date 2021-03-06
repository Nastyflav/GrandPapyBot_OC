#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-04-20
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from os import environ


#Application informations
APP_NAME = 'GrandPy Bot'
APP_CATCHLINE = 'On lui a installé l\'ADSL, profitez-en ! Trouvez des lieux et leur histoire !'
APP_AUTHOR = 'Flavien Murail'
APP_LINKEDIN_LINK = 'https://www.linkedin.com/in/flavien-murail-7155b7156/'
APP_REPO_LINK = 'https://github.com/Nastyflav/GrandPapyBot_OC'
APP_PARTNER_LINK = 'https://openclassrooms.com/'
APP_GPL_LINK = 'https://fr.wikipedia.org/wiki/Licence_publique_g%C3%A9n%C3%A9rale_limit%C3%A9e_GNU'

#Chatbox presets
TEXT_AREA = 'Coucou GrandPy, tu vas bien ? Dis-moi, tu ne saurais pas où se situe le Louvre par hasard ?'
ANSWERS_ADRESS_OK = ['Evidemment, je ne suis pas encore gâteux ! Voici l\'adresse', 
                    'Héhé, ça me dit quelque chose',
                    'Attends voir...Tiens, j\'ai trouvé',
                    'Tu ne connais pas ça ? Faut sortir un peu quand même']
ANSWERS_STORY_OK = ['Haha, je me souviens, un bien bel endroit',
                    'On y est allé avec ta grand-mère, on a passé du bon temps, héhé... Comment ça tu veux pas savoir ? Bon, voici la version pour les enfants',
                    'Alors, attends, oui, je me rappelle maintenant',
                    'Ouvre bien tes esgourdes, je ne le répéterai pas deux fois']
ANSWERS_ADRESS_FAIL = ['Tu as tourné la carte ou quoi ?',
                        'Connais pas. Je bosse pas aux PTT moi !',
                        'Sois plus précis s\'il te plait, GrandPy est fatigué...',
                        'Répète pour voir, j\'ai mal entendu']
ANSWERS_STORY_FAIL = ['Il ne se passe jamais rien là-bas, faut t\'y faire.',
                        'Je ne me suis jamais autant ennuyé que dans ce bled. Rien à dire.',
                        'Bon, je ne vais pas te faire la lecture jusqu\'à ma mort.',
                        'J\'ai pas la science infuse moi ! Regarde dans un livre !']

#Google Maps Api presets
GOOGLE_KEY = environ['API_KEY'],
GOOGLE_URL = 'https://maps.googleapis.com/maps/api/geocode/json?'
GOOGLE_LANGUAGE = 'fr'

#Wikipedia Api presets
WIKI_URL = 'https://fr.wikipedia.org/w/api.php'
