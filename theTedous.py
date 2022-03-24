def tedious(elements):
    for i in  elements:
        if i=='':
            continue
        elem=i.split(';')
        if elem[0]=='C':
            if elem[1]=='V':
                word=elem[2]
                req=word.split(' ')
                dem=req[0]
                for i in range(1,len(req)):
                    dem=dem+ req[i][:1].upper() + req[i][1:]
                print(dem)
            if elem[1]=='C':
                word=elem[2]
                words=word.split(' ')
                des=''
                for i in words:
                    des=des+ i[:1].upper() + i[1:]
                print(des)
            if elem[1]=='M':
                word=elem[2]
                words=word.split(' ')
                des=words[0]
                for i in range(1,len(words)):
                    des=des+ words[i][:1].upper() + words[i][1:]
                print(des+'()')
        elif elem[0]=='S':
            if elem[1]=='V':
                desmo=elem[2]
                demo=''
                arr=[]
                final=''
                for i in desmo:
                    if i.islower():
                        demo=demo + i
                    elif i.isupper():
                        arr.append(demo)
                        demo=i.lower()
                else: arr.append(demo)
                for i in arr:
                    if i!='':
                      final=final + i +' '
                    else:pass
                print(final)
            if elem[1]=='C':
                desmo=elem[2]
                demo=''
                arr=[]
                final=''
                for i in desmo:
                    if i.islower():
                        demo=demo + i
                    # elif i.isupper():
                    #     arr.append(demo)
                    #     demo=i.lower()
                    else:
                       if demo != '':
                           arr.append(demo)
                           demo=''
                           demo=i.lower()
                       else: 
                           demo=i.lower()
                else: arr.append(demo)
                for i in arr:
                    if i!='':
                      final=final + i +' '
                    else:pass
                print(final)
            if elem[1]=='M':
                desmo=elem[2]
                demo=''
                arr=[]
                final=''
                for i in desmo:
                    if i.islower():
                        demo=demo + i
                    # elif i.isupper():
                    #     arr.append(demo)
                    #     demo=i.lower()
                    else:
                       if demo != '':
                           arr.append(demo)
                           demo=''
                           demo=i.lower()
                       else: 
                           demo=i.lower()
                else: arr.append(demo)
                for i in arr:
                    if i!='':
                      final=final + i +' '
                    else:pass
                print(final[:-5])


# fire=['S;V;iPad','C;M;mouse pad','C;C;code swarm','S;C;OrangeHighlighter'] 
                     

# tedious(fire)
