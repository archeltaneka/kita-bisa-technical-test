class Problem1UnitTest():
    
    """
    Unit Test for Problem 1
    
    """
    
    def positive_number_test(self, boxes, cakes, apples):
        """
        Check whether 'boxes', 'cakes', and 'apples' variables are greather than 0
        """
        
        assert boxes > 0 and cakes > 0 and apples > 0, 'The number of boxes, apples, and cakes in the box should be greater than 0!'

    def cake_test(self, boxes, cakes, total_cakes):
        """
        Check whether the number of cakes in each box is equal across all boxes
        """
        
        assert boxes * cakes == total_cakes, 'The number of cakes in each box do not match!'

    def apple_test(self, boxes, apples, total_apples):
        """
        Check whether the number of cakes in each box is equal across all boxes
        """
        
        assert boxes * apples == total_apples, 'The number of apples in each box do not match!'