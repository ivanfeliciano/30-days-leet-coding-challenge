class Solution:
    def backspaceCompare(self, S, T):
        stack_s = ""
        stack_t = ""
        for i in range(len(S)):
            if S[i] != "#": stack_s += S[i]
            if i > 0 and S[i] == "#":
                stack_s = stack_s[:-1]
        for i in range(len(T)):
            if T[i] != "#": stack_t += T[i]
            if i > 0 and T[i] == "#":
                stack_t = stack_t[:-1]
        return stack_s == stack_t

def main():
    S = "a#c"
    T = "b"
    print(Solution().backspaceCompare(S, T))
if __name__ == '__main__':
    main()