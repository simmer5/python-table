s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
action=""
def print_horiz_line():
    print( " --- --- ---")

def table():

    print_horiz_line()
    print ('|', s[0],'|', s[1],'|', s[2], '|' )
    print_horiz_line()
    print ('|', s[3],'|', s[4],'|', s[5], '|' )
    print_horiz_line()
    print ('|', s[6],'|', s[7],'|', s[8], '|' )
    print_horiz_line()

table()

del_nr = []
counter=0


while action != "0":
    print ("Exit - 0, del - d, add - a, exampl: d2, a2 ")
    action = input()
    
    if action =="0":
        print ("EXIT")
        break
    sk=int(action[1])
    if action[0] == "d":
        d_sk = sk
        s[d_sk-1]="X"
        del_nr.append(d_sk)
        counter=del_nr.count(d_sk)
        
        if counter>2:
            print ("Number "+ str(d_sk) +" has been deleted more the two times!")
            s[d_sk-1]=d_sk
        table()
    if action[0] == "a":
        s[sk - 1] = sk
        table()
