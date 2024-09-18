
                        





def main():
    
    temp = []
    
    for i in range(4):
        tempe = float(input())
        escala = str(input()).upper()
        temp.append((tempe, escala))
        
    nova_lista = temp_kelvin(temp)
    print(nova_lista)

if __name__=='__main__':
    main()
        
    