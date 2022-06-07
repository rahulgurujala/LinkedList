from __future__ import annotations


class Node:
    def __init__(self, data: int | float = None, link: "Node" = None):
        """Value of data and link is none if no data is passed

        :param data: Input data, defaults to None
        :type data: int | float, optional
        :param link: `LinkedList` Node, defaults to None
        :type link: Node, optional
        """

        self.data = data
        self.link = link

    def updateData(self, data: int | float) -> None:
        """Update the data field of Node

        :param data: Input Data
        :type data: int | float
        """

        self.data = data

    def setLink(self, node: "Node") -> None:
        """set Link field of the Node

        :param node: `LinkedList` Node
        :type node: Node
        """

        self.link = node

    def getData(self) -> int | float:
        """Data field of the Node

        :return: data field of the Node
        :rtype: int | float
        """
        return self.data

    def getNextNode(self) -> "Node":
        """Address of the next Node

        :return: Returns address of the next Node
        :rtype: Node
        """

        return self.link


class LinkedList:
    def __init__(self) -> None:
        """`LinkedList`"""
        self.head = None

    def prepend(self, data: int | float) -> "LinkedList":
        """Adds elements to the left of the `LinkedList`

        :param data: Input Data
        :type data: int | float
        :return: Self `LinkedList`
        :rtype: `LinkedList`
        """

        tempNode = Node(data)
        tempNode.setLink(self.head)
        self.head = tempNode
        del tempNode
        return self

    def append(self, data: int | float) -> "LinkedList":
        """Adds elements to the right of the `LinkedList`

        :param data: Input Data
        :type data: int | float
        :return: Self `LinkedList`
        :rtype: `LinkedList`
        """

        start = self.head
        tempNode = Node(data)
        while start.getNextNode():
            start = start.getNextNode()
        start.setLink(tempNode)
        del tempNode
        return self

    def __str__(self) -> str:
        start = self.head
        if start is None:
            return "<LinkedList()>"

        stack = [start.getData()]
        while start:
            start = start.link
            if start:
                stack.append(start.getData())
        return f"<LinkedList({stack})>"

    def length(self) -> int:
        """Length of `linkedList`

        :return: Returns length of `linkedList`
        :rtype: int
        """

        start = self.head
        size = 0
        while start:
            size += 1
            start = start.getNextNode()
        return size

    def __len__(self):
        """Length of `linkedList`

        :return: Returns length of `linkedList`
        :rtype: int
        """

        return self.length()

    def index(self, data: int | float) -> int:
        """Index of the received data

        :param data: Input Data
        :type data: int | float
        :return: Returns index of the received data
        :rtype: int
        """

        start = self.head
        position = 1

        while start:
            if start.getData() == data:
                return position
            position += 1
            start = start.getNextNode()

    def remove(self, item: int | float) -> "LinkedList":
        """Removes item passed from the `LinkedList`

        :param item: Input Data
        :type item: int | float
        :return: Removes item passed from the `LinkedList`
        :rtype: `LinkedList`
        """

        start = self.head
        previous = None
        found = False

        while not found:
            if start.getData() == item:
                found = True
            else:
                previous = start
                start = start.getNextNode()

        if previous is None:
            self.head = start.getNextNode()
        else:
            previous.setLink(start.getNextNode())
        return self

    def Max(self) -> int | float:
        """Maximum element of `LinkedList`

        :return: Returns maximum element of `LinkedList`
        :rtype: int | float
        """

        start = self.head
        largest = start.getData()
        while start:
            if largest < start.getData():
                largest = start.getData()
            start = start.getNextNode()
        return largest

    def Min(self) -> int | float:
        """Minimum element of `LinkedList`

        :return: Returns minimum element of `LinkedList`
        :rtype: int | float
        """

        start = self.head
        smallest = start.getData()
        while start:
            if smallest > start.getData():
                smallest = start.getData()
            start = start.getNextNode()
        return smallest

    def push(self, data: int | float) -> "LinkedList":
        """Pushes element to the `LinkedList`

        :param data: Input Data
        :type data: int | float
        :return: Pushes element to the `LinkedList`
        :rtype: `LinkedList`
        """

        self.append(data)
        return self

    def pop(self) -> int | float:
        """Removes and returns the last element from the `LinkedList`

        :return: Returns the last element from the `LinkedList`
        :rtype: int | float
        """

        start = self.head
        previous = None

        while start.getNextNode():
            previous = start
            start = start.getNextNode()

        if previous is None:
            self.head = None
        else:
            previous.setLink(None)
            data = start.getData()
            del start
            return data

    def atIndex(self, position: int) -> int | float:
        """The element at given position

        :param position: Position of element
        :type position: int
        :return: Returns the element at given position
        :rtype: int | float
        """

        start = self.head
        position = position
        pos = 0
        while pos != position:
            start = start.getNextNode()
            pos += 1

        return start.getData()

    def copy(self) -> "LinkedList":
        """Copy of the current `LinkedList`

        :return: Copy of the current `LinkedList`
        :rtype: `LinkedList`
        """

        temp = LinkedList()
        start = self.head

        temp.prepend(start.getData())
        while start := start.getNextNode():
            temp.append(start.getData())
        return temp

    def clear(self) -> True:
        """Clear `LinkedList`

        :return: True after clear
        :rtype: True
        """

        self.head = None
        return True

    def removePosition(self, position: int) -> int | float:
        """Returns and removes element at received position

        :param position: Position of element for remove
        :type position: int
        :return: Returns and removes element at received position
        :rtype: int | float
        """

        data = self.atIndex(position)
        self.remove(data)
        return data

    def toString(self, separator: str = ", ") -> str:
        """Convert `LinkedList` into string object with given separator.

        :param separator: Separator of `LinkedList` element, defaults to ", "
        :type separator: str, optional
        :return: `LinkedList` in string format
        :rtype: str
        """

        start = self.head
        finalString = ""
        while start:
            tempString = start.getData()
            finalString += str(tempString)
            start = start.getNextNode()

            if start:
                finalString += separator

        return finalString

    def count(self, element) -> int:
        """The occurrences of a given element

        :param element: Input element
        :type element: _type_
        :return: Returns the occurrences of a given element
        :rtype: int
        """

        start = self.head
        count1 = 0
        while start:
            if start.getData() == element:
                count1 += 1
            start = start.getNextNode()
        return count1

    def toList(self) -> list:
        """Convert to builtin List of python consisting of Elements of `LinkedList`

        :return: Returns builtin List of python consisting of Elements of `LinkedList`
        :rtype: list
        """

        start = self.head
        tempList = []
        while start:
            tempElement = start.getData()
            tempList.append(tempElement)
            start = start.getNextNode()
        return tempList

    def toSet(self) -> set:
        """Convert to builtin Set of python consisting of Elements of `LinkedList`

        :return: Returns builtin Set of python consisting of Elements of `LinkedList`
        :rtype: set
        """

        start = self.head
        tempSet = set()
        while start:
            tempElement = start.getData()
            if tempElement not in tempSet:
                tempSet.add(tempElement)
            start = start.getNextNode()
        return tempSet

    def reverse(self) -> None:
        """Reverses the `LinkedList` inplace

        :return: Reversed the `LinkedList`
        :rtype: None
        """

        start = self.head
        tempNode = None
        previousNode = None

        while start:
            tempNode = start.getNextNode()
            start.setLink(previousNode)
            previousNode = start
            start = tempNode

        self.head = previousNode

    def sort(self) -> None:
        """Sorts `LinkedList` inplace"""
        start = self.head
        beginNode = start
        while beginNode:
            tempNode = beginNode
            tempNode2 = beginNode
            smallest = beginNode.getData()
            while tempNode:
                if smallest > tempNode.getData():
                    smallest = tempNode.getData()
                    tempNode2 = tempNode
                tempNode = tempNode.getNextNode()

            temp = beginNode.getData()
            beginNode.updateData(tempNode2.getData())
            tempNode2.updateData(temp)

            beginNode = beginNode.getNextNode()

    def sorted(self) -> "LinkedList":
        """Create New instance of the sorted `LinkedList` without changing original `LinkedList`

        :return: New instance of the sorted `LinkedList` without changing original `LinkedList`
        :rtype: `LinkedList`
        """

        tempList = self.copy()
        tempList.sort()
        return tempList


if __name__ == "__main__":

    linkedlist = LinkedList()
    start_data = [1, 2, 3, 4, 5]
    end_data = [6, 7, 8, 9, 10]

    for i in start_data[::-1]:
        linkedlist.prepend(i)

    for i in end_data:
        linkedlist.append(i)

    print(linkedlist)
