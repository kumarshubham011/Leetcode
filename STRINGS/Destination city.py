# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

# METHOD 1
from ast import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dest = {}
        for path in paths:
            citya, cityb = path
            # if city in dest then we will increment the value by 1 else we will set its value to 0.
            # for this we will use .get(keyname,value), value is predefined which is set when key is not present in dictionary.
            dest[citya] = dest.get(citya, 0)+1
            dest[cityb] = dest.get(cityb, 0)

        # now we will check for every key in dest if its value is zero then it will be answer
        for city in dest:
            if dest[city] == 0:
                return city


# METHOD 2

    def destCity(self, paths: List[List[str]]) -> str:
        starts, ends = set(), set()
        for path in paths:
            starts.add(path[0])
            ends.add(path[1])

        return (ends-starts).pop()
