class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        max_factor = max(factor for factor, _ in items)
        freq = [0] * (max_factor + 1)
        for factor, _ in items:
            freq[factor] += 1
            
        multiples_count = [0] * (max_factor + 1)
        for f in range(1, max_factor + 1):
            if freq[f] > 0:
                for multiple in range(f, max_factor + 1, f):
                    multiples_count[f] += freq[multiple]
                    
        items.sort(key=lambda x: x[1])
        min_price = items[0][1]
        
        total_items = 0
        
        for factor, price in items:
            if price >= 2 * min_price or budget < price:
                break
                
            available_bonuses = multiples_count[factor] - 1
            if available_bonuses > 0:
                can_buy = min(available_bonuses, budget // price)
                total_items += can_buy * 2
                budget -= can_buy * price
                
        total_items += budget // min_price
        
        return total_items
