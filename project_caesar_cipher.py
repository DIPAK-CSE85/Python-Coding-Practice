# both encrypt and decrypt is seperated
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encryption(plane_text,shift_key):
    cipher_text=""
    for char in plane_text:
        if char in alphabets:
            position=alphabets.index(char)
            new_position=(position+shift_key)%26
            cipher_text+=alphabets[new_position]
        else:
            cipher_text+=char    
    print("encrypted text is=",cipher_text)    
def decryption(cipher_text,shift_key):
    plane_text=""
    for char in cipher_text:
        if char in alphabets:
            position=alphabets.index(char)
            new_position=(position-shift_key)%26
            plane_text+=alphabets[new_position]
        else:
            plane_text+=char    
    print("encrypted text is=",plane_text) 
end=True
while end:    
    direction=input("type'encrypt'to encryption,type 'decrept' to decryption=")
    text=input("type a message=").lower()
    shift=int(input("enter a shift key="))
    if(direction=="encrypt"):
        encryption(text,shift)
    else:
        decryption(text,shift)
    play_again=input("type 'yes' for continue,type'no' for end=").lower()
    if(play_again=='no'):
        end=False
        print("have a nice day,Buy!")


# both encrypt  and decrypt is mixed        

alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def choice(direction,text,shift_key):
    if(direction=='decrypt'):
        shift_key*=-1
    new_text=""
    for char in text:
        if char in alphabets:
            position=alphabets.index(char)
            new_position=(position+shift_key)%26
            new_text+=alphabets[new_position]
        else:
            new_text+=char    
    print(f"here's is the text after {direction}=",new_text)    
end=True
while end:    
    direction=input("type'encrypt'to encryption,type 'decrept' to decryption=")
    text=input("type a message=").lower()
    shift=int(input("enter a shift key="))
    choice(direction=direction,text=text,shift_key=shift)
    play_again=input("type 'yes' for continue,type'no' for end=").lower()
    if(play_again=='no'):
        end=False
        print("have a nice day,Buy!")        