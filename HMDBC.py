#encoding="utf-8"
#HerbeMalveillante's Discord Bot Client V0.1
#Warning : for the moment, NO error troubleshooting is implemented, so please respect the conventions and don't type randomly.
#Note : i MUST use the audit log thing, and the icon_url_as() thing


import discord
import sys
import asyncio
import json
import time
import os
from datetime import datetime
from jsonpdfmodule import jsonToPdf
from readmeCreator import createReadme
import time

version = "0.1.4"

#------------------------------------------------------------------------------


def initialize_discord(token): #initialize the connection for a given token. 
    print("Initializing the connection, please wait...\n")
    client.run(token) #/!\ Once this function is called, anything elsewhere than in the "async def on_ready" will be executed


async def saveServer(guild, channels,limitMessages, fileType): #Function that saves a server.
    '''
    Taken arguments : -server : server object
                      -channels : list of channels index to save
                      -limit : messages saved per channel. If None, it will save everything (slow)
                      -saveContent : "log" or "messages" (will be modified after)
                      -fileType : "json" or "pdf" (will be modified after)
                      -outputSave : "default" or complete path
                      -outputLog : "default" or complete path
    '''
    print("Starting saving " + guild.name +". Please wait, it may take a while")
    
    timeStart = time.time()

    #Converting the indexes to channel object.
    channelObjectList = []
    for index in channels :

        channelObject = guild.text_channels[index]
        channelObjectList.append(channelObject)
    

    
    #retrieve all the messages from each channel and stores it in a dictionnary
        
    serverSave = {} #the largest dictionnary    
    
    '''
    warning ! all the commented lines in the following code contains information that cannot be transferred into json. It needs to be fixed.
    '''
    serverInfo = {} #the dictionnary that contains the informations of the server
    
    serverInfo["name"] = guild.name #str
    serverInfo["region"] = guild.region #VoiceRegion (specific)
    serverInfo["afk_timeout"] = guild.afk_timeout #int
    serverInfo["icon"] = str(guild.icon_url) #str
    serverInfo["is_icon_animated"] = guild.is_icon_animated() #bool
    serverInfo["id"] = guild.id #int
    serverInfo["owner_id"] = guild.owner_id #int
    serverInfo["owner"] = str(guild.owner) #member
    serverInfo["created_at"] = str(guild.created_at) #datetime converted to string
    serverInfo["member_count"] = guild.member_count #int
    serverInfo["max_presences"] = guild.max_presences #int
    serverInfo["max_members"] = guild.max_members #int
    serverInfo["description"] = guild.description #str
    serverInfo["mfa_level"] = guild.mfa_level #int : 0 = no 2FA , 1 = 2FA
    serverInfo["verification_level"] = guild.verification_level #verification level (specific)
    serverInfo["explicit_content_filter"] = guild.explicit_content_filter #ContentFilter (specific)
    serverInfo["default_notifications"] = guild.default_notifications #NotificationLevel (specific)
    serverInfo["features"] = guild.features #list[str]
    serverInfo["splash"] = guild.splash #str
    serverInfo["premium_tier"] = guild.premium_tier #int from 0 to 3
    serverInfo["premium_subscription_count"] = guild.premium_subscription_count #int
    serverInfo["preferred_locale"] = guild.preferred_locale #str
    serverInfo["discovery_splash"] = guild.discovery_splash #str
    serverInfo["large"] = guild.large #bool
    serverInfo["emoji_limit"] = guild.emoji_limit #int
    serverInfo["bitrate_limit"] = guild.bitrate_limit #float
    serverInfo["filesize_limit"] = guild.filesize_limit #int (in byte)    
    if guild.afk_channel == None :
        serverInfo["afk_channel"] = "None"
    else :
        serverInfo["afk_channel"] = guild.afk_channel.name #string
    emojiList = []
    for i in guild.emojis :
        emojiList.append(i.name)
    serverInfo["emojis"] = emojiList #tuple
    serverInfo["banner_url"] = str(guild.banner_url) #asset
    serverInfo["splash_url"] = str(guild.splash_url) #asset
    serverInfo["discovery_splash_url"] = str(guild.discovery_splash_url) #asset   
    if guild.system_channel == None :
        serverInfo["system_channel"] = "None"
    else :
        serverInfo["system_channel"] = guild.system_channel.name #TextChannel       
    if guild.rules_channel == None :
        serverInfo["rules_channel"] = "None"
    else :
        serverInfo["rules_channel"] = guild.rules_channel.name #TextChannel        
    serverInfo["default_role"] = str(guild.default_role.name)
    roleNameList = []
    for i in guild.roles :
        roleNameList.append(i.name)
    serverInfo["roles"] = roleNameList    
    premiumSubscribersNames = []
    for i in guild.premium_subscribers :
        premiumSubscribersNames.append(i.name)
    serverInfo["premium_subscribers"] = premiumSubscribersNames        
    members = []
    for i in guild.members :
        members.append(str(i))
    serverInfo["members"] = members   
    voiceChannels = []
    for i in guild.voice_channels :
        voiceChannels.append(i.name)
    serverInfo["voice_channels"] = voiceChannels  
    textChannels = []
    for i in guild.text_channels :
        textChannels.append(i.name)
    serverInfo["text_channels"] = textChannels    
    categories = []
    for i in guild.categories :
        categories.append(i.name)
    serverInfo["categories"] = categories    
    #the following lines won't be useful for now
    #serverInfo["channels"] = guild.channels #list[abc.GuildChannel] WARNING THIS NEEDS TO BE FIXED
    #serverInfo["categories"] = guild.categories #list[CategoryChannel]
    #serverInfo["by_category"] = guild.by_category() #List[Tuple[Optional[CategoryChannel], List[abc.GuildChannel]]]
    
    
    
     
    
      
        
    serverMessages = {} #the dictionnary that contains the messages for each channel
    for channel in channelObjectList :
        channelMessage = []
        async for message in channel.history(limit = limitMessages):
            selectedMessage = {}
            selectedMessage["author"] = str(message.author)
            selectedMessage["date"] = str(message.created_at)
            selectedMessage["content"] = message.content
            channelMessage.insert(0,selectedMessage)
            
        serverMessages[channel.name] = channelMessage
        
    
        

            
    serverSave["info"] = serverInfo
    serverSave["messages"] = serverMessages
            
        
    today=datetime.today() #gets the date for the namefile
    name=str(today.year) + str(today.month) + str(today.day) + str(today.hour) + str(today.minute)
    try :
        os.mkdir("serverSaves/"+name)
    except :
        print("folder \"" +name+"\" already exists" )
        
    with open("serverSaves/"+name+"/"+name+"serverSave.json", "w") as fp:
        json.dump(serverSave, fp)
    
    timeJson = time.time()
    print("The json save has been done successfully. Please check serverSaves/"+name+"/"+name+"serverSave.json")
    print("Time elapsed : " + str(round(timeJson-timeStart,2))+"s.")
    
                
    if fileType == "pdf":
        jsonToPdf("serverSaves/"+name+"/"+name+"serverSave.json",name)
        timePDF = time.time()
        print("Time elapsed : " + str(round(timePDF-timeJson,2))+"s.")
            
    print("saving done.")
    print("Total time : " + str(round(timePDF-timeStart,2))+"s.")
    
        
                
def getGuild(): #not a definitive function, is used to get the server. returns a guild object
    print("\nhere are the servers the client is connected to.")
    count = 0
    for guild in client.guilds :
        print(str(count) + " | " + guild.name)
        count+=1
        
    serverIndex = int(input("Select the index of the server you want to save : "))
    selectedGuild = client.guilds[int(serverIndex)]
    print("the selected Guild is " + selectedGuild.name)
    return(selectedGuild)
    
def getChannels(guild): #This function can't be used BEFORE the getGuild() function. Not a definitive function either. Used to select the channels. returns a list of channel indexes
    print("\nhere are the text channels the server has. Please note that the bot may not have the acces to all the channels of the server.")
    count = 0
    for channel in guild.text_channels :
        print(str(count) + " | " + channel.name)
        count+=1
    
    channelList = []
    while 1==1 :
        userInput = input("Please select the index of the channels you want to save. Please press \"ENTER\" between each input.\nType \"all\" to select all the channels. type \"end\"when you're done selecting the channels :")
        if userInput != "all" and userInput != "end" :
            if userInput not in channelList :
                channelList.append(int(userInput))
            else :
                print("the channel has already been selected.")
                
        elif userInput == "all" :
            channelList = []
            for i in range(len(guild.text_channels)) :
                channelList.append(i)
            print("Selected channels : all")
            break
                
        elif userInput == "end" :
            serversSelectedStr = ""
            for i in channelList:
                serversSelectedStr = serversSelectedStr + str(i) + "|"
            print("Selected channels : " + "|" + serversSelectedStr)
            break
            
    return(channelList)



def init():
    print("HerbeMalveillante's Discord Bot Client V"+version)
    if not os.path.exists("serverSaves"):
        if not os.path.exists("readme.txt"):
            createReadme(version)
        os.mkdir("serverSaves")
        print("A \"readme.txt\" file and a \"serverSaves\" folder were created. Please check them out.")
        
    token = input("Please enter the token of the bot you want to connect to (without the quotation marks) : ")
    initialize_discord(token)
    
    


#-------------------------------------------------------------------------------

client = discord.Client()
@client.event
async def on_ready() :
    global isBotRunning
    if isBotRunning == False : #The bot tends to be ready again after heavy tasks. I make sure this won't run the program twice.
        
        #everything here will run when the bot is connected. When the bot is connected, anything in this or below another event won't run.
        print("Logged in as:", client.user.name)
        print("ID:", client.user.id)
        print("Logged in successfully ! The program can now interact with discord. Make sure that the bot is on the server that you want to save and have the correct permissions : read messages / read message history")
        isBotRunning = True
    
        #the following actions are provisory
        selectedGuild = getGuild()
        selectedChannels = getChannels(selectedGuild)
        await saveServer(selectedGuild, selectedChannels, None, "pdf")
    

isBotRunning = False
init()