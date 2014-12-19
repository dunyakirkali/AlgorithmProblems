import sys
def palindex(string):
    for i in range(len(string)//2):
        if string[i] != string[-1*(i+1)]:
            if string[i+1] == string[-1*(i+1)]:
                return i
                
            else:
                return (len(string) - (i+1))
    return -1


def main():
    #inp = sys.stdin.read()
    inp = """3
aaab
baa
aaa"""
    inplist = []
    for line in inp.split('\n')[1:]:
        print(palindex(line))

main()