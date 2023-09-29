import module_four as m


def create_f_ext(nums_and_extensions = (), path = ""):
    for item in nums_and_extensions:
        m.create_files(extension=item[0], num_of_files=item[1],pathname=path)


create_f_ext(nums_and_extensions = ((".txt", 3),(".py",4)))

