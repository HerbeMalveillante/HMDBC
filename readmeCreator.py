import os

def createReadme(version):
    f = open("readme.txt","w+")
    
    f.write("Herbe Malveillante's Discord Bot Creator V"+version+"\n")
    f.write("_________________________________\n\n")
    f.write("this program is created by Herbe Malveillante.\n")
    f.write("website : http://projetcharbon.tk\n")
    f.write("Discord : HerbeMalveillante#0252\n")
    f.write("Twitter : @P4CO3\n")
    f.write("_________________________________\n\n")
    f.write("Changelog : (The first number is the global version (0=beta). The second one is the subversion. It increases each time i publish an update. The third one is the build number.)\n")
    f.write("V0.1.X : first successful build. allow user to select a server and the channels, and the server get saved in json and pdf.")
    f.close()
