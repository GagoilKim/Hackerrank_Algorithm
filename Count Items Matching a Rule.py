class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        for i in range(len(items)):
            value = ""
            if ruleKey == "type":
                value = items[i][0]
            elif ruleKey == "color":
                value = items[i][1]
            else:
                value = items[i][2]
            if value == ruleValue:
                count += 1
            else:
                continue
        return count