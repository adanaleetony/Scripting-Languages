password = input("Enter your message : ")
key = int(input("Enter a number : "))

def crypt(text,num):
    for i in range(len(text)):
        print(chr(ord(text[i])+num),end="")
        
crypt(password,key)

#def decrypt(text,num) :
    #for i in range(len(text)):
        #print(chr(ord(text[i])-num),end="")
        
#decrypt(password,key)