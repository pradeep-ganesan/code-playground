package main

import "fmt"

func maxLeft(grid [][]int) []int {
	leftHeight := make([]int, len(grid[0]))
	for x := 0; x < len(grid[0]); x++ {
		for y := 0; y < len(grid); y++ {
			if leftHeight[x] < grid[x][y] {
				leftHeight[x] = grid[x][y]
			}
		}
	}
	fmt.Println(leftHeight)
	return leftHeight
}

func maxTop(grid [][]int) []int {
	topHeight := make([]int, len(grid))
	for y := 0; y < len(grid); y++ {
		for x := 0; x < len(grid[y]); x++ {
			if topHeight[y] < grid[x][y] {
				topHeight[y] = grid[x][y]
			}
		}
	}
	fmt.Println(topHeight)
	return topHeight
}

func maxIncreaseKeepingSkyline(grid [][]int) int {
	totalIncrease := 0
	topHeight := maxTop(grid)
	leftHeight := maxLeft(grid)
	for y := 0; y < len(grid); y++ {
		for x := 0; x < len(grid[y]); x++ {
			if grid[x][y] < topHeight[y] {
				totalIncrease = totalIncrease + (topHeight[y] - grid[x][y])
			}
		}
	}
	for x := 0; x < len(grid[0]); x++ {
		for y := 0; y < len(grid); y++ {
			if topHeight[y] > leftHeight[x] {
				totalIncrease = totalIncrease - (topHeight[y] - leftHeight[x])
			}
		}
	}
	return totalIncrease
}

func main() {
	grid := [][]int{{3, 0, 8, 4}, {2, 4, 5, 7}, {9, 2, 6, 3}, {0, 3, 1, 0}}
	sum := maxIncreaseKeepingSkyline(grid)
	fmt.Printf("Total increase: %d\n", sum)
}
