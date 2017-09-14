class SeqList(object):
    def __init__(self, nseq=None, nqueries=None):
        self.nseq = int(nseq)
        self.nqueries = int(nqueries)
        self.lastAnswer = 0
        self.seq = []
        for _ in xrange(self.nseq):
            self.seq.append([])

    def find_answer(self):
        queries = []
        for _ in xrange(self.nqueries):
            query = raw_input('Query: ').split(' ')
            queries.append(query)

        for query in queries:
            qtype = int(query[0])
            x = int(query[1])
            y = int(query[2])
            seqid = (x ^ self.lastAnswer) % self.nseq
            if qtype == 1:
                self.seq[seqid].append(y)
            elif qtype == 2:
                self.lastAnswer = self.seq[seqid][y % len(self.seq[seqid])]
                print self.lastAnswer

if __name__ == '__main__':
    inp = raw_input('N Q: ').split(' ')
    sequence = SeqList(inp[0], inp[1])
    sequence.find_answer()