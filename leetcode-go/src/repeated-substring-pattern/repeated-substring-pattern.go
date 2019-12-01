package main

import "fmt"

func findSubstring(s string, start1 int, start2 int) (int, int) {
	strlen := len(s)
	i, j := start1+1, start2-1
	for ; i < strlen/2 && i < j; i, j = i+1, j-1 {
		if s[:i] == s[j:] {
			break
		}
	}
	fmt.Printf("Substring: i=%d j=%d %s %s %v\n", i, j, s[:i], s[j:], s[:i] == s[j:])
	return i, j
}

func isRepeating(s string, substr string) bool {
	sslen := len(substr)
	slen := len(s)
	for start := 0; start <= slen-sslen; start = start + sslen {
		if s[start:start+sslen] != substr {
			fmt.Printf("Not repeating %s %s\n", s[start:start+sslen], substr)
			return false
		}
	}
	fmt.Printf("Repeating %s\n", substr)
	return true
}

func repeatedSubstringPattern(s string) bool {
	fmt.Println(s)
	start1, start2 := findSubstring(s, 0, len(s))
	for start1 < start2 {
		if len(s)%len(s[:start1]) != 0 {
			start1, start2 = findSubstring(s, start1, start2)
		} else {
			repeat := isRepeating(s, s[:start1])
			if repeat {
				return repeat
			} else {
				start1, start2 = findSubstring(s, start1, start2)
			}
		}
	}
	if start1 == start2 {
		return isRepeating(s, s[:start1])
	}
	return false
}

func main() {
	fmt.Println(repeatedSubstringPattern("pradeepgpradeepgpradeepg"))
	fmt.Println(repeatedSubstringPattern("pradeepgpradeepgpradeep"))
	fmt.Println(repeatedSubstringPattern("abab"))
	fmt.Println(repeatedSubstringPattern("abaababaab"))
}
