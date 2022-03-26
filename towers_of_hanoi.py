def hanoi(n, source, helper, target):
    if n > 0:
        # move tower except last disk to the helper pole
        hanoi(n-1, source, target, helper)

        # move final large disk to the target pole
        target.append(source.pop())

        print(A, B, C)

        # move remaining smaller tower from helper to target
        hanoi(n-1, helper, source, target)


A = [4, 3, 2, 1]
B = []
C = []

hanoi(len(A), A, B, C)
