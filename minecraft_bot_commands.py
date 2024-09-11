import os
import requests
from typing import Final
from dotenv import load_dotenv

#loading variables from .env file
load_dotenv()
SERVER_URL: Final[str] = os.getenv('MINECRAFT_SERVER_URL')
MCSMANAGER_TOKEN: Final[str] = os.getenv('MCSMANAGER_TOKEN')
INSTANCE_ID: Final[str] = os.getenv('INSTANCE_TOKEN')
DAEMON_ID: Final[str] = os.getenv('DAEMON_TOKEN')


def get_response():
    return

#Creates the url for the HTTP API request, depending on the "choice" between open, stop and restart
def create_url(choice):
    url = SERVER_URL + choice
    parameters={
        'apikey': MCSMANAGER_TOKEN,
        'uuid': INSTANCE_ID,     
        'daemonId': DAEMON_ID,
    }
    r = url + '?apikey=' + MCSMANAGER_TOKEN + '&uuid=' + INSTANCE_ID + '&daemonId=' + DAEMON_ID
    return(r)
    
#Endpoint "open" starts the minecraft server
def start():
    requests.get(create_url('/api/protected_instance/open'))
    return

#Endpoint "stop" stops the minecraft server
def stop():
    requests.get(create_url('/api/protected_instance/stop'))
    return

#Endpoint "restart" restarts the minecraft server
def restart():
    requests.get(create_url('/api/protected_instance/restart'))
    return

#Endpoint "instance" retrieves informations from the minecraft server, as a json file
def get_infos():
    r = requests.get(create_url('/api/instance'))
    json_data = r.json() #stores the json data in a variable
    status = json_data['data']['started'] #Retrieves the "started" value from the json, which has "17" if online, and "15" if offline
    result = json_data['data']['config']['nickname'] #Retrieves the "nickname" value of the server, which is just the name given to the server when created
    
#Just adds the status of the server in String after the nickname of the server, to display something like :"Minecraft Server : Online"
    if(status == 17):
        result += ' : En ligne'
    else:
        result += ': Déconnecté'
    
    return(result)

#Most important part IMO, it filters the input from the discord user, so they get a response if they try to use a command that isn't implemented.
def interprete_commands(rqst):
    request = rqst
    match request:
        case 'start':
            start()
            return('Server powering on...')
        case 'stop':
            stop()
            return('Server powering off...')
        case 'restart':
            restart()
            return('Server restarting...')
        case 'infos':
            return(get_infos())
        case _:
            print(request)
            return('Invalid command')
        
