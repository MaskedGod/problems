from re import findall
def count_smileys_re(arr):
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))

list = [';o(', ':D', ':-(', ':-D', ':(', ';D', ';oD', ':(', ':(', ':D', ';(', ';oD', ':(', ';o(', ';D']

def count_smileys(arr):
    valid = [[':', ';'], [ 'D',  ')']]
    count = 0
    for face in arr:
        if face[0] in valid[0] and face[-1] in valid[1]:
            count += 1
    return count


print(count_smileys(list))