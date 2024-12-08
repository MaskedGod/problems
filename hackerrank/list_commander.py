if __name__ == '__main__':
    wrk_list = []
    N = int(input())

    for _ in range(N):
        command_input = input().split(" ")
        command = command_input[0]

        if len(command_input) == 2:
            num = int(command_input[1])
        elif len(command_input) > 2:
            i = int(command_input[1])
            num = int(command_input[2])

        match command:
            case "insert":
                wrk_list.insert(i, num)
            case "print":
                print(wrk_list)
            case "remove":
                wrk_list.remove(num)
            case "append":
                wrk_list.append(num)
            case "sort":
                wrk_list.sort()
            case "pop":
                wrk_list.pop()
            case "reverse":
                wrk_list.reverse()