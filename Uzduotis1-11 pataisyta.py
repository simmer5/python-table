s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
veiksmas=""
def print_horiz_line():
    print( " --- --- ---")

def print_vert_line():
    print( "| " * (3 + 1) )

def lentele():

    print_horiz_line()
    print ('|', s[0],'|', s[1],'|', s[2], '|' )
    print_horiz_line()
    print ('|', s[3],'|', s[4],'|', s[5], '|' )
    print_horiz_line()
    print ('|', s[6],'|', s[7],'|', s[8], '|' )
    print_horiz_line()

lentele()

istrinti_sk = []
istr_sk_kiekis=0


while veiksmas != "0":
    print ("Exit - 0, Pasirink istrinti - d ar prideti - a, pvz. d2: ")
    veiksmas = input()
    
    if veiksmas =="0":
        print ("EXIT")
        break
    sk=int(veiksmas[1])
    if veiksmas[0] == "d":
        d_sk = sk
        s[d_sk-1]="X"
        istrinti_sk.append(d_sk)
        istr_sk_kiekis=istrinti_sk.count(d_sk)
        
        if istr_sk_kiekis>2:
            print ("Skaiciu "+ str(d_sk) +" istrynei jau daugiau nei du kartus")
            s[d_sk-1]=d_sk
        lentele()
    if veiksmas[0] == "a":
        s[sk - 1] = sk
        lentele()
       




