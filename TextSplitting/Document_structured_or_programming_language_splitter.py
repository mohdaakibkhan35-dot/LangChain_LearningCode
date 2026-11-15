from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text = """

class RatInMazeCheckMark4D:
    @staticmethod
    def PrintPath(sr,sc,matrix,s):
        er = len(matrix)-1
        ec = len(matrix[0])-1

        if(sr>er or sc>ec or sr<0 or sc<0): return
        if(sr == er and sc == ec):
            print(s)
            return
        if(matrix[sr][sc] == 0): return
        if(matrix[sr][sc] == -1): return

        matrix[sr][sc] = -1

        RatInMazeCheckMark4D.PrintPath(sr+1,sc,matrix,s+"R")
        RatInMazeCheckMark4D.PrintPath(sr,sc+1,matrix,s+"D")
        RatInMazeCheckMark4D.PrintPath(sr-1,sc,matrix,s+"L")
        RatInMazeCheckMark4D.PrintPath(sr,sc-1,matrix,s+"U")

        matrix[sr][sc] = 1


List = [[1,0,1,1,1,1],
        [1,1,0,1,0,1],
        [0,1,1,1,1,1],
        [0,0,1,0,1,1]]


ans = RatInMazeCheckMark4D.PrintPath(1, 1, List, "")

print(ans)

class fibbanoci:
    def __init__(self, n):
        self.n = n

    def fib(self):
        n = self.n

        if n == 1 or n == 2: return 1
        return fibbanoci(n-1).fib() + fibbanoci(n-2).fib()
for i in range(1,7):
    print(f"fibbanoci sum of number {'i'}",fibbanoci(i).fib())



class fibb:
    @staticmethod
    def fib(n):
        if n == 0 or n == 1: return 1
        return fibb.fib(n - 1) + fibb.fib(n - 2)


ans = fibb.fib(4)
print(ans)


def fib(n):
    if n is 0 or n is 1: return n
    return fib(n-1)+fib(n-2)

ans = fib(5)
print(ans)

"""
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=500,
    chunk_overlap=0
)
chunks = splitter.split_text(text)

print(len(chunks))

print(chunks[0])



