# leetcode_py
Python version of leetcode problems

#### 33 Search in Rotated Sorted Array
问题：找到经过旋转的有序数组中是否有目标的数。

解法：基于二分的方法，根据 `target`、`num[0]`、`nums[mid]` 的大小关系判断向哪个方向搜索。

#### 34 Find First and Last Position of Element in Sorted Array
问题：找到第一个和最后一个等于 `target` 的位置。

解法：三次二分，第一次找到任意一个等于 `target` 的位置 `temp`，如果没有找到返回 `[-1, -1]`。第二次从 `temp` 向左找，第三次从 `temp` 向右找。

重点：二分的编写，条件的设置。

#### 35 Search Insert Position
问题：找到 `nums` 数组中 `target` 的位置。如果不存在，返回在 `nums` 中插入 `target` 的位置。

解法：问题等价于返回第一个 `>= target` 的数，设置好条件即可。

#### 36 Valid Sudoku
问题：判断一个 Sudoku 的棋盘是否有效。

解法：问题即判断棋盘中的每行、每列和每个单元中，是否有重复的数字。设置三个数组，每检测到一个数就对对应的数组位置设置为 `True`，如果已经为 `True` 则返回 `False`。

#### 37 Sudoku Solver
问题：解决数独。

解法：深度优先搜索。(1) 同上设置 `rows`、`cols`、`cells` 三个数组，并利用棋盘中已经有的数字进行初始化；(2) 对每一个空着的格子，分别尝试每一个数；(3) 对之后的棋盘进行类似的操作，如果已经没有数可以填了，则返回 False；(4) 当棋盘已经填满后，返回 True。

#### 38 Count and Say
问题：
