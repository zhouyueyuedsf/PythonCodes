from ADT import Stack

VALIDTAGS = []
EXCEPTIONS = ['br', 'hr', 'meta']

def getTags(filename):
	infile = open(filename, "r")
	htmlStr = infile.read()
	infile.close()
	tagList = []
	while htmlStr != "":
		if htmlStr[0] != '<':
			htmlStr = htmlStr[1:]
		else:
			index = htmlStr.find('>')
			whitespaceIndex = htmlStr.find(' ')
			if whitespaceIndex < index and whitespaceIndex != -1:
				tag = htmlStr[1:whitespaceIndex]
			else:
				tag = htmlStr[1:index]
			tagList.append(tag)
			htmlStr = htmlStr[index + 1:]
	print(tagList)
	return tagList

def checkTags(tagList):
	stack = Stack()
	errorType = -1
	for tag in tagList:
		flag = 0
		for valid_tag in VALIDTAGS:
			if valid_tag == tag:
				flag = 1
		if flag == 0:
			VALIDTAGS.append(tag)
			print("New tag " + tag + " found and added to list of valid tags")
		if tag[0] == '/':
			if stack.size() == 0:
				print("Error:  tag is " + tag + " but stack is empty.")
				errorType = 1
				break
			elif stack.top() == tag[1:]:
				stack.pop()
				print("Tag " + tag + " matches top of stack: stack is now " + str(stack.items))
			else:
				print("Error:  tag is " + tag + " but top of stack is " + str(stack.top()))
				errorType = 2
				break
		elif tag == EXCEPTIONS[0] or tag == EXCEPTIONS[1] or tag == EXCEPTIONS[2]:
			print("Tag " + tag + " does not need to match: stack is still " + str(stack.items))
		else:
			stack.push(tag)
	if errorType == -1:
		if stack.size() == 0:
			print("Processing complete. No mismatches found.")
		else:
			print("Processing complete. Unmatched tags remain on stack: " + str(stack.items))
	print("VALIDTAGS are these: " + str(VALIDTAGS))
	print("EXCEPTIONS are these: " + str(EXCEPTIONS))

def main():
	tagList = getTags("test5.html")
	checkTags(tagList)

main()