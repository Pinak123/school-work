def theTedious(element):
    for i in element:

       elem=i.split(';')
       if elem[0] == 'C':
           if elem[1] == 'V':
              word=elem[2]
              word=word.split(' ')
              des=word[0]
              for i in range(1,len(word)) :
                  des=des + word[i][:1].upper() + word[i][1:]
   
              print (des)
           
           if elem[1] == 'C':
              word=elem[2]
              word=word.split(' ')
              des=''
              for i in range(len(word)) :
                  des=des + word[i][:1].upper() + word[i][1:]
   
              print (des , word )
           if elem[1] == 'M':
              word=elem[2]
              word=word.split(' ')
              des=word[0]
              for i in range(1,len(word)) :
                  des=des + word[i][:1].upper() + word[i][1:]
   
              print(des +'()')
   
   
       else:
           if elem[1] == 'V':
               word=elem[2]
               demo=''
               des=[]
               final=''
               for i in word:
                   
                   if i.islower():
                       demo=demo + i
                   else:
                       des.append(demo)
                       demo=''
                       demo=i.lower()
               else: des.append(demo)
               for i in des:
                   final=final + i +' '
               print(final)
           if elem[1]=='C':
               word=elem[2]
               demo=''
               des=[]
               final=''
               for i in word:
                   
                   if i.islower():
                       demo=demo + i
                   else:
                       des.append(demo)
                       demo=''
                       demo=i.lower()
               else: des.append(demo)
               for i in des:
                   final=final + i +' '
               print(final) 
           else: 
               word=elem[2]
               demo=''
               des=[]
               final=''
               for i in word:
                   
                   if i.islower():
                       demo=demo + i
                   else:
                       des.append(demo)
                       demo=''
                       demo=i.lower()
               else: des.append(demo)
               for i in des:
                   final=final + i +' '
               print (final[:-5])
   
fire=['S;V;iPad','C;M;mouse pad','C;C;code swarm','S;C;OrangeHighlighter']   
# inputData = [line.rstrip('\n\r') for line in sys.stdin.readlines()]
   
print(theTedious(fire))




        

