class Solution:
    def interpret(self, command: str) -> str:

        idx = 0
        result = ""

        while idx <= len(command) - 1:

            if command[idx] == "G":
                result += "G"
            elif command[idx] == "(" and command[idx + 1] == ")":
                result += "o"
                idx += 1
            else: # (al)
                result += "al"
                idx += 3

            idx += 1

        return result




        