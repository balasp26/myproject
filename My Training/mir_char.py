# # function to mirror characters of a string
#
# def mirrorChars(input, k):
# 	# create dictionary
# 	original = 'abcdefghijklmnopqrstuvwxyz'
# 	print("The Original is {}".format(original))
# 	reverse = 'zyxwvutsrqponmlkjihgfedcba'
# 	print("The Reversal is {}".format(reverse))
# 	dictChars = dict(zip(original, reverse))
# 	print("The Dictchars are {}".format(dictChars))
#
# 	# separate out string after length k to change
# 	# characters in mirror
# 	prefix = input[0:k - 1]
# 	print("The Prefix is {}".format(prefix))
# 	suffix = input[k - 1:]
# 	print("The Suffix is {}".format(suffix))
# 	mirror = ''
#
# 	# change into mirror
# 	for i in range(0, len(suffix)):
# 		mirror = mirror + dictChars[suffix[i]]
# 		print("The Mirror is {}".format(mirror))
#
# 	# concat prefix and mirrored part
# 	print(prefix + mirror)
#
#
# # Driver program
# if __name__ == "__main__":
# 	input = 'paradox'
# 	k = 3
# 	mirrorChars(input, k)


def family():
	male = ['Bala', 'Manoj', 'Vasu', 'Prabakaran']
	female = ['Lavanyaa', 'Ramya', 'Kalaiselvi', 'Geethanjali']
	kudumbam = dict(zip(male, female))
	print(kudumbam)

family()