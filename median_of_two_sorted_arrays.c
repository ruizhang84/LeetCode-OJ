#include <stdio.h>

/* get meidan of an array nums1 and a numbe nums2  */
double getMedian(int* nums1, int* nums2, int size){
    int median, median_left, median_right;
    if (size%2 == 0){
        median_left = nums1[(size-1)/2];
        median_right = nums1[size/2];
        if (nums2[0] < median_left){
            return median_left;
        }else if (nums2[0] > median_right){
            return median_right;
        }else{
            return nums2[0];
        }
    }else{
        median = nums1[(size-1)/2];
        median_left = nums1[(size-3)/2];
        median_right = nums1[(size+1)/2];
        
        if (nums2[0] < median_left){
            return (median_left + median)/2.0;
        }else if (nums2[0] > median_right){
            return (median_right + median)/2.0;
        }else{
            return (nums2[0] + median)/2.0;
        }
    }
}

/* find max and min of two values*/
int max (int x, int y){
    return x > y? x: y;
}

int min(int x, int y){
    return x > y? y: x;
}

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    double median1, median2;
    /* base case */
    if (nums1Size == 0){
        return  nums2Size%2 == 0? (nums2[(nums2Size-1)/2]+nums2[nums2Size/2])/2.0: nums2[(nums2Size-1)/2];
    }else if(nums2Size == 0){
        return  nums1Size%2 == 0? (nums1[(nums1Size-1)/2]+nums1[nums1Size/2])/2.0: nums1[(nums1Size-1)/2];
    }else if(nums1Size ==1 && nums2Size ==1){
        return (nums1[0]+nums2[0])/2.0;
    }else if(nums1Size == 1){
        return getMedian(nums2, nums1, nums2Size);
    }else if(nums2Size == 1){
        return getMedian(nums1, nums2, nums1Size);
    }else if (nums1Size == 2 && nums2Size == 2){
        return (max(nums1[0], nums2[0])+min(nums1[1],nums2[1]))/2.0;
    }
    
    /* find meidan */
    median1 = nums1Size%2 == 0? (nums1[nums1Size/2]+nums1[nums1Size/2-1])/2.0: nums1[(nums1Size-1)/2];
    median2 = nums2Size%2 == 0? (nums2[nums2Size/2]+nums2[nums2Size/2-1])/2.0: nums2[(nums2Size-1)/2];
    if (nums2Size %2 == 0 && median1 < nums2[nums2Size/2] && median1 > nums2[nums2Size/2-1]){
        if (nums1Size %2 == 0){
            return (max(nums1[nums1Size/2-1], nums2[nums2Size/2-1])+min(nums1[nums1Size/2], nums2[nums2Size/2]))/2.0;
        }else{
            return median1;
        }
    }else if (nums1Size %2 == 0 && median2 < nums1[nums1Size/2] && median2 > nums1[nums1Size/2-1]){
        if (nums2Size %2 == 0){
            return (max(nums1[nums1Size/2-1], nums2[nums2Size/2-1])+min(nums1[nums1Size/2], nums2[nums2Size/2]))/2.0;
        }else{
            return median2;
        }
    }
    
    /* binary search sub arrary*/
    if (median1 == median2){
        return median1;
    }else if (median1 < median2){
        int nums1prev = nums1Size;
        int nums2prev = nums2Size;
        nums1Size = nums1Size%2 == 0? nums1Size/2: (nums1Size-1)/2;
        nums2Size = nums2Size%2 == 0? nums2Size/2: (nums2Size-1)/2;
        findMedianSortedArrays( nums1+min(nums1Size, nums2Size), nums1prev-min(nums1Size, nums2Size), nums2,  nums2prev-min(nums1Size, nums2Size));
    }else{
        int nums1prev = nums1Size;
        int nums2prev = nums2Size;
        nums1Size = nums1Size%2 == 0? nums1Size/2: (nums1Size-1)/2;
        nums2Size = nums2Size%2 == 0? nums2Size/2: (nums2Size-1)/2;
        findMedianSortedArrays( nums1, nums1prev-min(nums1Size, nums2Size), nums2+min(nums1Size, nums2Size), nums2prev-min(nums1Size, nums2Size));
    }
    
}


int main(){
    int num1[2] = {1, 2};
    int num2[2] = {3, 4};
    printf ("The number is : %.3f \n", findMedianSortedArrays(num1, 2, num2, 2));
    return 0;
