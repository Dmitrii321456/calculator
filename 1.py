def count_smileys(arr):
    valid_list = [':)', ':D', ';-D', ':~)']
    count = 0
    r = list((arr.count(x) for x in valid_list if x in ()))
    return print(r)

r = [':D',':~)',';~D',':)']
count_smileys(r)