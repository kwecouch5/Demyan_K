def maxProfit(prices):
    m_price=0
    profit=0
    dp=[0]*len(prices)
    for i in range(len(prices)):
        if m_price>prices[i]:
            m_price=prices[i]
        elif prices[i]-m_price > profit:
            profit =prices[i]-m_price
    return profit


print(maxProfit([7,1,5,3,6,4]))