#import eng_to_ipa as ipa
import re, requests, time
t = open("kjv-red.yet","r").read()
tt = ""
tl = re.compile("(?:^.*$\n?){1,1000}",re.M).findall(t)
for i in tl:
    t = time.time()
    #tt += ipa.convert(i) + '\n'
    open("kjv-red-convipa-notfixed.txt","a").write(requests.get("https://tophonetics-api.ajlee.repl.co/api", data={"text": i}).text + '\n')
    print(i[:20])
    print(time.time()-t)
