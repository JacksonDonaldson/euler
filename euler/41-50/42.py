import time
current=time.time()
words = open('42.txt', 'r')
wordlist = words.read();
ap='';
done=[];
for text in wordlist:
    if text == '"':
        if ap:
            mode = False
            done.append(ap);
            ap='';
        else:
            mode= True
            
            continue
    if mode:
        ap+=text;
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];
for letter in letters:
    letters[letters.index(letter)] = letter.upper()

triangles=[];
for i in range(0,19):
    triangles.append((0.5*i)*(i+1));


triwords=0;
for word in done:
    total = 0;
    for j in word:
        total+=letters.index(j)+1;
    if total in triangles:
        triwords+=1;
print(triwords)
print(time.time()-current);
