import sys
from pathlib import Path


EASY, MEDIUM, HARD = [], [], []                 # 三种难度的题目
ALIGN_BASE_ONE, ALIGN_BASE_TWO = 28, 29         # 对齐基数
P = Path("./src")                               # 默认路径


def summary(verbose: bool):
    '''遍历文件，统计题目信息'''
    for file in P.iterdir():
        number, name, difficulty = file.name.split("-")
        if difficulty == 'E':
            EASY.append((number, name, '简单'))
        elif difficulty == 'M':
            MEDIUM.append((number, name, '中等'))
        else:
            HARD.append((number, name, '困难'))
        
        if verbose:
            EASY.sort(key=lambda x: int(x[0]))
            MEDIUM.sort(key=lambda x: int(x[0]))
            HARD.sort(key=lambda x: int(x[0]))


def countsGBK(name: str) -> int:
    '''统计题目中汉字的个数'''
    return sum(map(lambda ch: 1, filter(lambda ch: 0x4E00 <= ord(ch) <= 0x9FA5, name)))


def printMsg(verbose: bool):
    '''打印统计信息'''
    if not verbose:
        print(f'统计'.center(88, '-'))
        print(f'{"简单:":<8}{len(EASY):5}')
        print(f'{"中等:":<8}{len(MEDIUM):5}')
        print(f'{"困难:":<8}{len(HARD):5}')
        return

    print('-'*90)
    print('|', end='')
    print(f'{"题号":^{ALIGN_BASE_ONE - 2}}', end='')
    print('|', end='')
    print(f'{"题目":^{ALIGN_BASE_TWO - 2}}', end='')
    print('|', end='')
    print(f'{"难度":^{ALIGN_BASE_TWO - 2}}', end='')
    print('|')
    print('-'*90)
        
    for term in [EASY, MEDIUM, HARD]:
        for item in term:
            print('|', end='')
            print(f'{item[0]:^{ALIGN_BASE_ONE - countsGBK(item[0])}}', end='')
            print('|', end='')
            print(f'{item[1]:^{ALIGN_BASE_TWO - countsGBK(item[1])}}', end='')
            print('|', end='')
            print(f'{item[2]:^{ALIGN_BASE_TWO - countsGBK(item[2])}}', end='')
            print('|')
            print('-'*90)



if __name__ == '__main__':
    verbose = True if '--verbose' in sys.argv else False
    summary(verbose)    
    printMsg(verbose)