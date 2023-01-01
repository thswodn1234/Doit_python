

import re

sentence = 'I love a lovely dog, readlly. Iam not telling a lie. What a pretty dog! I love this dog.'

res = re.sub(r'dog','cat',sentence)

print(res)