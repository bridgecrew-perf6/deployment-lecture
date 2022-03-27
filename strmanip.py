import argparse

def manipulator(text:str, first:int=-1, last:int=-1, upper:bool=False, reverse_sentence:bool=False):
    words = text.split()
    
    # Choose which first or last words to take, or just skip this
    words_fl = []
    if first > 0:
        words_fl = words[:first]
    if last > 0: 
        words_fl += words[-last:]
    
    if len(words_fl)>0:
        ret_words = words_fl
    else:
        ret_words = words
    
    ret_text = ' '.join(ret_words)
    if upper:
        ret_text = ret_text.upper()
    if reverse_sentence:
        ret_text = ret_text[::-1]
        
    return ret_text
        
def main():

    strmanip_parser = argparse.ArgumentParser(description='Apply various manipulations to input strings')
    
    strmanip_parser.add_argument('text', type=str, help='The string to manipulate')
    strmanip_parser.add_argument('--first', default=-1, type=int, help='How many words from the beginning to include')
    strmanip_parser.add_argument('--last', default=-1, type=int, help='How many words from the end to include')
    strmanip_parser.add_argument('-U', '--upper', action='store_true', help='Turn sentence to uppercase')
    strmanip_parser.add_argument('--reverse-sentence', action='store_true', help='Reverse character order')

    args = strmanip_parser.parse_args()
    
    print(
        manipulator(args.text, args.first, args.last, args.upper, args.reverse_sentence)
        )
    return 0

if __name__ == "__main__":
    main()