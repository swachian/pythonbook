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

    def buy(self, last_status):
        if (not last_status):
            self.buyed = True
            self.buy_price = self.price
            self.profit = 0
            return self
        else:
            if (last_status.buyed == False):
                last_status.buy_price = self.price
                last_status.buyed = True
                return None
            if (last_status.buyed):
                return None

    def sell(self, last_status):
        if (not last_status):
            return None
        else:
            if (last_status.buyed == False):
                return None
            if (last_status.buyed):
                sold_status = StatusEachDay(self.price)
                sold_status.sold_price = self.price
                sold_status.buy_price = last_status.buy_price
                sold_status.profit = sold_status.sold_price - sold_status.buy_price
                sold_status.sold = True 
                return sold_status

class Solution:
    def maxProfit(self, prices):
        self.max_profit = 0
        self.min_buy_price = prices[0]
        statuses = []
        for price in prices:
            self.next_price(price, statuses)
        return self.max_profit

    def next_price(self, price, statuses):
        status = StatusEachDay(price)

        i = 0
        while i < len(statuses):
            last_status = statuses[i]
            if last_status.buy_price != self.min_buy_price:
                del statuses[i] 
                continue
            if last_status.sold:
                del statuses[i]
                continue
            elif last_status.buyed:
                next_status = status.sell(last_status)
                if next_status.profit > self.max_profit:
                    self.max_profit = next_status.profit
            i += 1
        if self.min_buy_price > price or len(statuses) == 0:
            next_status = status.buy(None)
            self.min_buy_price = price
            statuses.append(next_status)
        

solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))
print(solution.maxProfit([7,6,4,3,1]))
print(solution.maxProfit([2,1,2,1,0,1,2]))
print(solution.maxProfit([1,2]))
