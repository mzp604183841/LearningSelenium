'''函数作为返回值'''


def lazy_mzp_sum(*args):
    def mzp_sum():
        ax = 0
        for num in args:
            ax = ax + num
            return ax
        return mzp_sum
