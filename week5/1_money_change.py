# Created by: René Vilar S.
# Algorithmic Toolbox - Coursera 2021
def get_change(m):
    #write your code here
    return m // 4

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))