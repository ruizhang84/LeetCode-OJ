class NumArray

=begin
    :type nums: Integer[]
=end
    def initialize(nums)
        @dp = []
        total = 0
        nums.each do |x|
            total += x
            @dp.push(total)
        end
       
    end


=begin
    :type i: Integer
    :type j: Integer
    :rtype: Integer
=end
    def sum_range(i, j)
        return i > 0? @dp[j] - @dp[i-1]: @dp[j]
    end


end

# Your NumArray object will be instantiated and called as such:
# obj = NumArray.new(nums)
# param_1 = obj.sum_range(i,j)
