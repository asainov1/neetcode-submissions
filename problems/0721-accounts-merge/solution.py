class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)
        was = [False] * len(accounts)
        res = []
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                graph[email].append(i) 

        #%%
        def dfs (i, emails):
            if was[i]:
                return
            was[i] = True
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                for nei in graph[email]:
                    dfs(nei, emails)



        for i, account in enumerate(accounts):
            if was[i]:
                continue
            name = account[0]
            emails = set()
            dfs(i, emails) # updates / fills emails 
            res.append([name] + sorted(emails))
        return (res)
