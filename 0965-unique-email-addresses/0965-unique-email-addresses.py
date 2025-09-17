class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for email in emails:
            local , domain = email.split('@')

            if '+' in local:
                local = local.split('+')[0]

            local = local.replace('.','')

            normalized = local + '@' + domain

            unique.add(normalized)
            
        return len(unique)
