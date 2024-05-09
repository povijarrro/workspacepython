#!python

def secret(text):
    res = ''
    for ch in text:
        v = ch in 'aAáÁeEéÉiIíÍyYýÝoOóÓuUúÚ'
        res += ch.replace(ch, ch+('p'+ch)*(int(v)))
    return res


print(secret("Toto je tajná reč."))