import os
os.chdir('C:\Users\User\Joker vs Thanos\Dataset\train\joker')
#os.chdir('C:\Users\User\Joker vs Thanos\Dataset\train\thanos')
i=1
for file in os.listdir():
    src=file
    dst="2"+"_"+str(i)+".jpg"
    os.rename(src,dst)
    i+=1

