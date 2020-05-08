
pas=input("Type Password please ====> ")
if pas  =='PALESTINE':
    print("correct")
    print("welcome to ZD10 tool")
    import os
    os.system("clear")
    
    print("\033[01;36m special thank's for my brother's ===> ♡ SAIF & NR11 ♡")
    def zd10 ():
        print("\033[2;39m ______  _____    ___   _____ ")
        print("\033[2;39m|___  / |  _  \  |_  | /  _  \ ")
        print("\033[2;32m   / /  | | | |    | | | | | |")
        print("\033[2;31m  / /   | | | |    | | | |/| |")
        print("\033[2;32m / /__  | |_| |    | | | |_| |")
        print("\033[2;39m/_____| |_____/    |_| \_____/")
    zd10()
    
    import socket
    import sys
   
    list="""   
    \033[01;34m[1] \033[01;31m scan a ip for website
    \033[01;37m[2] \033[01;32m little game (^_-) 
    \033[01;32m[3] \033[01;34m install kali linux for Termux
    \033[01;31m[4] \033[01;33m scan a port open for website
    \033[01;38m[5] \033[01;37m install tool for Collect information about the number's 
    \033[01;36m[6] \033[01;35m install metasploit
    """
    print(list)
    
    
    num=int(input("choose number please ===> "))
    if num == 1:
        
        host=input("\033[2;32mtype link here \033[2;31m===>")
        ip=socket.gethostbyname(host)
        print("Host is:",host,'\n''target ip is',ip)
    
    
    elif num == 2:
        import os
        os.system("clear")
        import sys
#########start#########
        user1=input("What's your name ? : ")  
        user2=input("And your name ? : ") 
        user1_answer=input("%s,\033[0;39m do you want to choose { \033[2;35m rock or \033[2;39m paper or \033[1;32m scissors } ? : " %user1)
        user2_answer=input("%s,\033[0;39m do you want to choose { \033[2;35mrock or \033[2;39m paper or \033[1;32m scissor } ? : " %user2)
#######code######
        def compare(u1,u2):
            if u1==u2:
                return("oh it's a tiel") 

            elif u1 =='rock':
                if u2 =='scissors':
                    return(u1,"win!")
                else:
                    return(u2,"win!")
                
            elif u1 =='paper':
                if u2 =='rock':
                    return(u1,'won!')
                else:
                    return(u2,'win!')
            elif u1 =='scissors':
                if u2 =='paper':
                    return(u,'win!')
                else:
                    return(u2,'win!')
            else:
                return("Invalid input ! you have not entered rock or paper or scissors,try again")
            sys.exit()
        print (compare(user1_answer,user2_answer))
##############################################################        
    elif num == 3:
        os.system("pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/Techriz/AndronixOrigin/master/Installer/Kali/kali.sh && bash kali.sh")
        
    elif num == 4:
        website = input('\033[01;34m | ENTER a WEBSITE ===> ')
        os.system("ping" + " " + website)   
    
    elif num == 5:
        os.system("https://github.com/entynetproject/phonia && chmod +x install.sh")

    elif num == 6:
        os.system("pkg install ruby")
        os.system("wget https://Auxilus.github.io/metasploit.sh")
        os.system("bash metasploit.sh")
        
    yazan = """

    \033[01;39m\script made by : Yazan Al Azab 
                  
    \033[01;35m\ Instagram ==> \033[01;31m\ @zid_mod10
    """
    print (yazan)
else:
    print("ERROR TRY AGAIN\v"*1000)
       