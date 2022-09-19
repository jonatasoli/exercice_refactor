def validate_cpf(cpf) -> bool:
    """Validate CPF Module"""
    if cpf != None:
        if len(cpf) >= 11 and len(cpf) <= 14:
            cpf = (
                cpf.replace('.', '')
                .replace('.', '')
                .replace('-', '')
                .replace(' ', '')
            )
            if not len(set(cpf)) == 1:
                try:
                    check_fist_digit = check_second_digit = 0
                    first_digit = second_digit = rest_number_checker = 0
                    digit_index = None
                    digit_number_checker_solution = None

                    for cpf_index in range(1, (len(cpf) - 1)):

                        digit_index = int(cpf[cpf_index - 1 : cpf_index])
                        check_fist_digit = (
                            check_fist_digit + (11 - cpf_index) * digit_index
                        )

                        check_second_digit = (
                            check_second_digit + (12 - cpf_index) * digit_index
                        )

                    rest_number_checker = check_fist_digit % 11

                    first_digit = first_digit = (
                        0
                        if rest_number_checker < 2
                        else 11 - rest_number_checker
                    )
                    check_second_digit += 2 * first_digit
                    rest_number_checker = check_second_digit % 11
                    if rest_number_checker < 2:
                        second_digit = 0
                    else:
                        second_digit = 11 - rest_number_checker

                    digit_number_checker = cpf[len(cpf) - 2 : len(cpf)]
                    digit_number_checker_solution = (
                        '' + str(first_digit) + '' + str(second_digit)
                    )
                    return (
                        digit_number_checker == digit_number_checker_solution
                    )
                except Exception as e:
                    print('Erro !' + str(e))

                    return False

            else:
                return False

        else:
            return False

    else:
        return False
