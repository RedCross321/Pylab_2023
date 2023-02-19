def next_largest_coin(coin):
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25
def count_coins(total):
    """Возвращает кол-во вариантов размена total используя монеты по 1, 5, 10, 25 коп.
    Например 15 коп. можно разменять так:
    - 15 монет по 1 коп.
    - 10 монет по 1 коп. + 1 монета 5 коп.
    - 5 монет по 1 коп. + 2 по 5 коп.
    - 5 монет по 1 коп. + 1 по 10 коп.
    - 3 монеты по 5 коп.
    - 1 монета 5 коп. + 1 монета 10 коп.
    Итого 6 вариантов.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # как можно разменять рубль (100 копеек)?
    242
    >>> from construct_check import check
    >>> # нельзя использовать циклы
    >>> check(LAB_SOURCE_FILE, 'count_coins', ['While', 'For'])
    """
    def cc(amount, kindsOfCoins):
        if amount==0:
            return 1
        if amount<0 or kindsOfCoins==0:
            return 0
        else:
            return cc(amount, kindsOfCoins-1)+cc(amount-firstDenomination(kindsOfCoins), kindsOfCoins)
    def firstDenomination(kindsOfCoins):
        if kindsOfCoins==1:
            return 1
        elif kindsOfCoins==2:
            return 5
        elif kindsOfCoins==3:
            return 10
        else:
            return 25
    return cc(total, 4)
 
 
print(count_coins(20))
