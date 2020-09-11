#創建文件+內容
def build_1():
    Output1="1.txt"
    with open(Output1, 'w') as outfile:
            outfile.write('{\n')
            outfile.write(' "1": "1",\n')
            outfile.write(' "2": "2",\n')
            outfile.write(' "3": "3",\n')
            outfile.write('}')

#f = open('C:\\Users\\ness_huang\\Desktop\\讀取文字內容\\1.txt','r')
f = open("1.txt","r")

build_1()
line = f.read()
print(line)
input()
f.close()
