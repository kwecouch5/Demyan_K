def mergeTwoLists(list1,list2):
    dummy = ListNode()
    current = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # Добавляем оставшиеся узлы
    current.next = list1 if list1 else list2

    return dummy.next
print(mergeTwoLists([1,5,7],[1,2,3,7,8]))