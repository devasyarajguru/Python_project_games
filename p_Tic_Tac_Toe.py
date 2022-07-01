#from playsound import playsound
# from function_sound_file import function_sound

list1 = ['-','-','-','-','-','-','-','-','-',]
# Printing the Tic-Tac Toe patten
print(list1[0],'|',list1[1],'|',list1[2])
print(list1[3],'|',list1[4],'|',list1[5])
print(list1[6],'|',list1[7],'|',list1[8])

t = 1
while t<10:
    try:
        if t%2==0:
            print("Player2 Your turn[X]")
            # playsound("Turn2.mp3")
            x = int(input("Enter position:"))
            if list1[x-1]=='-':
                list1[x-1] = 'X'
            else:
                print("Position is Full!")
                t = t -1
        else:
            print("Player1 Your turn[O]")
            # playsound("Turn1.mp3")
            x = int(input("Enter position:"))
            if list1[x-1]=='-':
                list1[x-1] = 'O'
            else:
                print("Position is Full!")
                t = t -1
    except:
        print("PLease enter valid position!!")
        t = t -1


    print(list1[0], '|', list1[1], '|', list1[2])
    print(list1[3], '|', list1[4], '|', list1[5])
    print(list1[6], '|', list1[7], '|', list1[8])

    t = t + 1


    if list1[0]==list1[1]==list1[2] and list1[0]!="-":
        if list1[0]=='O':
            print("Player1 Won")
            t = 15
        else:
            print("Player2 Won")
            t = 15
        break
    elif list1[0]==list1[3]==list1[6] and list1[0]!="-":
        if list1[0]=='O':
            print("Player1 Won")
            t = 15
        else:
            print("Player2 Won")
            t = 15
        break
    elif list1[0]==list1[4]==list1[8] and list1[4]!="-":
        if list1[0]=='O':
            print("Player1 Won")
            t = 15
        else:
            print("Player2 Won")
            t = 15
        break
    elif list1[6]==list1[7]==list1[8] and list1[6]!="-":
        if list1[6]=='O':
            print("Player1 Won")
            t = 15
        else:
            print("Player2 Won")
            t = 15
        break
    elif list1[1]==list1[4]==list1[7] and list1[1]!="-":
        if list1[1]=='O':
            print("Player1 Won")
            t = 15
        else:
            print("Player2 Won")
            t = 15
        break
    elif list1[2]==list1[5]==list1[8]  and list1[2]!="-":
        if list1[2]=='O':
            print("Player1 Won")
            t = 15
        else:
            print("Player2 Won")
            t = 15
        break
    elif list1[2]==list1[4]==list1[6] and list1[2]!="-":
        if list1[2]=='O':
            print("Player1 Won")
            t = 15
        else:
            print("Player2 Won")
            t = 15
        break

    else:
        continue


# print(t)

if t==10:
    print("Match Tied!")
