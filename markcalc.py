#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    calcmymarks.markcalc
    ~~~~~~~~~~~~~~~~~~~~

    The mark calculator object

    :copyright: (c) 2009-2011 by Aaron Toth.
    :license: Apache 2.0, see LICENSE for more details.
"""

class MarkCalc(object):
    """A mark calculator"""
    def __init__(self, current):
        super(MarkCalc, self).__init__()
        self.current_mark= 0.0
        self.current_total = 0.0
        self.current = current
        self.process_existing()
        
    def process_existing(self):
        """Process current marks"""
        for i in range(len(self.current)):
            self.current_mark += (self.current[i][0]/100) * self.current[i][2]
            self.current_total += self.current[i][2]
        
    def exam_total(self):
        """Gets the exam total"""
        return 100.0 - self.current_total
        
    def needed(self, goal):
        """Calculates the mark needed on an exam given overall mark goal"""
        return ((goal - self.current_mark) / self.exam_total()) * 100
        
    def whatif(self, grade):
        """Calculates grade if you got a certain mark on the exam"""
        return self.current_mark + (grade / 100.0) * self.exam_total()
        
if __name__ == '__main__':
    curr = [[63.0, "Midterm", 70.0],]
    mk = MarkCalc(curr)
    print mk.exam_total()
    print mk.current_mark
    print mk.current_total
    print "%0.0f" % mk.needed(74)
    print "%0.2f" % mk.whatif(90)
