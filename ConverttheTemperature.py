class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        kelvin = celsius + 273.15
        fah = celsius * 1.80 + 32.00
        
        res = [float(kelvin), float(fah)]
        return res
