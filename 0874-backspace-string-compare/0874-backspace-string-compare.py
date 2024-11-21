class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backspace(text: str):
            st = []

            for ch in text:
                if ch != '#':
                    st.append(ch)
                elif st:
                    st.pop()

            return ''.join(st)

        return backspace(s) == backspace(t)