from matplotlib import pyplot as plt
k={'Pavan':314,'Prakash':400,'Jeevitha':430,'Hema':245}
l=list(k.keys())
m=list(k.values())
plt.figure(figsize=(30,30))
plt.pie(m,labels=l,autopct='%0.0f%%',shadow='true')
plt.show()
