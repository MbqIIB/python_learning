import exlotto
def output(m, n):
    nums = exlotto.lotto(m, n)
    snums = sorted(nums)   
    return snums

#跑一萬次出現最多的數字六個
if __name__ == '__main__':
    import operator    
    lilotto = list()
    dictlotto = {}
    for i in range(10000):
        #將新的list加入
        lilotto.extend(output(48,6))

    #統計每個數字出現的次數
    myset = set(lilotto)
    for item in myset:
        dictlotto[item] = lilotto.count(item)

    #使用operator 排序dict的value
    sorted_x = sorted(dictlotto.items(), key=operator.itemgetter(1))
    print(sorted_x)

            
