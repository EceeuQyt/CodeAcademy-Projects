#Shows defualt list for Range() up to 200, aplhabet included.
#list_char = []  
#for i in range(0, 200):
  #list_char.append(chr(i))  
#print(list_char)
message_offset10 = ' xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!' 
message_1 = 'jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.'
message_2 = 'bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!'
message_3 = 'vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px\'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.'
#Decoding Caesar cipher Message
def caesar(text, shift): 
  #Location route of decoded message--beforehand.
  cipherText = ""
  #Iterates over given text argument during function call
  for ch in text:
    #Recreates space between words by checking if space exist
    if ch == " ":
      cipherText += " "
    #Checks if index is within alphabet by using ord() method-- which searches the universal code of Alphabet between range(97, 123). Then adds universal(charindex) to given cipher shfit. Saves within stayinalphabet
    if ch.isalpha():
      stay_in_alphabet = ord(ch) + shift
      #Checks if varibale is greater then ord('z') index, so it does press beyond. Then subtracts perivous variable by total letters within the alphabet(26), returns result, and converts index number into universal character/ord(). Finally, adds letter and spaces to cipherText variable.  
      if stay_in_alphabet > ord('z'):
        stay_in_alphabet -= 26
      finalLetter = chr(stay_in_alphabet)
      cipherText += finalLetter
  print("Your ciphertext is:", cipherText)
  return cipherText

#Returning Caesar Cipher message
def encrypt_text(plaintext,n):
    ans = ""
    # iterate over the given text
    for i in range(len(plaintext)):
        ch = plaintext[i]
        # check if space is there then simply add space
        if ch==" ":
            ans+=" "
        # check if a character is uppercase then encrypt it accordingly 
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)
    return ans

# Vigenere Cipher
alphabet = "abcdefghijklmnopqrstuvwxyz"
def vigenere_decode(message, keyword):
  keyword_phrase = ""
  keyword_index = 0

  for character in message:
    if keyword_index >= len(keyword):
      keyword_index = 0
    if character in alphabet:
      keyword_phrase += keyword[keyword_index]
      keyword_index += 1
    else:
      keyword_phrase += character

  decoded_message = ""

  for i in range(len(message)):
    if message[i] in alphabet:
      old_character_index = alphabet.find(message[i])
      offset_index = alphabet.find(keyword_phrase[i])
      new_character = alphabet[(old_character_index + offset_index) % 26]
      decoded_message += new_character
    else:
      decoded_message += message[i]
    
  return decoded_message
vigenere_message = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!"
vigenere_keyword = "friends"



#Running Code
caesar(message_offset10, 10)
caesar(message_1, 10)
#caesar(message_2, 10)
caesar(message_3, 7)
print('Vigenere decoded:', vigenere_decode(vigenere_message, vigenere_keyword))


my_text = "Make it a little easier next time, yeah."
n = 10
print("Plain Text is : " + my_text)
print("Shift pattern is : " + str(n))
print("Cipher Text is : " + encrypt_text(my_text,n))