

from xml.etree.ElementTree import tostring


def seq_num_format(i):
    message = str(i)
    while len(message) < 7:
        message = "0" + message

    return message

def main():
    for i in range(1000):
        print(seq_num_format(i))

main()