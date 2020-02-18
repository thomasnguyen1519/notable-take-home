
import re


# driver code
def main():
    # change this to any desired input
    transcription = 'Patient presents today with several issues. Number one BMI has increased by 10% since their last visit. Number next patient reports experiencing dizziness several times in the last two weeks. Number next patient has a persistent cough that hasn’t improved for last 4 weeks.'
    trans = transform(transcription)
    print(trans)

# Returns a transformation of the string input that has an ordered list
def transform(transcription):
    start = re.search('Number (?:one|two|three|four|five|six|seven|eight|nine) ', transcription)
    if not start:
        raise ValueError('Input did not have a starting phrase')
    nums_map = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    starting_statement = transcription[start.start():start.end()]
    word_num = starting_statement.split(' ')[1]
    curr_num = nums_map[word_num]
    split_by_items = re.split(' Number (?:one|two|three|four|five|six|seven|eight|nine|next) ', transcription)
    index = 1
    while index < len(split_by_items):
        split_by_items[index] = '\n' + str(curr_num) + '. ' + split_by_items[index][0].capitalize() + split_by_items[index][1:]
        index += 1
        curr_num += 1
    return ''.join(split_by_items)

# python module name guard
if __name__ == '__main__':
    main()
