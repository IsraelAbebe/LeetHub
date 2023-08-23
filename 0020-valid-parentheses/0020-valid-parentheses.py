class Solution:
    def isValid(self, s: str) -> bool:
        bucket = []
        values = {
            'open': list('({['),
            'close':list(')}]')
        }

        for i in list(s):
            if len(bucket) ==0:
                if i in values['open']:
                    bucket.append(i)
                else:
                    return False
            else:
                if i in values['open']:
                    bucket.append(i)
                else:
                    if bucket[-1] == values['open'][values['close'].index(i)]:
                        bucket.pop()
                    else:
                        return False
        return True if len(bucket)==0 else False

