""" 
메모리 누수 leak 

가비지 컬렉션으로도 메모리 누수가 발생할 수 있는 경우 중 하나는 순환 참조(Reference Cycle)입니다. 
순환 참조는 서로를 참조하는 객체들 사이에 발생하는 상황으로, 
가비지 컬렉션 시스템이 이를 탐지하지 못하고 회수하지 못하는 메모리 누수를 초래할 수 있습니다.

"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# 순환 참조가 발생하는 객체 생성
node1 = Node(1)
node2 = Node(2)
node1.next = node2
node2.next = node1

# 순환 참조로 인한 메모리 누수 발생

"""
위의 코드의 메모리 누수를 수정하기 위해서는 순환참조를 끊어주어야 합니다.
아래의 코드처럼 참조를 해제해서 메모리 누수없이 객체를 회수하게 만들어야 합니다.
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# 순환 참조가 발생하는 객체 생성
node1 = Node(1)
node2 = Node(2)
node1.next = node2
node2.next = node1

# 순환 참조 해제
node1.next = None
node2.next = None

# 가비지 컬렉션 실행하여 메모리 회수
