letter = ''' Dear <|Name|>
            you are selected!
            <|Date|>'''

print(letter.replace("<|Name|>", "Prachi").replace("<|Date|>", "3 December 2025 "))