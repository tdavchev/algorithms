
from collections import deque, defaultdict


class Trie(object):
	def __init__(self):
		self.store = defaultdict(Trie)
	def add(self, l):
		return self.store[l]

def build_trie(words):
	root = Trie()
	for word in words:
		node = root
		for l in word:
			node = node.add(l)
	return root

class Solution(object):
	def solve(self, beg_word, end_word, words):
		self.beg_word = beg_word
		self.end_word = end_word
		self.words = words
		self.trie = build_trie(words)
		
		visited = set([beg_word])
		fringe = deque([(beg_word, [])])
		shortest_length = -1
		ans = []
		while fringe:
			word, path = fringe.popleft()
			if shortest_length != -1 and len(path) > shortest_length:
				continue
			if word == end_word and shortest_length == -1:
				shortest_length = len(path)
				ans.append(path)
				continue
			if word == end_word and shortest_length == len(path):
				ans.append(path)
				continue
			for nb in self.get_nbs(word):
				if nb in visited:
					continue
				visited.add(nb)
				fringe.append((nb, path + [word]))
		return ans

	def get_nbs(self, word):
		nbs = []
		# for the current letter
		# if exact match i proceed 
		# else i find all that are different and then proceed to exact match
		#      and i procced to my 
		fringee = [(self.trie, '', False)]
		while fringee:
			node, suffix, exact_match = fringee.pop()
			if exact_match and len(suffix) == len(word):
				nbs.append(suffix)
				continue
			w = word[len(suffix)]
			if exact_match:
				while w in node.store:
					suffix += w
					node = node.store[w]
					if len(suffix) == len(word):
						break
					w = word[len(suffix)]
				if len(suffix) == len(word):
					nbs.append(suffix)
				continue


			for l, n in node.store.items():
				if l != w:
					fringee.append((n, suffix + l, True))
			
			if w in node.store:
				fringee.append((node.store[w], suffix + w, False))
		return nbs

solution = Solution()
normal_list = ["hot","dot","dog","lot","log","cog"]
print(solution.solve("hit", "cog", normal_list))
# assert solution.solve("hit", "cog", normal_list) == [["hit","hot","lot","log","cog"], ["hit","hot","dot","dog","cog"]] or solution.findLaddersNOTFeasible("hit", "cog", normal_list) == [["hit","hot","dot","dog","cog"], ["hit","hot","lot","log","cog"]]
