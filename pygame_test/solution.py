'''ym15d'''

def run_length_encode(a):
    encoded = []
    i = 0

    while i < len(a):
        ch = a[i]
        count = 0
        while i < len(a) and ch == a[i]:
            count += 1
            i += 1

        if count > 1:
            encoded.append(ch)
            encoded.append(str(count))
        else:
            encoded.append(ch)

    return ''.join(encoded)


def run_length_decode(a):
    decoded = []

    for i in range(len(a)):
        if a[i].isdigit():
            continue

        elif i + 1 < len(a) and a[i + 1].isdigit():
            for j in range(int(a[i + 1])):
                decoded.append(a[i])
        else:
            decoded.append(a[i])

    return ''.join(decoded)

print(run_length_decode('W3ABC'))