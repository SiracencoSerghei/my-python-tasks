def past(h, m, s):
    # Good Luck!
    
    m_s_in_sec = 1000
    m_s_in_minute = m_s_in_sec * 60
    m_s_in_hour = m_s_in_minute * 60
    
     
    result = m_s_in_hour * h + m_s_in_minute * m + m_s_in_sec * s
    return result
    
past(0, 1, 1)

print(past(0, 1, 1))

