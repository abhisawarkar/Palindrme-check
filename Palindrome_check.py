def palindrome(original):
	originalL=list(original)
	start=0
	end=len(original)-1
	while start <= end:
		if originalL[start] == originalL[end]:
			pass
		else:
			return "Not a palindrome"
		start += 1
		end -= 1
	return "Palindrome"

print palindrome("nirtin")
	

    
