# leetcode_py
python version of leetcode problems

#### 33 Search in Rotated Sorted Array
问题：找到经过旋转的有序数组中是否有目标的数。
描述：基于二分的方法，根据 `target`、`num[0]`、`nums[mid]` 的大小关系判断向哪个方向搜索。