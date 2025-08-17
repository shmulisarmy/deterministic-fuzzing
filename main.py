def add(a: int, b: int) -> int:
    return a + b




import random, json, os
random_gen = {
    int: lambda: random.randint(0, 100),
    str: lambda: random.shuffle(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
}




def confirm_cases(func: callable):
    previous_cases_info = {} 
    with open(f"fuzz/{func.__name__}.json", "r") as f:
        previous_cases_info = json.loads(f.read())
    for case in previous_cases_info["all_test_case_call_instances"]:
        print(f"{case=}")
        assert func(*list(case.values())[:-1]) == case["return"]



def create_testing_info(func: callable, test_count: int = 100):
    arg_collection = []
    arg_names = list(func.__annotations__.keys())

    test_info_json = {"all_test_case_call_instances": []}
    for _ in range(test_count):
        j = {

        }
        arg_collection.clear()
        for arg, type_ in func.__annotations__.items():
            arg_collection.append(random_gen[type_]())

        for i, arg in enumerate(arg_names):
            j[arg] = arg_collection[i]

        print(f"{j = }")
        del j["return"]
        arg_collection.pop()
        j["return"] = func(*arg_collection)

        test_info_json["all_test_case_call_instances"].append(j)

    if not os.path.exists("fuzz"):
        os.system("mkdir fuzz")

    with open(f"fuzz/{func.__name__}.json", "w") as f:
        f.write(json.dumps(test_info_json))

create_testing_info(add)