# 이 코드대로 하면 l1과 l2의 자리수가 1 차이나는 것만 제대로 계산하므로 내 코드가 조금 더 적절할 듯
from linkedListFIFO import LinkedListFIFO
from node import Node


class LinkedListFIFOYield(LinkedListFIFO):
    def _printList(self):
        node = self.head
        while node:
            yield node.value #함수 안에서 yield를 사용하면 함수는 제너레이터가 되며 yield에는 값(변수)을 지정gka
            node = node.pointer


def sumlls(l1, l2):
    lsum = LinkedListFIFOYield()
    dig1 = l1.head
    dig2 = l2.head
    pointer = 0 # 내 코드에서 upper_val과 동일한 역할

    while dig1 and dig2:
        d1 = dig1.value
        d2 = dig2.value
        sum_d = d1 + d2 + pointer
        if sum_d > 9:
            pointer = sum_d // 10
            lsum.addNode(sum_d % 10)
        else:
            lsum.addNode(sum_d)
            pointer = 0

        dig1 = dig1.pointer
        dig2 = dig2.pointer

    if dig1:
        sum_d = pointer + dig1.value
        if sum_d > 9:
            lsum.addNode(sum_d % 10)
        else:
            lsum.addNode(sum_d)
        dig1 = dig1.pointer

    if dig2:
        sum_d = pointer + dig2.value
        if sum_d > 9:
            lsum.addNode(sum_d % 10)
        else:
            lsum.addNode(sum_d)
        dig2 = dig2.pointer

    return lsum


if __name__ == "__main__":
    l1 = LinkedListFIFOYield()  # 2671
    l1.addNode(1)
    l1.addNode(7)
    l1.addNode(6)
    l1.addNode(2)
    #l1.addNode(1)

    l2 = LinkedListFIFOYield()  # 455
    l2.addNode(5)
    l2.addNode(5)
    l2.addNode(4)

    lsum = sumlls(l1, l2)
    l = list(lsum._printList())
    for i in reversed(l):
        print(i, end="")
    print()
