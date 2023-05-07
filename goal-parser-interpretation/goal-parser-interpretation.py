class Solution:
    def interpret(self, command: str) -> str:

        idx = 0
        result = ""

        while idx <= len(command) - 1:

            if command[idx] == "G":
                result += "G"
            elif command[idx] == "(" and command[idx + 1] == ")":
                result += "o"
            elif command[idx] == "(" and command[idx + 1] != ")":
                result += "al"

            idx += 1

        return result




        