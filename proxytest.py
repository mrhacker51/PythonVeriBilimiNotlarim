import requests
import numpy as np
import matplotlib.pyplot as plt



def main():
	url = "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&country=all"
	f = open("proxies.txt","w")
	print(requests.get(url).text,file=f)
	f.close()
	f = open("proxies.txt","r").readlines()

	leng_list = range(len(f))
	numpy_array_ = np.array(leng_list)
	numpy_array = np.array(f)

	#plt.plot(numpy_array_,numpy_array,"g")

	#plt.xlabel("Leng")
	#plt.ylabel("Proxy")
	#plt.title("Proxy Figure")

	myfigure = plt.figure()
	figureA = myfigure.add_axes([0.2,0.2,0.9,0.9])
	figureA.plot(numpy_array_,numpy_array,"r--",label="Proxies")
	figureA.legend()
	figureA.set_xlabel("Leng")
	figureA.set_ylabel("Proxy")
	figureA.set_title("Proxy Figure")

	plt.show()



if __name__ == '__main__':
	main()








