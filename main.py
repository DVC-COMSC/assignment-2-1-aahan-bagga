def main():
    m = int(input("males: "))
    f = int(input("females: "))

    m_perc = m / (m+f) * 100
    f_perc = f / (m+f) * 100
    print(f"Total students: {m+f}")
    print(f"Number males: {m}")
    print(f"Number females: {f}")
    print(f'Percentage of males and females: {m_perc:.2f} {f_perc:.2f}')
    """

    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """

    return m_perc, f_perc


if __name__ == '__main__':
    main()
