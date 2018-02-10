import random

def v_code():
    '''
    :return:
    '''
    ret = ""
    for i in range(5):
        num=random.randint(0,9)
        alf=chr(random.randint(65,122))
        s=str(random.choice([num,alf]))
        ret+=s
    return ret

print(v_code())