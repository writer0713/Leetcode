class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        match = list(strs[0]) # ["f, l, o, w, e ,r"]
        for word in strs:
            size = len(word)

            match = match[:size]

            for idx in range(len(match)):

                if word[idx] == match[idx]:
                    continue
                else:
                    match[idx] = ''

        result = ""
        for x in match:
            if x == '':
                break
            else:
                result += x

        print(result)
        return result

                

            
                


