class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while len(stack) != 0 and stack[-1] > 0 and a < 0:
                if stack[-1] < abs(a):
                    stack.pop()
                    continue
                elif stack[-1] == abs(a):
                    stack.pop()
                break

            else:
                stack.append(a)
        
        print(stack)

        return stack


