from wtforms import ValidationError

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def revstr(s):
    newS = ""
    length = len(s)
    for i in range(1, length + 1):
        newS += s[length - i]
    return newS

def siretValidator(message=None):
    if not message:
        message = "The siret number is not valid."

    def _siretValidator(form, field):
        siret = ""
        s = field.data
        for i in s:
            if i == ' ':
                continue
            if is_int(i) == False:
                raise ValidationError(message)
            siret += i

        total = 0
        count = 1
        for i in revstr(siret):
            num = int(i)
            if count % 2 == 0:
                num = num * 2
            if num > 10:
                num -= 9
            count += 1
            total += num
        if total % 10 != 0:
            raise ValidationError(message)
                
    return _siretValidator
