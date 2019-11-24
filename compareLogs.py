with open("cleaned-evaluator-integration.txt", "r") as f:
	log = f.read().splitlines()


#dict for segment key, cookie values
dictOfSegmentKeys = {}
#dict for cookie key, segment values
dictOfCookiesKeys = {}

#for each line make two dicts: one for cookies as key, and the other segments as key
for line in log:
	segmantAndCookies = line.split(", ")
	segmantAndCookies = filter(None, segmantAndCookies)

	cookie = segmantAndCookies[0]
	segments = segmantAndCookies[1:]
	# print cookie, segments
	dictOfCookiesKeys[cookie] = segments

	for segment in segments:
		if segment in dictOfSegmentKeys.keys():
			#append cookie to list
			dictOfSegmentKeys[segment].append(cookie)
		else:
			#create new key with cookie in its list value
			dictOfSegmentKeys[segment] = [cookie]

#opens the file and splits the lines
with open("cleaned-evaluator-integration-baseline.txt", "r") as f:
	log = f.read().splitlines()

#dict for segment key, cookie values
baselineDictOfSegmentKeys = {}
#dict for cookie key, segment values
baselineDictOfCookiesKeys = {}

#for each line make two dicts: one for cookies as key, and the other segments as key
for line in log:
	segmantAndCookies = line.split(", ")
	segmantAndCookies = filter(None, segmantAndCookies)

	cookie = segmantAndCookies[0]
	segments = segmantAndCookies[1:]

	baselineDictOfCookiesKeys[cookie] = segments

	for segment in segments:
		if segment in baselineDictOfSegmentKeys.keys():
			#append cookie to list
			baselineDictOfSegmentKeys[segment].append(cookie)
		else:
			#create new key with cookie in its list value
			baselineDictOfSegmentKeys[segment] = [cookie]

#collects all segments with added cookies and segments with missing cookies
countOfAddedCookies = 0
totalSegments = 0
countOfMissingCookies = 0
dictOfSegmentKeysWithAddedCookies = {}
dictOfSegmentKeysWithMissingCookies = {}
for segment in dictOfSegmentKeys.keys():
	if segment in baselineDictOfSegmentKeys.keys():
		totalSegments += 1
		temp = set(dictOfSegmentKeys[segment]) - set(baselineDictOfSegmentKeys[segment])
		if len(temp) > 0:
			dictOfSegmentKeysWithAddedCookies[segment] = temp 
			countOfAddedCookies += 1
		temp = set(baselineDictOfSegmentKeys[segment]) - set(dictOfSegmentKeys[segment])
		if len(temp) > 0:
			dictOfSegmentKeysWithMissingCookies[segment] = temp
			countOfMissingCookies += 1

#prints all segments with added cookies in specified format
print "Segments with added cookies: ", countOfAddedCookies, "/", totalSegments 
count = 0
for segment in dictOfSegmentKeysWithAddedCookies:
	print count, "\t", segment, "\t", len(dictOfSegmentKeysWithAddedCookies[segment]), "\t", list(dictOfSegmentKeysWithAddedCookies[segment])
	count += 1

#prints all segments with missing cookies in specified format
print "Segments with missing cookies: ", countOfMissingCookies, "/", totalSegments 
count = 0
for segment in dictOfSegmentKeysWithMissingCookies:
	print count, "\t", segment, "\t", len(dictOfSegmentKeysWithMissingCookies[segment]), "\t", list(dictOfSegmentKeysWithMissingCookies[segment])
	count += 1

#collects all cookies with extra segments and cookies omitted from segments
countOfCookiesWithExtraSegments = 0
totalCookies = 0
countOfCookiesOmittedFromSegments = 0
dictOfCookiesKeysWithExtraSegments = {}
dictOfCookiesKeysOmittedFromSegments = {}
for cookie in dictOfCookiesKeys.keys():
	if cookie in baselineDictOfCookiesKeys.keys():
		totalCookies += 1
		temp = set(dictOfCookiesKeys[cookie]) - set(baselineDictOfCookiesKeys[cookie])
		if len(temp) > 0:
			dictOfCookiesKeysWithExtraSegments[cookie] = temp 
			countOfCookiesWithExtraSegments += 1
		temp = set(baselineDictOfCookiesKeys[cookie]) - set(dictOfCookiesKeys[cookie])
		if len(temp) > 0:
			dictOfCookiesKeysOmittedFromSegments[cookie] = temp
			countOfCookiesOmittedFromSegments += 1

#prints all the cookies in extra segments as specified format
print "Cookies in extra segments: ", countOfCookiesWithExtraSegments, "/", totalCookies 
count = 0
for cookie in dictOfCookiesKeysWithExtraSegments:
	print count, "\t", cookie, "\t", len(dictOfCookiesKeysWithExtraSegments[cookie]), "\t", list(dictOfCookiesKeysWithExtraSegments[cookie])
	count += 1

#prints all the cookies omitted from segments as specified format
print "Cookies omitted from segments: ", countOfCookiesOmittedFromSegments, "/", totalCookies 
count = 0
for cookie in dictOfCookiesKeysOmittedFromSegments:
	print count, "\t", cookie, "\t", len(dictOfCookiesKeysOmittedFromSegments[cookie]), "\t", list(dictOfCookiesKeysOmittedFromSegments[cookie])
	count += 1



