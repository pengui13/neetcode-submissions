def sort_func(e):
    return e[1]
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elem_counter = {}
        for el in nums:
            elem_counter[el] = elem_counter.get(el,0) + 1
        items = list(elem_counter.items())
        items.sort(key = sort_func, reverse=True)
        items_to_delete = len(items) - k
        for i in range(0, items_to_delete):
            items.pop()
        return [el[0] for el in items]