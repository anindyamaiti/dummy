from datetime import datetime

date = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')

myFileName = date+'.txt'

print(myFileName)

file = open(myFileName, 'w')

file.write(myFileName)

file.close()
