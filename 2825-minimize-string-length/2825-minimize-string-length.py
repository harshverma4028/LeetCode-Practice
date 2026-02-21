class Solution:
    def minimizedStringLength(self, s: str) -> int:
        
        st = set()
        for word in s:
            if word not in st:
                st.add(word)
        
        return len(st)