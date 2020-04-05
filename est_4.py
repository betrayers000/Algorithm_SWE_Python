def solution(S, C):
    names = S.split("; ")
    candidates = {}
    result = ""
    for name in names:
        temp = name.split(" ")
        mail = temp[-1].replace("-", "").lower() + '_' + temp[0].lower() + '@' + C.lower() + '.com'
        if candidates.get(mail):
            mail_temp = temp[-1].replace("-", "").lower() + '_' + temp[0].lower() + str(candidates[mail][-1]+1) + '@' + C.lower() + '.com'
            candidates[mail_temp] = [name, 1]
            candidates[mail][-1] += 1
            mail = mail_temp
        else :
            candidates[mail] = [name, 1]
        result += name + " <" + mail + ">; "
    return result[:-2]



name_list = 'John Doe; Peter Benjamin Parker; Mary Jane Watson-Parker; John Elvis Doe; John Evan Doe; Jane Doe; Peter Brian Parker'
company = 'Example'

print(solution(name_list, company))