from bs4 import BeautifulSoup
import os

def main():
    sortings = []
    for i in os.listdir("./tables/"):
        sortings += takeSortings(readHtml(i.split(".")[0]))
    """s1 = takeSortings(readHtml("table1"))
    s2 = takeSortings(readHtml("table2"))
    s3 = takeSortings(readHtml("table3"))
    s4 = takeSortings(readHtml("table4"))"""
    x = []
    for i in sortings:
        avr = marginsToAverage(i)
        if avr:
            x += marginsToAverage(i)
    total = 0
    #print(x)
    for i in x:
        total += i
    percenstage = total/len(x)
    print(f"Total: {total}\n Lenght Of X: {len(x)}")
    print(percenstage)

def readHtml(fName:str) -> str:
    print(f"Reading HTML string from {fName}...")
    with open(f"./{fName}.html", "r") as f:
        html = f.read()
        f.close()
    return html

def takeSortings(html:str) -> list:
    print("Taking sortings from HTML string...")
    soup = BeautifulSoup(html, features="html.parser")
    trS = soup.find_all("tr")
    sortings = []
    for i in trS:
        lst = i.find_all("td", class_="dt-center vcenter")[8].find_all("font")
        newLst = []
        for i in lst:
            newLst.append(i.text)
        sortings.append(newLst)

    return sortings
        
def marginsToAverage(arr:list) -> list: 
    arr = normalizeList(arr)
    

    newArr = []
    for i in arr:
        newArr.append(int(i))

    if len(newArr) > 1:
        before = newArr[0]
        i = 1
        lst = []
        while i < len(newArr):
            lst.append(round((-((before - newArr[i])))/before*100, 2))
            before = newArr[i]
            i += 1

        return lst

def normalizeList(arr:list):
    newArr = []
    k = 0
    while k < len(arr):
        bl = True
        try:
            int(arr[k].replace(".",""))
        except:
            bl = False
            del arr[k]
        if bl:
            newArr.append(arr[k].replace(".",""))
        k += 1
    
    return newArr
    
main()
