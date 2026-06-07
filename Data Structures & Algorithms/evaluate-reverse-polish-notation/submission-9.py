from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        ops = ("+","-","*","/")

        def eval(a,b,n):
            a,b = int(a),int(b)
            match n:
                case '+':
                    return a+b
                case '-':
                    return b-a
                case '*':
                    return a*b
                case '/':
                    return int(b/a)


        for n in tokens:
            if n not in ops:
                stack.append(n)
                print(stack)
            else:
                a = stack.pop()
                b = stack.pop()
                print(a,b,n)
                stack.append(eval(a,b,n))
                print(stack)
        print(stack)
        ans = stack.pop()
        return int(ans)

