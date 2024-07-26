mode=input()        #User types in a mode, either "encrypt" or "decrypt"
base=int(input())   #enter the base you're encrypting to or decrypting from
message=''          
List=[]
output=''
lst=[]
paragraph=[]



        


if mode=="encrypt":

    while True:                         #ensures that the message can be entered across multiple lines
        try:
            line=input()
            paragraph.append(line)
            if not line:                #if user enters an empty line, stop the program
                break
        except EOFError:
            break
        message='\n'.join(paragraph)    

    for i in range(len(message)):       
        List.append(ord(message[i]))    #adds the ASCII values of all the characters in the message in a list


    #Convert ASCII value to desired base

    for i in range(len(List)):
        num=List[i]
        converted=''
        divisor=num



        if base<11 and base>=2:
            converted=''
            if num==0:
                converted+='0'
            else:
                while divisor!=0:
                    converted=converted+str(divisor%base)
                    divisor=divisor//base

        elif  base>=11 and base<=36:
            converted=''
            if num==0:
                converted+='0'
            else:
                while divisor!=0:
                        
                    if divisor%base<10:
                        converted=converted+str(divisor%base)           
                        divisor=divisor//base
                                
                    elif divisor%base>=10:
                        converted=converted+chr((divisor%base)+55)
                        divisor=divisor//base
        else:
            output=''
        output=output+converted[::-1]+' '
    print(output[:-1])


    #Convert numbers from a specific base back to the original message


elif mode=="decrypt":
    message=input()
    List=message.split(' ')
    
    for k in range(len(List)):
        num=List[k]
        num=num[::-1]
        converted=0
        for i in range(len(num),0,-1):

            if num[i-1] in ['0','1','2','3','4','5','6','7','8','9']:     
                converted=converted+(int(num[i-1])*(base**(i-1)))
            else:
                converted+=(ord(num[i-1])-55)*(base**(i-1))
        lst.append(converted)


    for j in range(len(lst)):
        output=output+chr(lst[j])
    print(output)