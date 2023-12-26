from datetime import datetime

newdate= "23 december 2023"
x = datetime.strptime(newdate,"%d/%m/%Y")
print(x)