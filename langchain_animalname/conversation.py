from .input_message import input_message


def conversation(cute_object, chain):
    end_request = False

    while end_request == False:
        request_target = input_message(cute_object)
        if request_target == "おわり":
            end_request = True
            continue
        print(chain.run(request_target))

    print("ばいばい！")
