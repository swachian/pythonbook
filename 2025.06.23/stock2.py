# 7 1 5
# b s 
# b n s
# b n n
# n b s
# n b s
# n n b
# n n n
class StatusEachDay:
    def __init__(self, price):
        self.price = price
        self.buyed = False
        self.sold = False
        self.profit = 0

    def buy(self, last_status):
        if (not last_status):
            self.buyed = True
            self.buy_price = self.price
            return self
        else:
            if (last_status.buyed == False):
                buy_status = StatusEachDay(self.price)
                buy_status.buy_price = self.price
                buy_status.buyed = True
                return buy_status
            if (last_status.sold == True):
                buy_status = StatusEachDay(self.price)
                buy_status.buy_price = self.price
                buy_status.buyed = True
                buy_status.profit = last_status.profit
                return buy_status

    def sell(self, last_status):
        if (not last_status):
            return None
        else:
            if (last_status.buyed == False):
                return None
            if (last_status.buyed and last_status.sold == False):
                sold_status = StatusEachDay(self.price)
                sold_status.sold_price = self.price
                sold_status.buyed = self.buyed
                sold_status.buy_price = last_status.buy_price
                if (sold_status.sold_price - sold_status.buy_price) <= 0:
                    return None
                sold_status.profit = sold_status.sold_price - sold_status.buy_price + last_status.profit
                sold_status.sold = True 
                return sold_status

class Solution:
    def maxProfit(self, prices):
        self.max_profit = 0
        self.min_buy_price = prices[0]
        statuses = []
        for price in prices:
            self.next_price(price, statuses)
        self.max_profit = max(map(lambda x: x.profit, statuses))
    
        return self.max_profit

    def next_price(self, price, statuses):
        status = StatusEachDay(price)
        statuses.append(status.buy(None))


        i = 0
        l = len(statuses)
        while i < l:
            last_status = statuses[i]
            next_status = status.buy(last_status)
            if next_status:
                statuses.append(next_status)
            next_status = status.sell(last_status)
            if next_status:
                statuses.append(next_status)
            i += 1

        

solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))
# print(solution.maxProfit([7,6,4,3,1]))
# print(solution.maxProfit([2,1,2,1,0,1,2]))
print(solution.maxProfit([34,82,16,74,55,46,44,25,96,80,51,62,73,26,76,30,20,30,55,6,3,93,74,80,8,13,3,82,1,35,68,22,81,63,77,41,51,84,36,46,86,71,5,65,65,91,97,57,92,96,57,97,74,33,19,42,44,22,12,26]))
