#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Do prbs11 calculation

Command input  format:
    output unit n, data0 , data1, data2, data3,....,data n
"""
import sys
class bitCalculate(): 
    def __init__(self): 
        pass
        
    def getBitVal(self,datain, index): 
        """
        brief:git bit value 
        :param datain: input data
        :param index: bit value
        :returns: bit value 0 or 1
        """
        if datain & (1 << index):
            return 1
        else:
            return 0
        
    def getBitsVal(self,datain,bitEnd,bitStr):
        dataout = 0
        for n in range(bitStr,bitEnd+1):
            dataout += datain & (1 << n)
        dataout >>= bitStr
        return dataout 

    def setBitVal(self,datain, index, val):
        """
        brief: change bit value
        :param datain: original data
        :param index:  bit position ,index 0 from right
        :param val:    set bit value
        :returns: new data after bit change
        """
        if val:
            datain = datain | (1 << index)
            return datain 
        else:
            datain & ~(1 << index)
            return datain
        
    def setBitsVal(self,datain,bitEnd,bitStr,val):
        pass
        
    def prbs11(self,datain):
        data = (self.getBitsVal(datain,9,0)<<1) + (self.getBitVal(datain,8)^self.getBitVal(datain,10))
        # print(f'{hex(datain)} prbs11: {hex(data)}')
        return data
        
    def prbs11WithFormat(self,datain,format = 0): 
        prbs11_01 = self.prbs11(datain)
        prbs11_02 = self.prbs11(prbs11_01)
        prbs11_03 = self.prbs11(prbs11_02)
        prbs11_04 = self.prbs11(prbs11_03)
        prbs11_05 = self.prbs11(prbs11_04)
        prbs11_06 = self.prbs11(prbs11_05)
        prbs11_07 = self.prbs11(prbs11_06)
        prbs11_08 = self.prbs11(prbs11_07)
        prbs11_09 = self.prbs11(prbs11_08)
        prbs11_10 = self.prbs11(prbs11_09)
        prbs11_11 = self.prbs11(prbs11_10)
        prbs11_12 = self.prbs11(prbs11_11)
        random0 =  (self.getBitVal(prbs11_11,0)<<11) +\
            (self.getBitVal(prbs11_10,0)<<10) + \
            (self.getBitVal(prbs11_09,0)<<9 )+ \
            (self.getBitVal(prbs11_08,0)<<8 )+ \
            (self.getBitVal(prbs11_07,0)<<7 )+ \
            (self.getBitVal(prbs11_06,0)<<6 )+ \
            (self.getBitVal(prbs11_05,0)<<5 )+ \
            (self.getBitVal(prbs11_04,0)<<4 )+ \
            (self.getBitVal(prbs11_03,0)<<3 )+ \
            (self.getBitVal(prbs11_02,0)<<2 )+ \
            (self.getBitVal(prbs11_01,0)<<1 )+ \
            (self.getBitVal(datain,0))  
        random1 =  (self.getBitVal(prbs11_11,1)<<11) +\
            (self.getBitVal(prbs11_10,1)<<10) + \
            (self.getBitVal(prbs11_09,1)<<9 )+ \
            (self.getBitVal(prbs11_08,1)<<8 )+ \
            (self.getBitVal(prbs11_07,1)<<7 )+ \
            (self.getBitVal(prbs11_06,1)<<6 )+ \
            (self.getBitVal(prbs11_05,1)<<5 )+ \
            (self.getBitVal(prbs11_04,1)<<4 )+ \
            (self.getBitVal(prbs11_03,1)<<3 )+ \
            (self.getBitVal(prbs11_02,1)<<2 )+ \
            (self.getBitVal(prbs11_01,1)<<1 )+ \
            (self.getBitVal(datain,1))
        if format:
            print(f"12bit data format of prbs11 data {hex(datain)}:")
            print(f'port0 prbs11: {hex(random0)}')
            print(f'port1 prbs11: {hex(random1)}')
        else:
            print(f"8bit data format of prbs11 data {hex(datain)}:")
            print(f'port0 prbs11: {hex(random0 & 0x0fff)}')
            print(f'port1 prbs11: {hex(random1 & 0x0fff)}\n')
        return prbs11_12      

a = bitCalculate()
datain = a.prbs11WithFormat(0x7ff)
datain = a.prbs11WithFormat(datain)
datain = a.prbs11WithFormat(datain)
datain = a.prbs11WithFormat(datain)
datain = a.prbs11WithFormat(datain)
datain = a.prbs11WithFormat(datain)
datain = a.prbs11WithFormat(datain)
datain = a.prbs11WithFormat(datain)
datain = a.prbs11WithFormat(datain)
datain = a.prbs11WithFormat(datain)