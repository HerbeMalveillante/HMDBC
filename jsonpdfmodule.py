import json
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
import requests
import PIL.Image
import time



def jsonToPdf(file,filename): #creation of the pdf file
    print("Starting creating the pdf file. Please wait, it may take a while")
    with open (file,"r")as fp:
        data = json.load(fp)
        
    my_doc = SimpleDocTemplate("serverSaves/"+filename+"/"+filename+"serverSavePDF.pdf")
    flowables = []
    sample_style_sheet = getSampleStyleSheet()
    
    
    paragraph_1 = Paragraph("<u>"+data["info"]["name"] + " server save</u>", sample_style_sheet['Heading1']) #title
    flowables.append(paragraph_1)
    
    
    paragraph_2 = Paragraph("Created with HerbeMalveillante's Discord Bot Client",sample_style_sheet['BodyText']) #subtitle
    flowables.append(paragraph_2)
    serverInfo = Paragraph ("Server Informations : ", sample_style_sheet["Heading2"]) #server Informations :
    flowables.append(serverInfo)
    
    info=Paragraph("<u>Name : </u>" + data["info"]["name"], sample_style_sheet["BodyText"]) #Name
    flowables.append(info)
    info=Paragraph("<u>Icon : </u>" + data["info"]["icon"], sample_style_sheet['BodyText'])#Icon
    flowables.append(info)
    with open("serverSaves"+"/"+filename+"/"+"serverIcon.png", 'wb') as f: #downloads the image from the given url
        f.write(requests.get(data["info"]["icon"]).content)
    image = Image("serverSaves"+"/"+filename+"/"+"serverIcon.png", 1.5*cm,1.5*cm)
    image.hAlign = "LEFT"
    flowables.append(image)
    
    info=Paragraph("<u>Region : </u>" + data["info"]["region"][0],sample_style_sheet["BodyText"])
    flowables.append(info)
    info=Paragraph("<u>Afk timeout : </u>" + str(data["info"]["afk_timeout"])+" seconds",sample_style_sheet["BodyText"])
    flowables.append(info)
    info=Paragraph("<u>Is icon animated </u>: " + str(data["info"]["is_icon_animated"]),sample_style_sheet["BodyText"])
    flowables.append(info)
    info=Paragraph("<u>ID : </u>" + str(data["info"]["id"]),sample_style_sheet["BodyText"])
    flowables.append(info)
    info=Paragraph("<u>Owner ID : </u>" + str(data["info"]["owner_id"]),sample_style_sheet["BodyText"])
    flowables.append(info)
    info=Paragraph("<u>Owner Name : </u>" + str(data["info"]["owner"]),sample_style_sheet["BodyText"])
    flowables.append(info)
    info=Paragraph("<u>Created at : </u>" + str(data["info"]["created_at"]),sample_style_sheet["BodyText"])
    flowables.append(info)
    info=Paragraph("<u>Member count : </u>" + str(data["info"]["member_count"]),sample_style_sheet["BodyText"])
    flowables.append(info)
    info=Paragraph("<u>Max presences : </u>" + str(data["info"]["max_presences"]),sample_style_sheet["BodyText"])
    flowables.append(info)
    info=Paragraph("<u>Max members : </u>" + str(data["info"]["max_members"]),sample_style_sheet["BodyText"])
    flowables.append(info)
    info=Paragraph("<u>Description : </u>" + str(data["info"]["description"]),sample_style_sheet["BodyText"])
    flowables.append(info)
    info=Paragraph("<u>Mfa level : </u>" + str(data["info"]["mfa_level"]),sample_style_sheet["BodyText"])
    flowables.append(info)
    info=Paragraph("<u>Verification level : </u>" + str(data["info"]["verification_level"][0]),sample_style_sheet["BodyText"])
    flowables.append(info)
    info=Paragraph("<u>Explicit content filter : </u>" + str(data["info"]["explicit_content_filter"][0]),sample_style_sheet["BodyText"])
    flowables.append(info)
    info=Paragraph("<u>Default notifications : </u>" + str(data["info"]["default_notifications"][0]),sample_style_sheet["BodyText"])
    flowables.append(info)
    strFeatures = "|"
    for i in data["info"]["features"]:
        strFeatures = strFeatures + str(i) + "|"
    info=Paragraph("<u>Features : </u>" + strFeatures,sample_style_sheet["BodyText"])
    flowables.append(info)
    info=Paragraph("<u>Splash : </u>" + str(data["info"]["splash"]),sample_style_sheet["BodyText"])
    flowables.append(info)
    info=Paragraph("<u>Premium tier : </u>" + str(data["info"]["premium_tier"]),sample_style_sheet["BodyText"])
    flowables.append(info)
    info=Paragraph("<u>Premium subscription count : </u>" + str(data["info"]["premium_subscription_count"]),sample_style_sheet["BodyText"])
    flowables.append(info)
    info=Paragraph("<u>Preferred locale : </u>" + str(data["info"]["preferred_locale"]),sample_style_sheet["BodyText"])
    flowables.append(info)
    info=Paragraph("<u>Discovery splash : </u>" + str(data["info"]["discovery_splash"]),sample_style_sheet["BodyText"])
    flowables.append(info)
    info=Paragraph("<u>Is large : </u>" + str(data["info"]["large"]),sample_style_sheet["BodyText"])
    flowables.append(info)
    info=Paragraph("<u>Emoji limit : </u>" + str(data["info"]["emoji_limit"]),sample_style_sheet["BodyText"])
    flowables.append(info)
    info=Paragraph("<u>Bitrate limit : </u>" + str(data["info"]["bitrate_limit"]),sample_style_sheet["BodyText"])
    flowables.append(info)
    info=Paragraph("<u>Filesize limit : </u>" + str(data["info"]["filesize_limit"]),sample_style_sheet["BodyText"])
    flowables.append(info)
    info=Paragraph("<u>Afk channel : </u>" + str(data["info"]["afk_channel"]),sample_style_sheet["BodyText"])
    flowables.append(info)
    emojis = "| "
    for i in data["info"]["emojis"]:
        emojis += i +" | "
    info=Paragraph("<u>Emoji list : </u>" + emojis,sample_style_sheet["BodyText"])
    flowables.append(info)
    info=Paragraph("<u>Banner url : </u>" + str(data["info"]["banner_url"]),sample_style_sheet["BodyText"])
    flowables.append(info)
    info=Paragraph("<u>Splash url : </u>" + str(data["info"]["splash_url"]),sample_style_sheet["BodyText"])
    flowables.append(info)
    info=Paragraph("<u>Discovery splash url : </u>" + str(data["info"]["discovery_splash_url"]),sample_style_sheet["BodyText"])
    flowables.append(info)
    info=Paragraph("<u>System Channel : </u>" + str(data["info"]["system_channel"]),sample_style_sheet["BodyText"])
    flowables.append(info)
    info=Paragraph("<u>Rules Channel : </u>" + str(data["info"]["rules_channel"]),sample_style_sheet["BodyText"])
    flowables.append(info)
    info=Paragraph("<u>Default role : </u>" + str(data["info"]["default_role"]),sample_style_sheet["BodyText"])
    flowables.append(info)
    
    roles = "| "
    for i in data["info"]["roles"]:
        roles += i + " | "
        
    info=Paragraph("<u>Role list : </u>" + roles,sample_style_sheet["BodyText"])
    flowables.append(info)
    
    premiumSubscribers = "| "
    for i in data["info"]["premium_subscribers"]:
        premiumSubscribers += i + " | "
    info=Paragraph("<u>Premium subscribers : </u>" + premiumSubscribers,sample_style_sheet["BodyText"])
    flowables.append(info)
    
    memberList = "| "
    for i in data["info"]["members"]:
        memberList += i + " | "
    info=Paragraph("<u>Members : </u>" + memberList,sample_style_sheet["BodyText"])
    flowables.append(info)
    
    voiceList = "| "
    for i in data["info"]["voice_channels"]:
        voiceList += i + " | "
    info=Paragraph("<u>Voice channels : </u>" + voiceList,sample_style_sheet["BodyText"])
    flowables.append(info)
    
    textList = "| "
    for i in data["info"]["text_channels"]:
        textList += i + " | "
    info=Paragraph("<u>Text channels : </u>" + textList,sample_style_sheet["BodyText"])
    flowables.append(info)
    
    categoriesList = "| "
    for i in data["info"]["categories"]:
        categoriesList += i + " | "
    info=Paragraph("<u>Categories : </u>" + categoriesList,sample_style_sheet["BodyText"])
    flowables.append(info)
    
    
    
    #-------------Messages---------------
    
    serverInfo = Paragraph ("Server Messages : ", sample_style_sheet["Heading2"]) #server Informations :
    flowables.append(serverInfo)
    
    #Explication :
    #The data dictionnary is made out of two dictionnarys : "info" and "messages".
    #The message dictionnary (data["messages"]) is made out of a key for each channel, wich value is a list of messages. 
    #Each message is himself a dictionnary : it has a ["content"] value, a ["author"] value and a ["date"] value.
    """
    channel_list = list(data["messages"].keys())
    counter = 0
    for channel in data["messages"]:#channel is a list of messages.
        serverInfo = Paragraph(channel_list[counter],sample_style_sheet["Heading3"])
        flowables.append(serverInfo)
        counter +=1
        for message in channel : #message is a dictionnary
            
            messageParagraph = Paragraph("<u>"+message["author"]+"</u> (<i>"+message["date"]+"</i>) :" + message["content"])
            flowables.append(messageParagraph)
    """
    
    
    for channel in data["messages"]:
        channelParagraph = Paragraph(channel+" :", sample_style_sheet["Heading3"])
        flowables.append(channelParagraph)
        
        for message in data["messages"].get(channel) :
            
            try :
                messageParagraph = Paragraph("<u>"+message["author"]+"</u> (<i>"+message["date"]+"</i>) :" + message["content"], sample_style_sheet["BodyText"])
                flowables.append(messageParagraph)
            except :
                errorMessage = Paragraph("Something went wront, we could not save this message in the pdf file.", sample_style_sheet["BodyText"])
                flowables.append(errorMessage)
                print("a message could not be integrated in the pdf.")
        
            
    
    
    
    
    
    
    
    
    
    
        
    
    
    
    
    
    
    
    my_doc.build(flowables)
    print("The pdf file has been created successfully. Please check serverSaves/" + filename + "/"+filename+"serverSavePDF.pdf")