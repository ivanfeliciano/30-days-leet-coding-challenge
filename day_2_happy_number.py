
class Solution:
    def isHappy(self, n):
        while n != 4:
            if n == 1: return True
            n = sum([int(i) ** 2 for i in str(n)])
        return False

def main():
    print(Solution().isHappy(4))
    for i in range(1, 100):
        if Solution().isHappy(i):
            print(i)
if __name__ == '__main__':
    main()