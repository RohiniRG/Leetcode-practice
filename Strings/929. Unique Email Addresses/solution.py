class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        mailsSent = []
        
        for each in emails:
            local, domain = each.split('@')
            mail = local
            
            if '+' in local:
                required = local.split('+')[0]
                mail = required
                
            
            if '.' in mail:
                parts = mail.split('.')
                joined = ''.join(parts)
                mail = joined
                
            mail += f'@{domain}'
            mailsSent.append(mail)
            
        totalSent = len(set(mailsSent))
        
        return totalSent
                
